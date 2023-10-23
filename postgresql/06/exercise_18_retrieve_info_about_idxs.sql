SELECT
	tablename,
	indexname,
	indexdef
FROM
	pg_indexes

WHERE
	indexdef LIKE '%ON public%'
ORDER BY
	tablename ASC,
	indexname ASC;