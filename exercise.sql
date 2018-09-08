create table ROUTINE (
	video_num int(7) not null,
	sex varchar(2) not null,
	length int(3) not null,
	timing varchar(10) not null,
	bodypart varchar(20) not null,
	level varchar(2) not null,
	url varchar(100) not null,
	primary key (video_num)
);

create table EXERCISE (
	video_num int(7) not null,
	sex varchar(2) not null,
	length int(3) not null,
	timing varchar(10) not null,
	bodypart varchar(20) not null,
	excer_type varchar(10) not null,
	trainer varchar(15) not null,
	equipment varchar(20) not null,
	level varchar(2) not null,
	url varchar(100) not null,
	primary key (video_num)
);
create table register (
	ID varchar(20) not null,
	PW varchar(100) not null,
	user_num int(6) not null,
	primary key(ID)
);
create table USER (
	user_num int(6) not null,
	sex varchar(1) not null,
	bodypart varchar(20) not null,
	muscle varchar(1) not null,
	endurance varchar(1) not null,
	age int(3) not null,
	height int(3) not null,
	weight int(3) not null,
	primary key(user_num)
);

create table HISTORY (
	user_num int(7) not null,
	video_num int(7) not null,
	rating int(1) not null,
	time timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
