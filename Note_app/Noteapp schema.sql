use Notes;
show Databases;
Create table User_record(
id int  auto_increment primary key,
Work_type varchar(50),
Content Varchar(200),
Creation Date
);
select *from User_record;
drop table User_record;
TRUNCATE User_record;
DESC User_Record;
Alter table User_record
change  Creation  Creation_date DATE;