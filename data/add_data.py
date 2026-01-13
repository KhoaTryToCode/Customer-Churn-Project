import pandas as pd
import os
import glob

# Configuration
MASTER_FILE = '/Users/khoale/Desktop/Customer-Churn-Project/data/telecom_churn.csv'
NEW_DATA_FOLDER = '/Users/khoale/Desktop/Customer-Churn-Project/data/new_data'  # Create this folder!

def ingest_new_data():
    # 1. Find all CSV files in the incoming folder
    new_files = glob.glob(os.path.join(NEW_DATA_FOLDER, "*.csv"))
    
    if not new_files:
        print("No new data found.")
        return

    print(f"Found {len(new_files)} new file(s). Appending...")

    for file_path in new_files:
        # 2. Read the new data
        df_new = pd.read_csv(file_path)
        
        # 3. Append to master file
        # mode='a' means append
        # header=False prevents adding the column names again in the middle of the file
        df_new.to_csv(MASTER_FILE, mode='a', index=False, header=False)
        
        # 4. Delete the processed file
        os.remove(file_path)
        print(f"Successfully processed and deleted: {file_path}")

    print("Ingestion complete.")

# Run the function
ingest_new_data()