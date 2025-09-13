import dlt
from pyspark.sql.functions import *
from pyspark.sql.window import Window

@dlt.table(
    name = "booking_silver"
)
def booking_silver():
    raw_df = spark.read.table("booking_staging")

    w = Window.partitionBy("pnr").orderBy(col("booking_time").desc())
    updated_df = raw_df.withColumn("rn",row_number().over(w)).filter(col("rn") == 1).drop("rn")

    class_map = {
        "SL": "Sleeper",
        "2A": "AC 2-Tier",
        "3A": "AC 3-Tier",
        "1A": "AC First Class",
        "CC": "Chair Car"
    }
    bookings_norm = updated_df.replace(class_map, subset=["class"])

    return bookings_norm