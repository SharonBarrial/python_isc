--create database
CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
);
--follow the instructions
DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Sanaa', 31);
INSERT INTO Ages (name, age) VALUES ('Dillan', 30);
INSERT INTO Ages (name, age) VALUES ('Mateusz', 19);
INSERT INTO Ages (name, age) VALUES ('Elsi', 27);
SELECT hex(name || age) AS X FROM Ages ORDER BY X;
--execute all to get the code in DB Browser for sqlife
SELECT hex(name || age) AS X FROM Ages ORDER BY X;

--my answer was for the first line: 44696C6C616E3330
