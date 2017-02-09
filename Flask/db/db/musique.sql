create table artiste (
  id integer primary key,
  nom varchar(25),
  est_solo boolean,
  nombre_individus integer
);

create table maison_disque (
  id integer primary key,
  nom varchar(25)
);

create table album (
  id integer primary key,
  titre varchar(25),
  annee integer,
  artiste_id integer,
  maison_disque_id integer,
  foreign key (artiste_id) references artiste(id),
  foreign key (maison_disque_id) references maison_disque(id)
);

insert into artiste values (1, 'Michael Jackson', 1, 1);
insert into artiste values (2, 'Michael Buble', 1, 1);
insert into artiste values (3, 'Elvis Presley', 1, 1);
insert into artiste values (4, 'Iron Maiden', 0, 6);
insert into artiste values (5, 'Metallica', 0, 4);
insert into artiste values (6, 'The Sweet Database', 0, 9);
insert into artiste values (7, 'Computing Gods', 0, 3);

insert into maison_disque values (1, 'Century Media');
insert into maison_disque values (2, 'Nuclear Blast');
insert into maison_disque values (3, 'Magic Geni');

insert into album values (1, 'Thriller', 1982, 1, 1);
insert into album values (2, 'Xscape', 2014, 1, 1);
insert into album values (3, 'Bad', 1987, 1, 1);
insert into album values (4, 'Dangerous', 1991, 1, 1);
insert into album values (5, 'Invincible', 2001, 1, 2);
insert into album values (6, 'Immortal', 2011, 1, 1);
insert into album values (7, 'To Be Loved', 2013, 2, 1);
insert into album values (8, 'Christmas', 2011, 2, 1);
insert into album values (9, 'Crazy Love', 2009, 2, 1);
insert into album values (10, 'Today', 1975, 3, 1);
insert into album values (11, 'Promised Land', 1975, 3, 1);
insert into album values (12, 'Fear Of The Dark', 1992, 4, 2);
insert into album values (13, 'Killers', 1981, 4, 2);
insert into album values (14, 'Piece of Mind', 1983, 4, 2);
insert into album values (15, 'Powerslave', 1984, 4, 2);
insert into album values (16, 'Metallica', 1991, 5, 2);
