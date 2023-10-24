CREATE OR REPLACE FUNCTION fn_cash_in_users_games(
	game_name VARCHAR(50)
) RETURNS TABLE (total_cash NUMERIC) AS
$$
	BEGIN
		RETURN QUERY
			SELECT
				TRUNC(SUM(cash), 2)
			FROM (
				SELECT
					ug.user_id,
					ug.game_id,
					g.name,
					ug.cash,
					(ROW_NUMBER() OVER (ORDER BY ug.cash DESC)) AS "row_no"
				FROM users_games AS ug
					JOIN games AS g
						ON ug.game_id = g.id
				WHERE g.name = game_name
				) AS subquery WHERE MOD("row_no", 2) = 1;
	END;
$$
LANGUAGE plpgsql;

SELECT * FROM fn_cash_in_users_games('Love in a mist');
SELECT * FROM fn_cash_in_users_games('Delphinium Pacific Giant');
