create table users (
  id integer primary key,
  utilisateur varchar(25),
  email varchar(100),
  salt varchar(32),
  hash varchar(128)
);

create table sessions (
  id integer primary key,
  id_session varchar(32),
  utilisateur varchar(25)
);
