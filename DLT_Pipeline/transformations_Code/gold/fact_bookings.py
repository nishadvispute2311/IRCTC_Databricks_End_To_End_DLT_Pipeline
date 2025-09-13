import dlt
from pyspark.sql.functions import *
from pyspark.sql.window import Window

@dlt.table(
    name="factBookings"
)
def factBookings():
    bookings_df = dlt.read("booking_silver")

    fact_df = bookings_df.select(
        col("pnr"),
        col("passenger_id"),
        col("train_no"),
        col("coach"),
        col("seat_no"),
        col("class"),
        col("booking_time"),
        to_date("booking_time").alias("booking_date")
    )

    return fact_df
