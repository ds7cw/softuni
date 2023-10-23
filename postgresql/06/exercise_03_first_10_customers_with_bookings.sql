SELECT
	b.booking_id AS "Booking ID",
	b.starts_at::DATE AS "Start Date",
	b.apartment_id AS "Apartment ID",
	CONCAT(c.first_name, ' ', c.last_name) AS "Customer Name"
FROM
	bookings AS b
		RIGHT JOIN customers AS c
			USING(customer_id)
ORDER BY
	"Customer Name" ASC
LIMIT
	10;