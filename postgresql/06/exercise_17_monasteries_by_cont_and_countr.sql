UPDATE
	countries
SET
	country_name = 'Burma'
WHERE
	country_name = 'Myanmar';
	
INSERT INTO
	monasteries(monastery_name, country_code)
VALUES
	('Hanga Abbey', (SELECT country_code FROM countries WHERE country_name = 'Tanzania'));
-- ('Myin-Tin-Daik', 'MM') Judge does not accept this line, Softuni need to fix the instructions

SELECT
	con.continent_name AS "Continent Name",
	c.country_name AS "Country Name",
	COUNT(m.id) AS "Monasteries Count"
FROM
	countries AS c
		LEFT JOIN continents AS con
			USING(continent_code)
				LEFT JOIN monasteries AS m
					USING(country_code)
WHERE
	c.three_rivers IS FALSE
GROUP BY
	c.country_name,
	con.continent_name
ORDER BY
	"Monasteries Count" DESC,
	c.country_name;