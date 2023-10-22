SELECT
	CONCAT('***', SUBSTRING(title, 4)) AS title
FROM books
WHERE title LIKE 'The%'
ORDER BY id;

-- Second Method
SELECT
	REPLACE(title, 'The', '***')
FROM books
WHERE LEFT(title, 3) = 'The'
ORDER BY id;