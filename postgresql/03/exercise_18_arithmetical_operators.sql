CREATE TABLE IF NOT EXISTS
	bookings_calculation AS
SELECT
	booked_for
FROM
	bookings
WHERE
	apartment_id = 93;


ALTER TABLE
	bookings_calculation
ADD COLUMN
	multiplication NUMERIC,
ADD COLUMN
	modulo NUMERIC;

UPDATE
	bookings_calculation
SET
	multiplication = booked_for * 50,
	modulo =MOD(booked_for, 50);



-- Second Method
CREATE TABLE
	bookings_calculation
AS SELECT
	booked_for,
	CAST(booked_for * 50 AS NUMERIC) AS multiplication,
	CAST(booked_for % 50 AS NUMERIC) AS modulo
FROM
	bookings
WHERE
	apartment_id = 93;



-- Third Method
CREATE TABLE IF NOT EXISTS
	bookings_calculation AS
SELECT
	booked_for,
	(booked_for * 50)::"numeric" AS multiplication,
	(mod(booked_for, 50))::"numeric" AS modulo
FROM bookings
WHERE
	apartment_id = 93;
select * from bookings_calculation