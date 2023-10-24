CREATE OR REPLACE PROCEDURE sp_increase_salary_by_id("id" INT)
AS
$$
	DECLARE
		emp_salary NUMERIC;
	BEGIN
		SELECT INTO emp_salary
			salary
		FROM
			employees
		WHERE
			employee_id = "id";
		
		IF emp_salary IS NULL THEN
			ROLLBACK;
			RETURN;
		END IF;
		
		UPDATE employees
		SET salary = salary * 1.05
		WHERE employee_id = "id";
		COMMIT;
		RETURN;
	
	END;
$$
LANGUAGE plpgsql;

SELECT salary FROM employees WHERE employee_id = 17;
-- salary for employee_id 17 is 13500

CALL sp_increase_salary_by_id(17);

SELECT salary FROM employees WHERE employee_id = 17;
-- salary for employee_id 17 is now 14175