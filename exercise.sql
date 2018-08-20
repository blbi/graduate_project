create table ROUTINE (
	sex varchar(1) not null,
	timing varchar(10) not null,
	bodypart varchar(8) not null,
	url varchar(15) not null,
	primary key (url)
);

create table EXERCISE (
	video_num int(7) not null,
	sex varchar(1) not null,
	length varchar(3) not null,
	bodypart varchar(8) not null,
	excer_type varchar(10) not null,
	trainer varchar(15) not null,
	equipment varchar(20) not null,
	timing varchar(10) not null,
	level varchar(1) not null,
	url varchar(15) not null,
	primary key (url)
);

create table USER (
	user_num int(6) not null,
	sex varchar(1) not null,
	bodypart varchar(8) not null,
	muscle varchar(1) not null,
	endurance varchar(1) not null,
	age int(3) not null,
	height int(3) not null,
	weight int(3) not null,
	primary key(user_num)
);

create table HISTORY (
	user_num int(6) not null,
	video_num int(6) not null,
	rating int(1) not null,
	time timestamp default current_timestamp on update current_timestamp,
	primary key(user_num)
);
