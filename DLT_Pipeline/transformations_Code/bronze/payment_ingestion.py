import dlt

payment_rules = {
    "rule1" : "transaction_id is not null"
}

@dlt.table(
    name = "payments_staging"
)
@dlt.expect_all_or_drop(payment_rules)
def payments_staging():
    df = spark.readStream.table("irctc_catalog.raw_data.Payments")
    return df