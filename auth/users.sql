create table users (
  id integer primary key,
  utilisateur varchar(25),
  salt varchar(32),
  hash varchar(128)
);
