SELECT
    a.name,
    CASE
        WHEN EXTRACT(hour FROM cour.start) BETWEEN 6 AND 20 THEN 'Day'
        ELSE 'Night'
        END AS dat_time,
    cour.bill,
    cl.full_name,
    cr.make,
    cr.model,
    cat.name
FROM
    courses AS cour
        JOIN addresses AS a
            ON cour.from_address_id = a.id
                JOIN clients AS cl
                    ON cour.client_id = cl.id
                        JOIN cars AS cr
                            ON cour.car_id = cr.id
                                JOIN categories AS cat
                                    ON cr.category_id = cat.id
ORDER BY
    cour.id;