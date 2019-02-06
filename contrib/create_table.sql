create schema favorite;

create table favorite.authorized_users(
  user_id bigint,
  object_id bigint,
  time_added timestamp,
  primary key (user_id, object_id)
)

