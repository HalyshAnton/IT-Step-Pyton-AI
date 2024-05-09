-- ПІДРАХУВАТИ СЕРЕДНІЙ ВІК СТУДЕНТІВ ТИХ ПРОФЕСІЙ, ДЕ Є БІЛЬШЕ ОДНОГО ПРЕДСТАВНИКА
SELECT JOB, AVG(AGE)
FROM STUDENT
GROUP BY JOB
HAVING COUNT(*) > 1;


-- ВИВЕСТИ ПОВНЕ ІМ'Я ПРО ТИХ СТУДЕНТІВ СЕРІДНІЙ ВІК ПРОФЕСІЇ ЯКИХ БІЛЬШЕ 25
SELECT FIRST_NAME || ' ' || LAST_NAME AS FULL_NAME, AGE, JOB
FROM STUDENT
WHERE JOB IN (SELECT JOB
			FROM STUDENT
			GROUP BY JOB
			HAVING AVG(AGE) > 30
)