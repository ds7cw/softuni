SELECT
	user_id,
	AGE(starts_at, booke_at) AS "Early Birds"
FROM
	bookings
WHERE
	AGE(starts_at, booked_at) >= INTERVAL '10 Months';



-- Second Method
SELECT
	user_id,
	AGE(starts_at, booked_at) AS "Early Birds"
FROM
	bookings
WHERE
	starts_at - booked_at >= '10 MONTHS';