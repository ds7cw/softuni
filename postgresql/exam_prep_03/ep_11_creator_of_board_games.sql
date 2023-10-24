CREATE OR REPLACE FUNCTION
    fn_creator_with_board_games(
        IN creator_first_name VARCHAR(30),
        OUT total_number_of_games INT
) AS
$$
    BEGIN
        SELECT INTO total_number_of_games
            COUNT(*)
            FROM creators AS c
                JOIN creators_board_games AS cbg
                    ON c.id = cbg.creator_id
                        JOIN board_games AS bg
                            ON cbg.board_game_id = bg.id
        WHERE
            C.first_name = creator_first_name;
        IF total_number_of_games IS NULL THEN
            total_number_of_games := 0;
        END IF;
    END;
$$
LANGUAGE plpgsql;


SELECT fn_creator_with_board_games('Bruno');
SELECT fn_creator_with_board_games('Alexander');