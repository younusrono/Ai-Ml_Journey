-- UPADTE TABLE 
USE instagram;

SELECT * FROM user;
SET SQL_SAFE_UPDATES=0;
--  This statement is used for no error in db
--  because sql doesnot allow changes in db

UPDATE user 
SET followers=600
WHERE age = 16; 