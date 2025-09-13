import dlt


dlt.create_streaming_table(
    name = "dimPassengers"
)

dlt.create_auto_cdc_flow(
    target = "dimPassengers",
    source = "passenger_view",
    keys = ["passenger_id"],
    sequence_by = "ingest_ts",
    stored_as_scd_type = "2",
    track_history_except_column_list = None,
    track_history_column_list=["passenger_name", "gender", "age", "email"]
)