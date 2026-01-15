from feast import FeatureStore
import pandas as pd
from datetime import datetime

store = FeatureStore(repo_path="/Users/khoale/Desktop/Customer-Churn-Project/churn_feature_repo/feature_repo")

# Simulate a training "entity dataframe"
# This is a list of IDs and the time we want their features from
entity_df = pd.DataFrame.from_dict({
    "customer_id": [10, 20, 30],
    "event_timestamp": [datetime.now(), datetime.now(), datetime.now()]
})

training_df = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "churn_features:DayMins",
        "churn_features:MonthlyCharge",
        "churn_features:ContractRenewal"
    ],
).to_df()

print("--- Offline Historical Features ---")
print(training_df.head())