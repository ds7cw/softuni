-- CREATE DATABASE soft_uni

-- Solution using DECLARE
CREATE FUNCTION fn_count_employees_by_town(VARCHAR)
RETURNS INT AS

$$
	DECLARE
		town ALIAS FOR $1;
	BEGIN
		RETURN(SELECT
					COUNT(*)
				FROM
					employees AS e
						JOIN addresses AS a
							USING(address_id)
								JOIN towns AS t
									USING(town_id)
				WHERE
					t.name = town);
	END
$$
LANGUAGE plpgsql;

SELECT fn_count_employees_by_town('Sofia');


-- Solution without DECLARE
CREATE FUNCTION fn_count_employees_by_town(town VARCHAR)
RETURNS INT AS

$$
	BEGIN
		RETURN(SELECT
					COUNT(*)
				FROM
					employees AS e
						JOIN addresses AS a
							USING(address_id)
								JOIN towns AS t
									USING(town_id)
				WHERE
					t.name = town);
	END;
$$
LANGUAGE plpgsql;

SELECT fn_count_employees_by_town('Sofia');
