-- Passengers Table
DROP TABLE Passengers;
CREATE TABLE Passengers (
    passenger_id VARCHAR(20) PRIMARY KEY,
    passenger_name VARCHAR(100),
    age INT,
    gender CHAR(1),
    email VARCHAR(100)
);

----------------------------------------------------------------------------------------------
-- Trains Table
CREATE TABLE Trains (
    train_no VARCHAR(10) PRIMARY KEY,
    train_name VARCHAR(100),
    train_type VARCHAR(50),
    source VARCHAR(50),
    destination VARCHAR(50),
    departure_time STRING,
    arrival_time STRING
);

---------------------------------------------------------------------------------------
-- Bookings Table
CREATE TABLE Bookings (
    pnr VARCHAR(15) PRIMARY KEY,
    passenger_id VARCHAR(20),
    train_no VARCHAR(10),
    coach VARCHAR(5),
    seat_no INT,
    class VARCHAR(5),
    booking_time TIMESTAMP,
    FOREIGN KEY (passenger_id) REFERENCES Passengers(passenger_id),
    FOREIGN KEY (train_no) REFERENCES Trains(train_no)
);

--------------------------------------------------------------------------------------------------------

-- Payments Table
CREATE TABLE Payments (
    transaction_id VARCHAR(20) PRIMARY KEY,
    pnr VARCHAR(15),
    mode VARCHAR(20),
    status VARCHAR(20),
    amount DECIMAL(10,2),
    payment_time TIMESTAMP,
    FOREIGN KEY (pnr) REFERENCES Bookings(pnr)
);

------------------------------------------------------------------------------------------------------------

-- Cancellations Table
CREATE TABLE Cancellations (
    cancellation_id VARCHAR(20) PRIMARY KEY,
    pnr VARCHAR(15),
    cancellation_time TIMESTAMP,
    refund_amount DECIMAL(10,2),
    FOREIGN KEY (pnr) REFERENCES Bookings(pnr)
);
