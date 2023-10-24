CREATE OR REPLACE FUNCTION fn_difficulty_level(
	IN "level" INT
	) RETURNS VARCHAR(50) AS
$$
	BEGIN
		IF "level" <= 40 THEN
			RETURN 'Normal Difficulty';
		ELSIF "level" <= 60 THEN
			RETURN 'Nightmare Difficulty';
		ELSE
			RETURN 'Hell Difficulty';
		END IF;
	
	END;
$$
LANGUAGE plpgsql;


SELECT
	user_id,
	"level",
	cash,
	(SELECT * FROM fn_difficulty_level(user_id)) AS difficulty_level
FROM
	users_games
ORDER BY
	user_id;