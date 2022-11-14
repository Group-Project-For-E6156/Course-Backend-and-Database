create schema if not exists teammate_db;

create table if not exists teammate_db.Team
(
    Team_id int not null AUTO_INCREMENT Primary key,
    Team_Name varchar(128) not null,
    Team_Captain_Uni varchar(20) not null,
    Team_Captain varchar(128) not null,
    Course_id int not null,
    Number_needed int,
    Team_message varchar(128) not null
);
 /* team_id integer auto generated 
 number_needed integer 
 created_at update_at delete_at*/
 

insert into teammate_db.Team (Team_name, Team_Captain_Uni, Team_Captain, Course_id, Number_needed, Team_message) values
("6156_team", "xc2597", "Xiaowei Chen", 1, 1, "hello"),
("we are the best", "yr2425", "Yue Rao", 1, 4, "let do it"),
("4111_team", "yr2425", "Yue Rao", 2, 0, "Full");


create table if not exists teammate_db.StudentsInTeam
(
    Uni varchar(128) not null,
    Course_id int not null,
    Team_id int not null,
    primary key (Team_id, Uni),
    Foreign key (Team_id) references Team(Team_id) on delete no action
);

insert into teammate_db.StudentsInTeam (uni, Course_id, Team_id) values
 ("aw3395", 1, 1),
 ("xc2597", 1, 1),
 ("yr2425", 1, 2),
 ("hl3445", 2, 3),
 ("bh2798", 2, 3)

/* uni course_id varchar  index auto genereated integer pri*/
