import dlt
from pyspark.sql.functions import *

train_rules = {
    "rule1" : "train_no is not null"
}

@dlt.table(
    name = "trains_data"
)
@dlt.expect_all_or_drop(train_rules)
def trains_data():
    df = spark.readStream.table("irctc_catalog.raw_data.Trains")
    df = df.withColumn("ingest_ts",current_timestamp())
    return df