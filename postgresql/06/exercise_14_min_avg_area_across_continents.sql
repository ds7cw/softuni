SELECT
	MIN("avg") AS min_average_area
FROM
	(
	SELECT
		AVG(area_in_sq_km)
	FROM
		countries
	GROUP BY
		continent_code) AS avg_area;