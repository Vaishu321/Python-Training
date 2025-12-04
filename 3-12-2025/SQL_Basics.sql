CREATE DATABASE college_db;
USE college_db;


CREATE TABLE students (
	student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50),
    age INT,
    city VARCHAR(50)
);

INSERT INTO students (first_name, last_name, email, age, city)
VALUES
("Aisha", "Khan", "aisha@example.com", 20, "Mumbai"),
("Rahul", "Sharma", "rahul@example.com", 22, "Delhi"),
("Meera", "Iyer", "meera@example.com", 21, "Chennai"),
("Imran", "Ali", "imran@example.com", 23, "Hyderabad");

SELECT * FROM students;

SELECT first_name, last_name, city
FROM students;

SELECT * FROM students
WHERE city ="Delhi";

SELECT * FROM students
ORDER BY age DESC;

-- Update and Delete--

UPDATE students 
SET city= "Bangalore"
WHERE student_id=2;

UPDATE students
SET age=24
WHERE email="imran@example.com";

DELETE FROM students
WHERE student_id =3;

DELETE FROM students 
WHERE city="Mumbai";

SELECT * FROM students;

DROP TABLE students;

DROP DATABASE college_db;

