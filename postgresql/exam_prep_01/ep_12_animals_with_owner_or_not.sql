CREATE OR REPLACE PROCEDURE sp_animals_with_owners_or_not(
	IN animal_name VARCHAR(30),
	OUT owner_name VARCHAR(50)
) AS
$$	
	BEGIN
		SELECT INTO owner_name
			o.name
		FROM
			animals AS a
				LEFT JOIN owners AS o
					ON a.owner_id = o.id
		WHERE
			a.name = animal_name;
		
		IF owner_name IS NULL THEN
			owner_name := 'For adoption';
		END IF;
	END;
$$
LANGUAGE plpgsql;