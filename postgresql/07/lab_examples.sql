-- Example 1
CREATE OR REPLACE FUNCTION fn_full_name(first_name VARCHAR, last_name VARCHAR)
RETURNS VARCHAR AS

$$
    DECLARE
        full_name VARCHAR;
    BEGIN
        IF first_name IS NULL and last_name IS NULL THEN
            full_name := NULL;
        ELSIF first_name IS NULL THEN
            first_name := last_name;
        ELSIF last_name IS NULL THEN
            full_name := first_name;
        ELSE
            full_name := concat(first_name, ' ', last_name);
        END IF;
        RETURN full_name;
    END
$$
LANGUAGE plpgsql;

SELECT fn_full_name('Cventan', 'Tomov')
-- SELECT fn_full_name('Cventan', NULL)
-- SELECT fn_full_name(NULL, 'Tomov')
-- SELECT fn_full_name(NULL, NULL)




-- Example 2.1
-- DROP FUNCTION
CREATE OR REPLACE FUNCTION fn_get_city_id(city_name VARCHAR)
RETURNS INT AS

$$
    DECLARE
    city_id INT;

    BEGIN
        SELECT "id" FROM cities
        WHERE name = city_name
        INTO city_id;
        RETURN city_id;
    END
$$
LANGUAGE plpgsql;

SELECT fn_get_city_id('Sofia');

INSERT INTO
    persons(first_name, last_name, city_id)
VALUES
    ('First', 'Last', fn_get_city_id('Plovdiv'));


-- Example 2.2
CREATE OR REPLACE FUNCTION fn_get_city_id(
    IN city_name VARCHAR,
    OUT city_id INT,
    OUT status INT
) AS

$$
    DECLARE
        temp_id INT;
    BEGIN
        SELECT "id" FROM cities WHERE "name" = city_name
        INTO temp_id;    
        IF temp_id IS NULL THEN
            SELECT 100 INTO status;
        ELSE
            -- city_id := temp_id;
            -- status := 0;
            SELECT temp_id 0 INTO city_id, status;
        END IF;
    END;
    -- No RETURN required since we used IN/ OUT within the fn arguments brackets
$$
LANGUAGE plpgsql;

SELECT * from fn_get_city_id('Kaspichan')



-- Example 3
CREATE PROCEDURE sp_add_person(first_name VARCHAR, last_name VARCHAR, city_name VARCHAR)
AS
$$
    BEGIN
        INSERT INTO persons ("first_name", "last_name", "city_id")
        VALUES (first_name, last_name, fn_get_city_id(city_id));

    END;
$$
LANGUAGE plpgsql;

CALL sp_add_person('First', 'Last', 'Burgas');



-- Example 4
CREATE OR REPLACE PROCEDURE p_transfer_money(
    IN sender_id INT,
    IN receiver_id INT,
    IN transfer_amount FLOAT,
    OUT status VARCHAR
)
AS
$$
    DECLARE
        sender_amount FLOAT;
        receiver_amount FLOAT;

    BEGIN
        SELECT b.amount FROM bank AS b WHERE "id" = sender_id INTO sender_amount;
        IF sender_amount < transfer_amount THEN
            status := 'Not enough money';
            RETURN;
        END IF;
        SELECT b.amount FROM bank AS b WHERE "id" = receiver_id INTO receiver_amount;
        UPDATE bank SET amount = amount - transfer_amount WHERE "id" = sender_id;
        UPDATE bank SET amount = amount + transfer_amount WHErE "id" = receiver_id;
        SELECT b.amount FROM bank AS b WHERE "id" = sender_id INTO temp_val;
        IF sender_amount - transfer_amount <> temp_val THEN
            status := 'Error in sender';
            ROLLBACK;
            RETURN;
        END IF;
        SELECT b.amount FROM bank AS b WHERE "id" = receiver_id INTO temp_val;
        IF receiver_amount + amount <> temp_val THEN
            status := 'Error in receiver';
            ROLLBACK;
            RETURN;
        END IF;
        status := 'Transfer done';
        COMMIT;
        RETURN;
    END;
$$
LANGUAGE plpgsql;

CALL p_transfer_money(1, 2, 500, NULL);



-- Example 5
CREATE TABLE
    items(
        id SERIAL PRIMARY KEY,
        status INT,
        create_date DATE
    );


CREATE TABLE
    items_log(
        id SERIAL PRIMARY KEY,
        status INT,
        create_date DATE
    );

CREATE OR REPLACE FUNCTION log_items()
RETURNS TRIGGER AS
$$
    BEGIN
        INSERT INTO items_log(status, create_date)
        VALUES(new.status, new.create_date);
        RETURN new
    END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER log_items_trigger
AFTER INSERT ON items
FOR EACH ROW
EXECUTE PROCEDURE log_items();

INSERT INTO items(status, create_date)
VALUES(1, NOW()), (2, NOW()), (3, NOW());

SELECT * FROM items;
SELECT * FROM items_log;



-- Example 6
CREATE OR REPLACE FUNCTION delete_last_item_log()
RETURNS TRIGGER AS
$$
    BEGIN
        WHILE (SELECT COUNT(*) FROM items_log) > 10 LOOP
            DELETE FROM items_log WHERE "id" = (SELCT MIN("id") FROM items_log);
        END LOOP;
        RETURN new;
    END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE TRIGGER clear_item_log
AFTER INSERT ON items_log
FOR EACH STATEMENT
EXECUTE PROCEDURE delete_last_item_log();

SELECT * FROM items_log;