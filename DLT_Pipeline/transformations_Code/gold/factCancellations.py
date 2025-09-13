import dlt
from pyspark.sql.functions import *
from pyspark.sql.window import Window

@dlt.table(
    name="factCancellation"
)
def factCancellations():
    cancel_df = dlt.read("cancellation_silver")
    bookings_df = dlt.read("booking_silver")

    # Keep only valid cancellations linked to bookings
    cancel_valid = cancel_df.join(
        bookings_df.select("pnr"),
        "pnr",
        "inner"
    )

    fact_df = cancel_valid.select(
        col("cancellation_id"),
        col("pnr"),
        col("cancellation_time"),
        col("refund_amount")
    )

    return fact_df
