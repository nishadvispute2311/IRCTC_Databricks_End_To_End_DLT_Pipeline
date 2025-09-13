import dlt

booking_rules = {
    "rule1" : "pnr is not null"
}

@dlt.table(
    name = "booking_staging"
)
@dlt.expect_all_or_drop(booking_rules)
def booking_staging():
    df = spark.readStream.table("irctc_catalog.raw_data.Bookings")
    return df