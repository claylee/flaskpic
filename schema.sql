drop table if exists entries;
commit;
create table entries (
  id integer primary key autoincrement,
  title string not null,
  text string not null
);

drop table if exists piccategory;
commit;
create table piccategory (
  pcatid integer primary key autoincrement,
  title string not null,
  text string not null,
  categorypath string
);

drop table if exists picdocument;
commit;
create table picdocument (
  pdocid integer primary key autoincrement,
  pcateid integer not null,
  title string not null,
  tags string not null,
  docpath string
);

drop table if exists picfile;
commit;
create table picfile (
  id integer primary key autoincrement,
  pdocid integer not null,
  fileno integer not null,
  md5code string not null,
  fpath string,
);
