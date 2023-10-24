CREATE OR REPLACE FUNCTION fn_calculate_future_value(
IN initial_sum DECIMAL,
IN yearly_interest_rate DECIMAL,
IN number_of_years INTEGER,
OUT future_value DECIMAL
) AS
$$
	DECLARE
		i INTEGER;
	BEGIN
		future_value := initial_sum;
		FOR i IN 1..number_of_years LOOP
			future_value := future_value + future_value * yearly_interest_rate;
		END LOOP;
		future_value := TRUNC(future_value, 4);
	END;
$$
LANGUAGE plpgsql;


SELECT * FROM fn_calculate_future_value (1000, 0.1, 5);