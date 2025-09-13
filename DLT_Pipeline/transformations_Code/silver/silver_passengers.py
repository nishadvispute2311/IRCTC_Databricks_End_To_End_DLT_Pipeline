import dlt
from pyspark.sql.functions import *

@dlt.view(
    name = "passenger_view"
)
def passenger_view():
  
  df = spark.readStream.table("passenger_staging")
  df= df.withColumn("passenger_name", upper(col("passenger_name")))
  return df


dlt.create_streaming_table(
    name = "passenger_silver"
)

dlt.create_auto_cdc_flow(
    target = "passenger_silver",
    source = "passenger_view",
    keys = ["passenger_id"],
    sequence_by = "ingest_ts",
    stored_as_scd_type = "1"
)