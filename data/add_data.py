import pandas as pd
import os
import glob
from datetime import datetime, timedelta

# Configuration
MASTER_FILE = '/Users/khoale/Desktop/Customer-Churn-Project/data/telecom_churn.csv'
NEW_DATA_FOLDER = '/Users/khoale/Desktop/Customer-Churn-Project/data/new_data' 

def ingest_new_data():
    # 1. Load the Master File (if it exists)
    if os.path.exists(MASTER_FILE):
        df_master = pd.read_csv(MASTER_FILE)
    else:
        df_master = pd.DataFrame()

    # 2. Check for legacy data (missing Feast columns)
    if not df_master.empty:
        if 'event_timestamp' not in df_master.columns:
            print("Legacy data detected. Initializing timestamps and IDs...")
            # Set legacy data to 1 day ago so it looks like "past" data
            df_master['event_timestamp'] = datetime.now() - timedelta(days=1)
            df_master["event_timestamp"] = pd.to_datetime(df_master["event_timestamp"], utc=True)

        if 'customer_id' not in df_master.columns:
            df_master['customer_id'] = range(len(df_master))

    # 3. Find all new CSV files
    new_files = glob.glob(os.path.join(NEW_DATA_FOLDER, "*.csv"))
    
    if not new_files:
        if 'event_timestamp' in df_master.columns:
            print("No new files found, but Master File is already updated.")
            return
        else:
            print("No new data found and no Master File to update.")
            return

    print(f"Found {len(new_files)} new file(s). Processing...")

    new_data_frames = [df_master]
    
    for file_path in new_files:
        df_new = pd.read_csv(file_path)
        
        # Add Feast columns to the NEW data
        df_new['event_timestamp'] = datetime.now()
        
        # Determine the next available customer_id
        start_id = df_master['customer_id'].max() + 1 if not df_master.empty else 0
        df_new['customer_id'] = range(int(start_id), int(start_id) + len(df_new))
        
        new_data_frames.append(df_new)
        
        # Clean up the folder
        os.remove(file_path)
        print(f"Processed: {file_path}")

    # 4. Concatenate and Overwrite the Master File
    df_final = pd.concat(new_data_frames, ignore_index=True)
    df_final.to_csv(MASTER_FILE, index=False)
    print(f"Ingestion complete. Master file now has {len(df_final)} rows with timestamps.")

if __name__ == "__main__":
    ingest_new_data()