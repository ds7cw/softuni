UPDATE coaches
SET salary = salary * coach_level
WHERE first_name LIKE 'C%'
AND id IN (
    SELECT coach_id
    FROM players_coaches
    WHERE coach_id IN (
        SELECT coach_id
        FROM players_coaches
        GROUP BY coach_id
        HAVING COUNT(player_id) > 0
    )
);





-- Alternative Selection Query using Join
SELECT
    c.first_name,
    c.last_name,
    COUNT(pc.coach_id)
FROM coaches AS c
    JOIN players_coaches AS pc
        ON c.id = pc.coach_id
WHERE
    c.first_name LIKE 'C%'
GROUP BY
    c.id;