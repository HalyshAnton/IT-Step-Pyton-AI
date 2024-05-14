-- ВИВЕСТИ ПРОФЕСІЮ, З НАЙМЕНШОЮ КІЛЬКІСТЮ СТУДЕНТІВ

-- СОРТУВАННЯ( ПОВІЛЬНО)
SELECT JOB, COUNT(*) AS "JOB COUNT"
FROM STUDENT
GROUP BY JOB
ORDER BY "JOB COUNT" DESC
LIMIT 1;


--- ВИКОРИСТАННЯ ТИМЧАСОВОЇ ТАБЛИЦІ( ШВИДШЕ)
WITH COUNTS_TABLE AS (
	SELECT JOB, COUNT(*) AS "JOB COUNT"
	FROM STUDENT
	GROUP BY JOB
)

SELECT JOB
FROM COUNTS_TABLE
WHERE "JOB COUNT" = (
	SELECT MAX("JOB COUNT")
	FROM COUNTS_TABLE
)

