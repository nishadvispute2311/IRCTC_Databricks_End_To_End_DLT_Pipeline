import dlt
from pyspark.sql.functions import *
from pyspark.sql.window import Window


@dlt.table(
    name = "payment_silver"
)
def payment_silver():
    raw_df = spark.read.table("payments_staging")
    
    w = Window.partitionBy("pnr").orderBy(
        when(col("status") == "Success", 1).otherwise(2),
        col("payment_time").desc()
    )
    updated_df = raw_df.withColumn("rn",row_number().over(w)).filter(col("rn")==1).withColumn("mode",upper(col("mode"))).drop("rn")

    return updated_df
    