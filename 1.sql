-- CREATE TABLE IF NOT EXISTS FAMILYINFO(
-- 	ID SERIAL PRIMARY KEY,
-- 	INFO VARCHAR(30),
-- 	STUDENT_ID INT REFERENCES STUDENT(ID)
-- );

-- INSERT INTO FAMILYINFO(
-- 	INFO,
-- 	STUDENT_ID
-- ) VALUES
-- ('BROTHER', 3),
-- ('SISTER', 11),
-- ('SISTER', 1),
-- ('MOTHER', 1),
-- ('FATHER', 1);

---ВИВЕСТИ ДАНІ ПРО СТУДЕНТІВ РАЗОМ З ДАНИМИ ПРО СІМ'Ю
SELECT *
FROM FAMILYINFO JOIN STUDENT ON FAMILYINFO.STUDENT_ID = STUDENT.ID

-- ВИВЕСТИ ДАНІ СТУДЕНТІВ, ПРО ЯКИХ Є ДАНІ ПРО САМІ
-- SELECT *
-- FROM STUDENT
-- WHERE ID IN (SELECT STUDENT_ID
-- 			 FROM FAMILYINFO
-- )



