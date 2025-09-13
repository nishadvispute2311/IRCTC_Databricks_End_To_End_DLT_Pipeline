from kafka import KafkaConsumer
import json
import os

# List of topics to consume
topics = ['yn-passenger_details-0812', 'yn-booking_details-0812', 'yn-cancellation_details-0812', 'yn-payment_details-0812']

# Output folder for CSVs
output_dir = 'csv_consumed_data_kafka'
os.makedirs(output_dir, exist_ok=True)

# Create Kafka Consumer
consumer = KafkaConsumer(
    *topics,
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='yn_sales_multi_topic_consumer_group_v1',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

# Track which files have had headers written
written_headers = {}

# Open file handles per topic
file_handles = {}

for message in consumer:
    topic = message.topic
    data = message.value
    print(f"[{topic}] Consumed: {data}")

    # CSV file path
    csv_file = os.path.join(output_dir, f"{topic}_data.csv")

    # Open file handle if not already
    if topic not in file_handles:
        f = open(csv_file, 'a', buffering=1)  # line-buffered
        file_handles[topic] = f

        # Write header if file is new
        if not os.path.exists(csv_file) or topic not in written_headers:
            header_line = ",".join(data.keys())
            f.write(header_line + "\n")
            written_headers[topic] = True

    # Write data line
    data_line = ",".join(str(data.get(key, "")) for key in data.keys())
    file_handles[topic].write(data_line + "\n")
    file_handles[topic].flush()  # Flush after each write