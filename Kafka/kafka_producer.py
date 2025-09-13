import uuid
import json
import random
import time
from faker import Faker
from datetime import datetime, timedelta
from confluent_kafka import Producer

fake = Faker()

# Kafka configuration
producer = Producer({'bootstrap.servers': 'localhost:9092'})

# Pre-generated static datasets
NUM_PASSENGERS = random.randint(1,10)


TOPICS = {
    "passengers": "yn-passenger_details-0812",
    "bookings": "yn-booking_details-0812",
    "cancellations": "yn-cancellation_details-0812",
    "payments": "yn-payment_details-0812"
}

bookings_store = []
payment_details = []
train_details = [
    {"Train_No": "12267", "Train_Name": "Mumbai Express", "Class": "SL"},
    {"Train_No": "12345", "Train_Name": "Rajdhani Express", "Class": "3A"},
    {"Train_No": "12627", "Train_Name": "Karnataka Express", "Class": "2A"},
    {"Train_No": "12650", "Train_Name": "Sampark Kranti Express", "Class": "SL"},
    {"Train_No": "12009", "Train_Name": "Shatabdi Express", "Class": "CC"},
    {"Train_No": "12951", "Train_Name": "Mumbai Rajdhani", "Class": "1A"},
    {"Train_No": "12245", "Train_Name": "Duronto Express", "Class": "2A"},
    {"Train_No": "12622", "Train_Name": "Tamil Nadu Express", "Class": "SL"},
    {"Train_No": "12802", "Train_Name": "Purushottam Express", "Class": "3A"},
    {"Train_No": "12137", "Train_Name": "Punjab Mail", "Class": "SL"},
    {"Train_No": "12688", "Train_Name": "Bangalore Express", "Class": "2A"},
    {"Train_No": "12423", "Train_Name": "Rajdhani Special", "Class": "3A"},
]


def passengers_generate():
    passengers_data = []
    for i in range(NUM_PASSENGERS):
        gender = random.choice(['male', 'female'])
        if gender == "male":
            name = fake.name_male()
        else:
            name = fake.name_female()
        c_data = {
            "passenger_id": f"P_{random.randint(100000,99999999)}",
            "name": name,
            "gender": gender,
            "email": f"{name.split()[0].lower()}{name.split()[1].lower()}@email.com",
            "phone": fake.phone_number(),
            "signup_date": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),
            "location": fake.city()
        }
        passengers_data.append(c_data)
    return passengers_data

passenger_details = passengers_generate()

def booking_event():
    if not passenger_details:
        return None
    passenger = random.choice(passenger_details)
    train = random.choice(train_details)
    booking = {
        "PNR": f"{random.randint(1000000000, 9999999999)}",
        "passenger_id": passenger["passenger_id"],
        "Train_No": train["Train_No"],
        "Train_Name": train["Train_Name"],
        "Coach": random.choice(["S1", "S2", "B1", "B2","A1","A2"]),
        "Seat_No": random.randint(1, 72),
        "Class": train["Class"],
        "Booking_Time": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    bookings_store.append(booking)
    return booking


def payment_event():
    if not bookings_store:
        return None
    booking_data = random.choice(bookings_store)
    payment_data = {
        "Transaction_ID": f"TXN{random.randint(100000,999999)}",
        "PNR": booking_data["PNR"],
        "Mode": random.choice(["UPI", "Credit Card", "NetBanking", "Debit Card"]),
        "Status": random.choice(["Success", "Failed"]),
        "Amount": round(random.uniform(500, 3000), 2),
        "Payment_Time": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    payment_details.append(payment_data)
    return payment_data


def cancellation_event():
    if not payment_details:
        return None
    payment_txn_data = random.choice(payment_details)
    if payment_txn_data["Status"] == "Success":
        cancellation_data = {
            "PNR": payment_txn_data["PNR"],
            "Transaction_ID": payment_txn_data["Transaction_ID"],
            "Cancellation_Time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "Refund_Amount": round(random.uniform(300, 2000), 2)
        }
    else:
        cancellation_data = {}
    return cancellation_data




def produce(topic, key, value):
    producer.produce(topic, key=key, value=json.dumps(value))
    producer.poll(0)

def flush_all():
    producer.flush()

def stream_static_data():
    for p in passenger_details:
        produce(TOPICS["passengers"], p["passenger_id"], p)
        pass
    flush_all()
    print(f"Static data streamed to {TOPICS['passengers']} topic.")


if __name__ == "__main__":
    stream_static_data()
    events = [("bookings", booking_event),
              ("cancellations", cancellation_event),
              ("payments", payment_event)]

    print("Starting Kafka Streaming Producer...")

    while True:
        # Pick a random event type
        topic_key, generator = random.choice(events)
        event = generator()
        if event:
            producer.send(TOPICS[topic_key], event)
            print(f"Produced {topic_key}: {event}")
        
        producer.flush()
        # Random interval between 1-5 seconds
        time.sleep(random.randint(1,3))