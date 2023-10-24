SELECT
    a.name AS "animal",
    EXTRACT(YEAR FROM a.birthdate::DATE) AS birth_year,
    at.animal_type
FROM
	animals AS a
        JOIN animal_types AS at
            ON a.animal_type_id = at.id
WHERE
	a.owner_id IS NULL
	AND
	at.animal_type <> 'Birds'
	AND
	EXTRACT(YEAR FROM AGE('01/01/2022'::DATE, a.birthdate)) < 5
ORDER BY
	"animal" ASC;