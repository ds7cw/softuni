SELECT
	(SELECT COUNT(*) FROM employees WHERE department_id = 1) AS "Engineering",
	(SELECT COUNT(*) FROM employees WHERE department_id = 2) AS "Tool Design",
	(SELECT COUNT(*) FROM employees WHERE department_id = 3) AS "Sales",
	(SELECT COUNT(*) FROM employees WHERE department_id = 4) AS "Marketing",
	(SELECT COUNT(*) FROM employees WHERE department_id = 5) AS "Purchasing",
	(SELECT COUNT(*) FROM employees WHERE department_id = 6) AS "Research and Development",
	(SELECT COUNT(*) FROM employees WHERE department_id = 7) AS "Production"



	-- Alternative Solution Using JOIN, Result in Rows though, Not Columns
SELECT
	d.department_name,
	COUNT(d.id)
FROM
	employees AS e
JOIN
	departments AS d
ON
	d.id = e.department_id
GROUP BY
	d.id;