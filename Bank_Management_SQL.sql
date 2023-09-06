create database newdb;


use newdb;


CREATE TABLE `bank` (
  `name` varchar(30) NOT NULL,
  `id` varchar(45) NOT NULL,
  `password` varchar(30) NOT NULL,
  `mobile` varchar(30) NOT NULL,
  `Balance` int NOT NULL,
  PRIMARY KEY (`mobile`,`id`)
);

CREATE TABLE `transaction` (
  `id` varchar(30) NOT NULL,
  `old_amount` varchar(45) DEFAULT NULL,
  `process_amount` varchar(45) DEFAULT NULL,
  `Total` int DEFAULT NULL,
  `Transaction_type` varchar(45) NOT NULL
);

create table bank_emp (name varchar(45), id varchar(45) primary key, password varchar(45));

insert into bank_emp values ('Bm','bm1@abc','1234'),('bemp','be1@abc','4567'),('be','be2@abc','898');


