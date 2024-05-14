-- СТВОРЕННЯ ІНДЕКСУ ПО ДАТІ - ТЕ САМЕ ЩО І БІНАРНЕ ДЕРЕВО
CREATE INDEX STUDENT_DATE_INDEX ON STUDENT (DATE_OF_BIRTH, AGE);


SELECT *
FROM STUDENT
WHERE DATE_OF_BIRTH < '2001-01-01'