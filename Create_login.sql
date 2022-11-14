/**
create database if not exists students_login_db;
use students_login_db;
drop table if exists students;
create table students
(
    uni varchar(12) primary key,
    first_name varchar(128) not null,
    last_name varchar(128) not null,
    middle_name varchar(128) null,
    email varchar(256) not null,
    password varchar(256) not null,
    status varchar(128)  not null,
    constraint students_email_unique unique(email)
);
insert into students_login_db.students(uni, last_name, first_name, email, password, status) values ("rl3155", "Liu", "Rosie", "rl3155@columbia.edu", "password", "ACTIVAT");
update students set status="Verified" where uni="rl3155" and email="rl3155@columbia.edu";
**/
create table students_profile
(
    uni varchar(12) primary key,
    timezone varchar(128) not null,
    major varchar(128) not null,
    gender varchar(12) not null,
    personal_message varchar(256) null
);
insert into students_login_db.students_profile(uni, timezone, major, gender, personal_message) values ("rl3155", "PST", "Data Science", "F", "xxxx");
