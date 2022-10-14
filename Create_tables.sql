
create schema if not exists courseswork_6156;

create table if not exists courseswork_6156.Courses
(
    Course_id     int auto_increment
        primary key,
    Course_Name  varchar(128) not null,
    Department  varchar(128) not null,
    CourseIntroduction varchar(128) null
);

create table if not exists courseswork_6156.Student_preferences
(
    uni varchar(20),
    Course_id int, 
    prefered_Dept varchar(128) not null, 
    prefered_Timezone varchar(128) not null,
    prefered_message varchar(128) not null, 
    Primary key (Course_id, uni),
    Foreign key (Course_id) references Courses(Course_id) on delete no action
);
/**
 insert into Courses (Course_Name, Department, CourseIntroduction)
    values ("Introduction to Database", "Computer Science", "Basics of database"), 
		   ("Cloud Computing", "Computer Science", "Basics of Cloud Computing and mainly do the big full stack project"),
           ('Linear Regression', 'Statistics', 'Basics of t-testing, F-testing, linear regression and logistic regression');
 **/          
 insert into Student_preferences (uni, Course_id, prefered_Dept, prefered_Timezone, prefered_message) values 
 ("bh2798", 1, "Math", "EST", ""),
 ("ct2522", 1, "Engineering", "EST", "Prefer in person meetings"),
 ("bh2798", 2, "Data Science", "WST", ""),
 ("bh2798", 3, "Computer Science", "WST", "")
 
/**
 insert into Student_preferences (uni, Course_id, prefered_Dept, prefered_Timezone, prefered_message)
**/ 







           
    
    
    