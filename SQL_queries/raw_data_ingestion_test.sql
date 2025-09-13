INSERT INTO Passengers VALUES ('P001', 'Rohan Sharma', 29, 'M', 'rohan.sharma@example.com');
INSERT INTO Passengers VALUES ('P002', 'Anjali Verma', 35, 'F', 'anjali.verma@example.com');
INSERT INTO Passengers VALUES ('P003', 'Aarav Singh', 42, 'M', 'aarav.singh@example.com');
INSERT INTO Passengers VALUES ('P004', 'Priya Mehta', 26, 'F', 'priya.mehta@example.com');
INSERT INTO Passengers VALUES ('P005', 'Sahil Khan', 31, 'M', 'sahil.khan@example.com');

----------------------------------------------------------------------------------------------

INSERT INTO Trains VALUES ('12267', 'Mumbai Express', 'Superfast', 'Delhi', 'Mumbai', '08:30:00', '20:45:00');
INSERT INTO Trains VALUES ('12345', 'Rajdhani Express', 'Rajdhani', 'Kolkata', 'Delhi', '16:00:00', '08:00:00');
INSERT INTO Trains VALUES ('12627', 'Karnataka Express', 'Express', 'Bengaluru', 'Delhi', '19:00:00', '12:30:00');
INSERT INTO Trains VALUES ('12951', 'Mumbai Rajdhani', 'Rajdhani', 'Mumbai', 'Delhi', '17:00:00', '07:30:00');

---------------------------------------------------------------------------------------

INSERT INTO Bookings VALUES ('PNR1001', 'P001', '12267', 'S3', 23, 'SL', '2025-08-15 09:30:00');
INSERT INTO Bookings VALUES ('PNR1002', 'P002', '12345', 'B2', 12, '3A', '2025-08-15 10:15:00');
INSERT INTO Bookings VALUES ('PNR1003', 'P003', '12627', 'A1', 3, '2A', '2025-08-15 11:45:00');
INSERT INTO Bookings VALUES ('PNR1004', 'P004', '12951', 'S1', 45, 'SL', '2025-08-16 08:00:00');
INSERT INTO Bookings VALUES ('PNR1005', 'P005', '12267', 'B1', 7, '2A', '2025-08-16 09:00:00');

--------------------------------------------------------------------------------------------------------

-- Passenger Rohan (PNR1001) → multiple attempts, finally success
INSERT INTO Payments VALUES ('TXN9001', 'PNR1001', 'UPI', 'Failed', 600.00, '2025-08-15 09:31:00');
INSERT INTO Payments VALUES ('TXN9002', 'PNR1001', 'UPI', 'Failed', 600.00, '2025-08-15 09:32:00');
INSERT INTO Payments VALUES ('TXN9003', 'PNR1001', 'UPI', 'Success', 600.00, '2025-08-15 09:33:00');

-- Passenger Anjali (PNR1002) → direct success
INSERT INTO Payments VALUES ('TXN9004', 'PNR1002', 'Credit Card', 'Success', 1800.00, '2025-08-15 10:16:00');

-- Passenger Aarav (PNR1003) → failed then success
INSERT INTO Payments VALUES ('TXN9005', 'PNR1003', 'NetBanking', 'Failed', 2500.00, '2025-08-15 11:46:00');
INSERT INTO Payments VALUES ('TXN9006', 'PNR1003', 'NetBanking', 'Success', 2500.00, '2025-08-15 11:47:00');

-- Passenger Priya (PNR1004) → success
INSERT INTO Payments VALUES ('TXN9007', 'PNR1004', 'UPI', 'Success', 750.00, '2025-08-16 08:01:00');

-- Passenger Sahil (PNR1005) → failed attempts, then success
INSERT INTO Payments VALUES ('TXN9008', 'PNR1005', 'Credit Card', 'Failed', 1200.00, '2025-08-16 09:01:00');
INSERT INTO Payments VALUES ('TXN9009', 'PNR1005', 'Credit Card', 'Success', 1200.00, '2025-08-16 09:02:00');

------------------------------------------------------------------------------------------------------------

-- Rohan cancelled (PNR1001)
INSERT INTO Cancellations VALUES ('CXL001', 'PNR1001', '2025-08-15 12:00:00', 450.00);

-- Aarav cancelled (PNR1003)
INSERT INTO Cancellations VALUES ('CXL002', 'PNR1003', '2025-08-15 13:15:00', 1200.00);

-- Sahil cancelled (PNR1005)
INSERT INTO Cancellations VALUES ('CXL003', 'PNR1005', '2025-08-16 10:00:00', 900.00);
