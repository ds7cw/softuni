UPDATE
	employees
SET
	salary = (CASE
				WHEN hire_date < '2015-01-16'::DATE THEN salary + 2500
				WHEN hire_date BETWEEN '2015-01-16'::DATE AND '2020-03-04'::DATE THEN salary + 1500
				ELSE salary
			END),
	job_title = (CASE
				WHEN hire_date < '2015-01-16'::DATE THEN CONCAT('Senior', ' ', job_title) 
				WHEN hire_date BETWEEN '2015-01-16'::DATE AND '2020-03-04'::DATE THEN CONCAT('Mid-', job_title)
				ELSE job_title
			END);



-- GPT Optimal Solution
UPDATE
	employees
SET
	salary = (CASE
				WHEN hire_date < '2015-01-16' THEN salary + 2500
				WHEN hire_date < '2020-03-04' THEN salary + 1500
				ELSE salary
		   	END),
	job_title = (CASE 
					WHEN hire_date < '2015-01-16' THEN CONCAT('Senior ', job_title)
					WHEN hire_date < '2020-03-04' THEN CONCAT('Mid-', job_title)
					ELSE job_title
			   END)
WHERE
	hire_date < '2020-03-04';



-- Sub-optimal Solution
UPDATE
	employees
SET
	job_title = CONCAT('Senior', ' ', job_title),
	salary = salary + 2500
WHERE
	hire_date < '2015-01-16'::DATE;


UPDATE
	employees
SET
	job_title = CONCAT('Mid-', job_title),
	salary = salary + 1500
WHERE
	hire_date BETWEEN '2015-01-16'::DATE AND '2020-03-04'::DATE;