drop table users;

create table users(user_id int, user_name varchar(255));

insert into users(user_id, user_name) values (1, 'John Doe'), (2, 'Jane Smith'), (3, 'Jim Beam'), (4, 'Jill Johnson'), (5, 'Jack Daniels');

update users set user_name = 'John Dan' where user_id = 1;

select * from users;

select * from users where user_id = 1;

select user_id from users;

create index idn on users(user_id,user_name);

create view user_view as select * from users where user_id between 3 and 5;

select * from user_view;

select * from users where user_id > (select avg(user_id) from users);

delete from users;

drop table users;