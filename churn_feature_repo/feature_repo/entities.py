from feast import Entity, ValueType

customer = Entity(
    name="customer_id", 
    join_keys=["customer_id"], 
    description="Customer ID for churn prediction",
    value_type=ValueType.INT64,
)
