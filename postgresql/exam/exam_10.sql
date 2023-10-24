CREATE OR REPLACE PROCEDURE sp_players_team_name(
    IN player_name VARCHAR(50),
    OUT player_team VARCHAR(45)
) AS
$$
    BEGIN
        SELECT INTO player_team
            t.name
        FROM
            teams AS t
                JOIN players AS p
                    ON t.id = p.team_id
        WHERE
            CONCAT(p.first_name, ' ', p.last_name) = player_name;

        IF player_team IS NULL THEN
            player_team := 'The player currently has no team';
        END IF;
    END;
$$
LANGUAGE plpgsql;