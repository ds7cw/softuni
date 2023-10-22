SELECT
	population,
	LENGTH(population::"text") as "length"
FROM
	countries;


-- Second Method
SELECT
	population,
	LENGTH(CAST(population AS VARCHAR)) AS "length"
FROM
	countries;