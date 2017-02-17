create table artiste (
  id integer primary key,
  nom varchar(25),
  est_solo boolean,
  nombre_individus integer
);

insert into artiste (nom, est_solo, nombre_individus) values ('Michael Jackson', 1, 1);
insert into artiste (nom, est_solo, nombre_individus) values ('Michael Buble', 1, 1);
insert into artiste (nom, est_solo, nombre_individus) values ('Elvis Presley', 1, 1);
insert into artiste (nom, est_solo, nombre_individus) values ('Iron Maiden', 0, 6);
insert into artiste (nom, est_solo, nombre_individus) values ('Metallica', 0, 4);
insert into artiste (nom, est_solo, nombre_individus) values ('The Sweet Database', 0, 9);
insert into artiste (nom, est_solo, nombre_individus) values ('Computing Gods', 0, 3);
