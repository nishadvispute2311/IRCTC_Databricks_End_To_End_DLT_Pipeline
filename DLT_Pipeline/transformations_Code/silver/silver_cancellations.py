import dlt
from pyspark.sql.functions import *
from pyspark.sql.window import Window


@dlt.table(
    name = "cancellation_silver"
)
def cancellation_silver():
    raw_df = spark.read.table("cancellation_staging")

    w = Window.partitionBy("pnr").orderBy(col("cancellation_time").desc())
    updated_df = raw_df.withColumn("rn", row_number().over(w)).filter(col("rn") == 1).drop("rn")

    return updated_df