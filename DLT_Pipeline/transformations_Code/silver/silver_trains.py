import dlt
from pyspark.sql.functions import *

@dlt.view(
    name = "train_view"
)
def train_view():
  
  df = spark.readStream.table("trains_data")
  return df


dlt.create_streaming_table(
    name = "train_silver"
)

dlt.create_auto_cdc_flow(
    target = "train_silver",
    source = "train_view",
    keys = ["train_no"],
    sequence_by = "ingest_ts",
    stored_as_scd_type = "1"
)