create table profiles (
  id integer primary key,
  fname varchar(40),
  lname varchar(40),
  pic_id varchar(32)
);

create table pictures (
  id varchar(32) primary key,
  data blob
);
