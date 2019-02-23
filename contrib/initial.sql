create schema if not exists favorite;

create table if not exists users (
  id    bigint,
  email varchar(100),
  primary key (id)
);

create table if not exists objects (
  id    bigint,
  price double precision,
  primary key (id)
);


create table if not exists favorite.authorized_users (
  user_id    bigint ,
  object_id  bigint ,
  time_added timestamp,
  primary key (user_id, object_id),
  foreign key (user_id) REFERENCES users (id),
  foreign key (object_id) REFERENCES objects (id)
)

