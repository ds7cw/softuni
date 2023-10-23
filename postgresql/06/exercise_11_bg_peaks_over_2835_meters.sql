-- CREATE DATABASE subqueries_joins_geography_db;

SELECT
	country_code,
	mountain_range,
	peak_name,
	elevation
FROM
	mountains_countries AS mc
		JOIN mountains AS m
			ON mc.mountain_id = m.id
				JOIN peaks AS p
					ON p.mountain_id = m.id
WHERE
	p.elevation > 2835
		AND
	mc.country_code = 'BG'
ORDER BY
	p.elevation DESC;