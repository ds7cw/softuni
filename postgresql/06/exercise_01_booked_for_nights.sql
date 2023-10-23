-- CREATE DATABASE subqueries_joins_booking_db;

SELECT
	CONCAT(a.address, ' ', a.address_2) AS "Apartment Address",
	b.booked_for AS "Nights"
FROM
	apartments AS a
		JOIN bookings AS b
			USING(booking_id)
ORDER BY
	a.apartment_id ASC;