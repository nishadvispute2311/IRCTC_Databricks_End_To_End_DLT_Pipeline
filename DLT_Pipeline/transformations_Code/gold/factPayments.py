import dlt
from pyspark.sql.functions import *
from pyspark.sql.window import Window


@dlt.table(
    name = "factPayments"
)
def factPayments():
    pay_df = spark.read.table("payment_silver")
    book_df = spark.read.table("booking_silver")

    valid_payments = pay_df.join(book_df.select("pnr"),"pnr","inner")
    final_df = valid_payments.select(
        col("transaction_id"),
        col("pnr"),
        col("mode"),
        col("status"),
        col("amount"),
        col("payment_time")
    )
    return final_df
