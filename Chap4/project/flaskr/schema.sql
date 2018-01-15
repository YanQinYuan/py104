drop table if exists users;
create table users (
  id integer primary key autoincrement,
  username char(120) not null unique,
  password char(120) not null
);
