SELECT
	CONCAT(m.mountain_range, ' ', p.peak_name) AS "Mountain Information",
	CHAR_LENGTH(CONCAT(m.mountain_range, ' ', p.peak_name)) AS "Characters Length",
	BIT_LENGTH(CONCAT(m.mountain_range, ' ', p.peak_name)) AS "Bits of a String"
FROM
	mountains as m,
	peaks as p
WHERE
    p.mountain_id = m.id;