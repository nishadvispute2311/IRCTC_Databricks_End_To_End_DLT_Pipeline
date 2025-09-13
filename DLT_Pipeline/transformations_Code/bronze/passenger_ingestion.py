import dlt
from pyspark.sql.functions import *

passenger_rules = {
    "rule1" : "passenger_id is not null",
    "rule2" : "age >= 18"
}

@dlt.table(
    name = "passenger_staging"
)
@dlt.expect_all_or_drop(passenger_rules)
def passenger_staging():
    df = spark.readStream.table("irctc_catalog.raw_data.Passengers")
    df = df.withColumn("ingest_ts",current_timestamp())
    return df