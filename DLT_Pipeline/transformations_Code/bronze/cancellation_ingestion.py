import dlt

cancellation_rules = {
    "rule1" : "cancellation_id is not null"
}

@dlt.table(
    name = "cancellation_staging"
)
@dlt.expect_all_or_drop(cancellation_rules)
def cancellation_staging():
    df = spark.readStream.table("irctc_catalog.raw_data.Cancellations")
    return df