drop table if exists entries;
create table entries(
  id integer primary key autoincrement,
  name text not null,
  username text not null
  password text not null
);