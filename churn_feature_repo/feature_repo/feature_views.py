from datetime import timedelta
from entities import customer
from feast import Field, FeatureView, FileSource
from feast.types import Float32, Int64, Float64

# 1. Point to your Parquet file
path = "data/processed_churn_data.parquet" # Path relative to feature_repo
file_source = FileSource(
    path=path,
    timestamp_field="event_timestamp",
)

# 2. Define the Feature View
churn_feature_view = FeatureView(
    name="churn_features",
    entities=[customer],
    ttl=timedelta(days=365), # How far back Feast should look for features
    schema=[
        Field(name="AccountWeeks", dtype=Float64),
        Field(name="ContractRenewal", dtype=Float64),
        Field(name="DataPlan", dtype=Float64),
        Field(name="DataUsage", dtype=Float64),
        Field(name="CustServCalls", dtype=Float64),
        Field(name="DayMins", dtype=Float64),
        Field(name="DayCalls", dtype=Float64),
        Field(name="MonthlyCharge", dtype=Float64),
        Field(name="OverageFee", dtype=Float64),
        Field(name="RoamMins", dtype=Float64),
        Field(name="MinsPerDayCall", dtype=Float64),
        Field(name="UnderusingData", dtype=Float64),
        # Note: We usually don't include the target 'Churn' here 
        # as a feature, but keep it in the parquet for training.
    ],
    online=True,
    source=file_source,
)