SELECT
    bg.name,
    bg.rating,
    cat.name AS category_name
FROM board_games AS bg
    JOIN players_ranges AS pr
        ON bg.players_range_id = pr.id
            JOIN categories AS cat
                ON bg.category_id = cat.id
WHERE rating > 7
    AND ((bg.name LIKE '%a%' OR (bg.name LIKE '%A%')) OR (bg.rating > 7.5))
    AND (((pr.min_players BETWEEN 2 AND 5) AND (pr.max_players BETWEEN 2 AND 5)))
ORDER BY
    bg.name ASC,
    bg.rating DESC
LIMIT
    5;