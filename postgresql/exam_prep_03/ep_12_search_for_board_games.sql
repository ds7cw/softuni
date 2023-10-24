CREATE TABLE search_results (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    release_year INT,
    rating FLOAT,
    category_name VARCHAR(50),
    publisher_name VARCHAR(50),
    min_players VARCHAR(50),
    max_players VARCHAR(50)
);


CREATE OR REPLACE PROCEDURE usp_search_by_category(
    IN category VARCHAR(50)
) AS
$$
    BEGIN
        INSERT INTO search_results("name", release_year, rating, category_name,
                                   publisher_name, min_players, max_players)
        SELECT
            b.name,
            b.release_year,
            b.rating,
            cat.name AS category_name,
            p.name AS publisher_name,
            CONCAT(pr.min_players::CHAR, ' people') AS min_players,
            CONCAT(pr.max_players::CHAR, ' people') AS max_players
        FROM board_games AS b
            JOIN publishers AS p
                ON b.publisher_id = p.id
            JOIN creators_board_games AS cbg
                ON b.id = cbg.board_game_id
            JOIN creators AS c
                ON cbg.creator_id = c.id
            JOIN players_ranges AS pr
                ON b.players_range_id = pr.id
            JOIN categories AS cat
                ON b.category_id = cat.id
        WHERE
            cat.name = 'Wargames'
        GROUP BY
            b.name,
            p.name,
            b.release_year,
            pr.min_players,
            pr.max_players,
            b.rating,
            cat.name
        ORDER BY
            p.name ASC,
            b.release_year DESC;
    END;
$$
LANGUAGE plpgsql;


CALL usp_search_by_category_2('Wargames');

SELECT * FROM search_results;