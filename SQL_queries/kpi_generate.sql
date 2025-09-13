-- Total_tickets_sales_daily
SELECT 
    booking_date,
    COUNT(*) AS total_tickets
FROM factbookings
GROUP BY booking_date
ORDER BY booking_date;

-- cancellation_rate
SELECT 
    booking_date,
    COUNT(c.pnr) * 100.0 / COUNT(b.pnr) AS cancellation_rate
FROM factBookings b
LEFT JOIN factCancellation c ON b.pnr = c.pnr
GROUP BY booking_date
ORDER BY booking_date;

-- repeat_customer_rate
SELECT 
    COUNT(DISTINCT passenger_id) AS total_customers,
    COUNT(DISTINCT CASE WHEN cnt > 1 THEN passenger_id END) AS repeat_customers,
    (COUNT(DISTINCT CASE WHEN cnt > 1 THEN passenger_id END) * 100.0 / COUNT(DISTINCT passenger_id)) AS repeat_customer_percent
FROM (
    SELECT passenger_id, COUNT(*) AS cnt
    FROM FactBookingS
    GROUP BY passenger_id
);


-- total_revenue
select sum(amount) from factpayments


-- avg refund per route
SELECT 
    CONCAT(t.source, '-', t.destination) AS route,
    (SUM(c.refund_amount) * 100.0 / SUM(F.amount)) AS avg_refund_percent
FROM factcancellation c
JOIN factbookings b ON c.pnr = b.pnr
JOIN train_silver t ON b.train_no = t.train_no
JOIN FACTPAYMENTS F ON b.pnr = F.pnr
GROUP BY t.source, t.destination;


-- revenue per mode
select mode as payment_mode, sum(amount) as total_revenue from factPayments where status = "Success" group by mode


-- tickets sold per train type
SELECT train_type, COUNT(*) as total_count FROM train_silver t JOIN factbookings b ON t.train_no = b.train_no GROUP BY train_type


-- top 5 routes by bookings
select * from top_routes limit 5


-- monthly ticket booking trend
SELECT 
    DATE_FORMAT(booking_date, 'yyyy-MM') AS booking_month,
    SUM(p.amount) AS total_revenue
FROM factbookings b
JOIN factpayments P ON b.pnr = p.pnr
GROUP BY DATE_FORMAT(booking_date, 'yyyy-MM')
ORDER BY booking_month;
