CREATE OR REPLACE FUNCTION fn_full_name(
    IN first_n VARCHAR(50),
    IN last_n VARCHAR(50),
    OUT full_name VARCHAR(101)) AS
$$
	BEGIN
		first_n := INITCAP(first_n);
		last_n := INITCAP(last_n);
		IF first_n IS NULL AND last_n IS NULL THEN
			full_name := NULL;
		ELSIF first_n IS NULL THEN
			full_name := last_n;
		ELSIF last_n IS NULL THEN
			full_name := first_n;
		ELSE
			SELECT INTO full_name
			CONCAT(first_n, ' ', last_n);
		END IF;
	END;
$$
LANGUAGE plpgsql;

SELECT * FROM fn_full_name('', 'SIMPSONS');
SELECT * FROM fn_full_name(NULL, NULL);