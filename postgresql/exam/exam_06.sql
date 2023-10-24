SELECT
    p.id,
    CONCAT(first_name, ' ', last_name) AS full_name,
    p.age,
    p.position,
    p.salary,
    sd.pace,
    sd.shooting
FROM players AS p
    JOIN skills_data AS sd
        ON P.skills_data_id = sd.id
WHERE
    p.position = 'A'
    AND
    (sd.pace + sd.shooting) > 130
    AND
    p.team_id IS NULL;