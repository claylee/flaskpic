drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title string not null,
  text string not null
);
drop table if exists piccategory;
create table piccategory (
  pcatid integer primary key autoincrement,
  title string not null,
  text string not null,
  categorypath string
);
drop table if exists picdocument;
create table picdocument (
  pdocid integer primary key autoincrement,
  title string not null,
  text string not null,
  docpath string,
  picno integer,
  picname string,
  picmid string
);