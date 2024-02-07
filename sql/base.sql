CREATE TABLE chats(
  id INTEGER PRIMARY KEY,
  mas_users TEXT, -- mas_users = [1, 2, 3, 4, 5]
  mas_messages TEXT DEFAULT NULL -- mas_messages = [{"id":0,"sender_id":0,"content":"text","timestamp":"DATETIME","is_read":False}]
  -- FOREIGN KEY (mas_users) REFERENCES users (id),
);
CREATE TABLE users(
  id INTEGER PRIMARY KEY,
  f_name TEXT,
  s_name TEXT,
  city TEXT DEFAULT NULL,
  -- birth DATE,

  avatar_file TEXT, -- default засунуть файл
  mas_photosFiles TEXT DEFAULT NULL, -- [1, 2, 3, 4, 5] - usersFiles
  mas_music TEXT DEFAULT NULL, -- [1, 2, 3, 4, 5] - musicFiles

  mas_posts TEXT DEFAULT NULL, -- [1, 2, 3, 4, 5] - usersPosts

  password TEXT,
  email TEXT UNIQUE,

  mas_friends TEXT DEFAULT NULL, -- [1, 2, 3, 4, 5]
  mas_chats TEXT DEFAULT NULL -- [1, 2, 3, 4, 5]
  -- FOREIGN KEY (mas_chats) REFERENCES chats (id)
);
CREATE TABLE usersPosts(
  id INTEGER PRIMARY KEY,
  user_id INTEGER, -- для надежности
  content TEXT,
  file TEXT DEFAULT NULL -- file и запятую не забудь
  -- timestamp DATE,
);
CREATE TABLE musicFiles(
  id INTEGER PRIMARY KEY,
  user_id INTEGER, -- для надежности
  file TEXT -- file
);
CREATE TABLE usersFiles(
  id INTEGER PRIMARY KEY,
  user_id INTEGER, -- для надежности
  file TEXT -- file
);
-- Почему TEXT вместо Array ? плохо разобрался или не получилось