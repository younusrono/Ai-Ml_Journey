CREATE DATABASE instagram;

USE instagram;
CREATE TABLE user(
  id INT,
  age INT,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(50) UNIQUE,
  followers INT DEFAULT  0,
  following INT,
  CONSTRAINT CHECK(age>=13),
  PRIMARY KEY(id)
);

CREATE TABLE post(
  id INT PRIMARY KEY,
  content VARCHAR(50),
  user_id INT,
  FOREIGN KEY(user_id) REFERENCES user(id)
);
INSERT INTO user 
(id,age,name,email,followers,following)
VALUES
(1, 14, "adam", "adam@yahoo.in", 123, 145),
(2, 15, "bob", "bob123@gmail.com", 200, 200),
(3, 16, "casey", "casey@gmail.com", 300, 306),
(4, 17, "donald", "donald@gmail.com", 200, 105);

SELECT * FROM user;

USE instagram;
SELECT name,following 
FROM user 
WHERE followers >=200;


SELECT name , age FROM USER 
WHERE age>15 AND followers >200;  

SELECT name , age FROM USER 
WHERE age>15 OR followers >200;  

SELECT name , age FROM USER 
WHERE age BETWEEN 15 AND 17;  

SELECT name , age FROM USER 
WHERE email IN ("adam@yahoo.in","bob123@gmail.com","ABC123@gmail.com");

SELECT name , age FROM USER 
WHERE age NOT IN(15,17);

