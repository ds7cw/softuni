SELECT
    ca.id,
    ca.make,
    ca.mileage,
    COUNT(bill) AS count_of_courses,
    ROUND(AVG(bill), 2) AS average_bill
FROM cars AS ca
    LEFT JOIN courses AS co
        ON co.car_id = ca.id
GROUP BY
    ca.id,
    ca.make,
    ca.mileage
HAVING
    count(bill) <> 2
ORDER BY
    count_of_courses DESC,
    ca.id ASC;