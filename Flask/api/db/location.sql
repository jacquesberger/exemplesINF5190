create table pays (
  id integer primary key,
  nom varchar(50)
);

create table provinces (
  id integer primary key,
  nom varchar(50),
  pays_id integer,
  foreign key (pays_id) references pays(id)
);

create table villes (
  id integer primary key,
  nom varchar(50),
  province_id integer,
  foreign key (province_id) references provinces(id)
);

insert into pays(id, nom) values(1, 'Canada');
insert into pays(id, nom) values(2, 'Chine');
insert into pays(id, nom) values(3, 'Cambodge');

insert into provinces(id, nom, pays_id) values(1, 'Ontario', 1);
insert into provinces(id, nom, pays_id) values(2, 'Alberta', 1);
insert into provinces(id, nom, pays_id) values(3, 'Jiangxi', 2);
insert into provinces(id, nom, pays_id) values(4, 'Heilongjiang', 2);
insert into provinces(id, nom, pays_id) values(5, 'Kampong Chhnang', 3);
insert into provinces(id, nom, pays_id) values(6, 'Rotanah Kiri', 3);

insert into villes(id, nom, province_id) values(1, 'Toronto', 1);
insert into villes(id, nom, province_id) values(2, 'Mississauga', 1);
insert into villes(id, nom, province_id) values(3, 'Edmonton', 2);
insert into villes(id, nom, province_id) values(4, 'Calgary', 2);
insert into villes(id, nom, province_id) values(5, 'Zhangshu', 3);
insert into villes(id, nom, province_id) values(6, 'Dexing', 3);
insert into villes(id, nom, province_id) values(7, 'Harbin', 4);
insert into villes(id, nom, province_id) values(8, 'Mudanjiang', 4);
insert into villes(id, nom, province_id) values(9, 'Kampong Chhnang', 5);
insert into villes(id, nom, province_id) values(10, 'Krang Ta Mun', 5);
insert into villes(id, nom, province_id) values(11, 'Banlung', 6);
insert into villes(id, nom, province_id) values(12, 'Veun Sai', 6);
