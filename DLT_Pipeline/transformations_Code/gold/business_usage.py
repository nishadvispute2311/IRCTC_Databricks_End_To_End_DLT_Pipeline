import dlt 
from pyspark.sql.functions import * 
from pyspark.sql.window import Window 

@dlt.table(
    name = "ticket_sales_daily"
)
def ticket_sales_daily():
    factBooking = spark.read.table("factBookings") 
    final_kpi = factBooking.withColumn("booking_date", to_date("booking_time")).groupBy("booking_date").agg(count("*").alias("total_sold_tickets")) 
    return final_kpi


@dlt.table(
    name = "revenue_by_route"
)
def revenue_by_route():
    train_df = spark.read.table("train_silver")
    booking_df = spark.read.table("factBookings")
    payment_df = spark.read.table("factPayments")
    combine_df = booking_df.join(payment_df, (booking_df.pnr == payment_df.pnr) & (payment_df.status == "Success")).join(train_df,booking_df.train_no==train_df.train_no).groupBy(train_df.source, train_df.destination, train_df.train_type).agg(sum(col("amount")).alias("total_revenue")) 
    return combine_df

@dlt.table(
    name = "cancellation_rate"
)
def cancellation_rate():
    booking_df = spark.read.table("factBookings")
    cancel_df = spark.read.table("factCancellation")

    final_df = booking_df.join(cancel_df, booking_df.pnr == cancel_df.pnr).withColumn("booking_date",to_date("booking_time")).groupBy("booking_date").agg((count(cancel_df.pnr) / count(booking_df.pnr)).alias("cancel_rate"))

    return final_df

@dlt.table(
    name = "top_routes"
)
def top_routes():
    train_df = spark.read.table("train_silver")
    booking_df = spark.read.table("factBookings")

    join_df = booking_df.join(train_df,booking_df.train_no == train_df.train_no).groupBy(train_df.source,train_df.destination).agg(count("*").alias("total_bookings")).orderBy(desc("total_bookings")).limit(10)

    return join_df

@dlt.table(
    name = "payment_method_split"
)
def payment_method_split():
    payment_df = spark.read.table("factPayments")

    final_df = payment_df.filter(col("status") == "Success").withColumn("payment_date",to_date("payment_time")).groupBy("payment_date","mode").agg(
        count("*").alias("txn_count"),
        sum("amount").alias("total_amount")
    )
    return final_df