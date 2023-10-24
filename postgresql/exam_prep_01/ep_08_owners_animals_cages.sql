SELECT
	CONCAT(o.name, ' - ', a.name) AS "Owners - Animals",
	o.phone_number AS "Phone Number",
	ac.cage_id AS "Cage ID"
FROM
	animals AS a
		JOIN owners AS o
			ON a.owner_id = o.id
				JOIN animals_cages AS ac
					ON a.id = ac.animal_id
WHERE
	a.animal_type_id = (SELECT "id"
						FROM animal_types
						WHERE animal_type = 'Mammals')
ORDER BY
	o.name ASC,
	a.name DESC;