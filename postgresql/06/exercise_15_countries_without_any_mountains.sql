-- Solution #1

SELECT
	COUNT(*) AS countries_without_mountains
FROM
	(
	SELECT
		c.country_name,
		m.mountain_range
	FROM
		countries AS c
			LEFT JOIN mountains_countries AS mc
				USING(country_code)
					LEFT JOIN mountains AS m
						ON mc.mountain_id = m.id
	) AS all_countries
WHERE 
	all_countries.mountain_range IS NULL;


-- Solution #2

SELECT
	COUNT(*) AS countries_without_mountains
FROM 
	countries AS c
LEFT JOIN 
	mountains_countries AS mc
USING 
	(country_code)
WHERE
	mc.mountain_id IS NULL;