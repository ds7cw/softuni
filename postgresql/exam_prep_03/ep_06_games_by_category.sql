SELECT
    board_games.id,
    board_games.name,
    release_year,
    categories.name AS category_name
FROM board_games
    JOIN categories
        ON board_games.category_id = categories.id
WHERE
    categories.name IN ('Strategy Games', 'Wargames')
ORDER BY
    release_year DESC;