create table ROUTINE (
	sex varchar(1) not null,
	timing varchar(10) not null,
	bodypart varchar(8) not null,
	url varchar(15) not null,
	primary key (url)
);

create table EXERCISE (
	sec varchar(1) not null,
	length varchar(3) not null,
	bodypart varchar(8) not null,
	excer_type varchar(10) not null,
	trainer varchar(15) not null,
	timing varchar(10) not null,
	url varchar(15) not null,
	primary key (url)
);