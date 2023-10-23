WITH row_number AS ( 
    SELECT
        country_name,
        peak_name,
        elevation,
        mountain_range,
        ROW_NUMBER() OVER (PARTITION BY country_name ORDER BY elevation DESC) AS rn
            FROM countries AS c
                LEFT JOIN mountains_countries AS mc
                    USING(country_code)
                       LEFT JOIN mountains AS m
                            ON m.id = mc.mountain_id
                                LEFT JOIN peaks AS p
                                    USING(mountain_id) )
SELECT
	row_number.country_name,
	COALESCE(row_number.peak_name, '(no highest peak)') AS peak_name,
    COALESCE(row_number.elevation, 0) AS elevation,
    CASE
        WHEN row_number.peak_name IS NOT NULL THEN row_number.mountain_range
        ELSE '(no mountain)'
        END AS mountain_range

FROM
    row_number
WHERE
    row_number.rn = 1
ORDER BY
    row_number.country_name,
    row_number.elevation DESC;