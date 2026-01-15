from feast import FeatureStore

store = FeatureStore(repo_path="/Users/khoale/Desktop/Customer-Churn-Project/churn_feature_repo/feature_repo")
feature_vector = store.get_online_features(
    features=[
        "churn_features:DayMins",
        "churn_features:CustServCalls",
        "churn_features:MinsPerDayCall",
        "churn_features:UnderusingData"
    ],
    entity_rows=[{"customer_id": 0}]
).to_dict()

print(feature_vector)
