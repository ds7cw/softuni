DELETE FROM clients
WHERE "id" NOT IN (
    SELECT client_id
    FROM courses
) AND length(full_name) > 3;