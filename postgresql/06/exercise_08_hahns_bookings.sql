-- Solution #1

SELECT
	COUNT(*) AS "count"
FROM (SELECT
	  	*
	  FROM
	  	customers
	  WHERE
	  last_name = 'Hahn') AS "asd";

-- Solution #2

SELECT
	COUNT(*)
FROM
	customers as c
		JOIN bookings AS b
			USING(customer_id)
WHERE
	c.last_name = 'Hahn';