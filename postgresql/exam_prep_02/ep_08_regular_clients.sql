SELECT
    cl.full_name,
    COUNT(co.car_id) AS count_of_cars,
    ROUND(SUM(co.bill), 2) AS total_sum
FROM courses AS co
    JOIN clients AS cl
        ON cl.id = co.client_id
WHERE
    SUBSTRING(full_name FROM 2 FOR 1) = 'a'
GROUP BY
    cl.full_name
HAVING
    COUNT(co.car_id) > 1
ORDER BY
    cl.full_name;