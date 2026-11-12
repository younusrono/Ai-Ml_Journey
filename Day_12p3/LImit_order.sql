USE instagram;
SELECT  name,age, email
FROM user
LIMIT 2;

-- order by clause

SELECT name,age,followers
FROM user
ORDER BY followers ASC