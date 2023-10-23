SELECT
	b.booking_id AS "Booking ID",
	a.name AS "Apartment Owner",
	a.apartment_id AS "Apartment ID",
	CONCAT(c.first_name, ' ', last_name) AS "Customer Name"
FROM
	bookings AS b
		FULL JOIN apartments AS a
			USING(booking_id)
				FULL JOIN customers as c
					USING(customer_id)
ORDER BY
	"Booking ID",
	"Apartment Owner",
	"Customer Name";