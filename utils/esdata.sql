DROP TABLE student;
CREATE TABLE student(
 id SERIAL PRIMARY KEY,
 name TEXT NOT NULL,
 age INT NOT NULL,
 gender TEXT NOT NULL,
 contact_no TEXT NOT NULL,
 course TEXT NOT NULL,
 address TEXT NOT NULL,
 qualification_10 INT NOT NULL,
 qualification_12 INT NOT NULL
);
insert into student(name,age, gender, contact_no, course, address, qualification_10, qualification_12) values ('sarath', 20, 'M', '9992228333', 'IT', 'blore', 90, 80);
insert into student(name,age, gender, contact_no, course, address, qualification_10, qualification_12) values ('sarath', 20, 'M', '9992228333', 'IT', 'blore', 90, 80);
insert into student(name,age, gender, contact_no, course, address, qualification_10, qualification_12) values ('sarath', 20, 'M', '9992228333', 'IT', 'blore', 90, 80);

DROP TABLE teacher;
CREATE TABLE teacher(
 id SERIAL PRIMARY KEY,
 name TEXT NOT NULL,
 age INT NOT NULL,
 gender TEXT NOT NULL,
 contact_no TEXT NOT NULL,
 course TEXT NOT NULL
);
insert into teacher(name,age, gender, contact_no, course) values ('sarath', 20, 'M', '9992228333', 'IT');
insert into teacher(name,age, gender, contact_no, course) values ('sarath', 20, 'M', '9992228333', 'IT');
insert into teacher(name,age, gender, contact_no, course) values ('sarath', 20, 'M', '9992228333', 'IT');
