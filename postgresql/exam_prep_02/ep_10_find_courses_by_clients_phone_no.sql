CREATE OR REPLACE FUNCTION fn_courses_by_client(
    IN phone_num VARCHAR(20),
    OUT client_courses INT
) AS
$$
    BEGIN
        SELECT INTO client_courses
            count(co.id)
        FROM clients AS cl
            JOIN courses AS co
                ON cl.id = co.client_id
        WHERE cl.phone_number = phone_num
        GROUP BY cl.id;

        IF client_courses IS NULL THEN
            client_courses := 0;
        END IF;
    END;
$$
LANGUAGE plpgsql;