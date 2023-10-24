SELECT
	"name" AS "volunteers",
	phone_number,
	REPLACE(REPLACE(REPLACE("address", ' S', 'S'), 'Sofia ', 'Sofia'), 'Sofia, ', '') AS "address"
FROM
	volunteers
WHERE
	department_id = (SELECT "id"
					FROM volunteers_departments
					WHERE department_name = 'Education program assistant')
	AND
	"address" LIKE '%Sofia%'
ORDER BY
	"name" ASC;