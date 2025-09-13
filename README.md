
# 🚆 IRCTC Real-Time Data Engineering Pipeline  

This project demonstrates an **end-to-end real-time data engineering pipeline** simulating an **IRCTC railway booking system**. The pipeline ingests streaming data from **Kafka topics** into **Databricks**, processes it through **Bronze → Silver → Gold (Dim & Fact) layers**, and finally builds **KPIs & dashboards** for business insights.  

---

## 📌 Architecture  

```

Kafka Producers → Kafka Topics (Passengers, Bookings, Payments, Cancellations)
↓
Kafka Consumers (Structured Streaming in Databricks)
↓
Raw Source Tables (Landing Zone)
↓
Bronze Layer (Raw Ingested Data)
↓
Silver Layer (Cleansed & Deduplicated Data, SCD Type 1)
↓
Gold Layer (Fact & Dimension Tables)
↓
Materialized Views (KPI Calculations)
↓
Databricks Dashboard (Visualizations)

```

---

## 📂 Project Structure  

```

IRCTC\_End\_To\_End\_Pipeline/
│── kafka\_producer/         # Data generators for 4 Kafka topics
│── kafka\_consumer/         # Consumers writing data into Databricks raw tables
│── raw\_tables/             # Landing zone in Databricks
│── bronze\_layer/           # Bronze ingestion notebooks
│── silver\_layer/           # Transformations, deduplication, SCD1 logic
│── gold\_layer/             # Fact & Dim tables creation (Bookings, Payments, etc.)
│── transformations\_Code/   # Business transformations
│── dashboards/             # Databricks dashboard queries
│── README.md               # Project documentation

````

---

## 🗄️ Data Flow  

### 1. **Kafka Producers (Data Generation)**
- **Passengers Topic** → Passenger profiles (ID, name, age, gender).  
- **Bookings Topic** → Ticket bookings (passenger_id, train_id, date, seats).  
- **Payments Topic** → Payment transactions (payment_id, booking_id, mode, amount, status).  
- **Cancellations Topic** → Ticket cancellations (cancellation_id, booking_id, refund_amount).  

### 2. **Bronze Layer**
- Raw append-only ingestion from Kafka.  
- Minimal transformations, schema applied.  

### 3. **Silver Layer**
- Deduplication, data quality checks.  
- SCD Type 1 for dimension updates.  
- Cleansed, analytics-ready tables.  

### 4. **Gold Layer (Star Schema)**
- **Dimension Tables:**  
  - `DimPassenger`  
  - `DimTrain`  
  - `DimPaymentMethod`  
- **Fact Tables:**  
  - `FactBooking`  
  - `FactPayment`  
  - `FactCancellation`  

### 5. **Materialized Views (KPIs)**
- Aggregated KPI views created on top of Fact tables.  
- Stored as Delta Live Tables for efficiency.  

---

## 📊 KPIs Implemented  

1. **Ticket Sales Daily** → Aggregated from `FactBooking`.  
2. **Revenue by Route** → Join `FactBooking + DimTrain`.  
3. **Cancellation Rate** → Ratio of cancellations vs bookings.  
4. **Payment Method Split** → Revenue distribution by payment mode.  
5. **Train Occupancy Rate** → Booked seats ÷ total seats.  
6. **Top Routes** → Most popular source-destination pairs.  
7. **User Behavior** → Repeat bookings by customers.  
8. **Average Refund % per Route** → Refund vs revenue.  
9. **Payment Retries Trend** → Failed → success payment ratio.  
10. **Revenue Leakage** → Failed payments vs booked seats.  
11. **Customer Loyalty Index** → Repeat bookings & cancellations.  
12. **Monthly Ticket Booking Trend** → Bookings & revenue by month.  

---

## 📈 Dashboard Visualizations  

- **KPI Value Cards:** Cancellation rate, Revenue leakage, Avg Refund %, Occupancy rate.  
- **Bar Charts:** Monthly ticket bookings, Revenue by route, Top routes.  
- **Pie Charts:** Payment mode split, User behavior (new vs repeat customers).  
- **Line Charts:** Payment retries trend, Revenue growth over months.  

---

## 🚀 Tech Stack  

- **Data Ingestion:** Kafka (Producers & Consumers)  
- **Processing & Storage:** Databricks (Delta Lake, Delta Live Tables)  
- **ETL Framework:** Medallion Architecture (Bronze → Silver → Gold)  
- **Streaming Framework:** Spark Structured Streaming  
- **Visualization:** Databricks Dashboards  

---

## 📌 Future Enhancements

* Add **Train Delay Data** for punctuality KPIs.
* Implement **SCD Type 2** for passenger/train history tracking.
* Integrate with **Power BI** for advanced reporting.
* Add **CI/CD with Azure DevOps** for automated deployments.

---

## 👨‍💻 Author

**Nishad Vispute**
Associate Data Engineer | Big Data, PySpark, Kafka, Databricks, Azure
