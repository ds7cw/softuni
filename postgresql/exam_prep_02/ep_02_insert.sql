INSERT INTO clients(full_name, phone_number)
SELECT
    CONCAT(first_name, ' ', last_name) AS full_name,
    CONCAT('(088) 9999', ("id"::INT * 2)) AS phone_no
FROM
    drivers
WHERE
    "id" BETWEEN 10 AND 20;