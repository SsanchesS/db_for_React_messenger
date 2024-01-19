CREATE TABLE chats(
  id INTEGER PRIMARY KEY,
  mas_users TEXT DEFAULT NULL, -- mas_users = [1, 2, 3, 4, 5]
  mas_messages TEXT DEFAULT NULL, -- mas_messages = [{"id":0,"sender_id":0,"content":"text","timetimestamp":"DATETIME","is_read":False}]
  -- FOREIGN KEY (mas_users) REFERENCES users (id),
);
CREATE TABLE users(
  id INTEGER PRIMARY KEY,
  f_name TEXT DEFAULT NULL,
  s_name TEXT DEFAULT NULL,
  password TEXT DEFAULT NULL,
  email TEXT DEFAULT NULL,
  avatar TEXT DEFAULT NULL,
  mas_friends TEXT DEFAULT NULL, -- mas_friends = [1, 2, 3, 4, 5]
  mas_chats TEXT DEFAULT NULL, -- mas_chats = [1, 2, 3, 4, 5]
  -- FOREIGN KEY (mas_chats) REFERENCES chats (id)
);
-- import json
-- mas_friends = [1, 2, 3, 4, 5]
-- mas_friends_str = json.dumps(mas_friends)
-- INSERT INTO users (mas_friends) VALUES (?)', (mas_friends_str,)

-- import json
-- SELECT mas_friends FROM users WHERE id = ?', (1,)
-- result = cursor.fetchone()
-- if result:
--   mas_friends_str = result[0]
--   mas_friends = json.loads(mas_friends_str)



-- 
--


-- CREATE TABLE users(
--   id INTEGER PRIMARY KEY,
--   f_name TEXT DEFAULT NULL,
--   s_name TEXT DEFAULT NULL,
--   pass TEXT DEFAULT NULL,
--   email TEXT DEFAULT NULL,
--   avatar TEXT DEFAULT NULL,
--   all_friends INTEGER DEFAULT NULL,
--   all_chats INTEGER DEFAULT NULL,
--   FOREIGN KEY (all_friends) REFERENCES friends (id)
--   FOREIGN KEY (all_chats) REFERENCES chats (id)
-- );
-- CREATE TABLE friends(
--   id INTEGER PRIMARY KEY,
--   friend_id INTEGER DEFAULT NULL,
-- );
-- CREATE TABLE chats(
--   id INTEGER PRIMARY KEY,
--   all_users INTEGER DEFAULT NULL,
--   all_messages INTEGER DEFAULT NULL,
--   FOREIGN KEY (all_users) REFERENCES users_in_chat (id),
--   FOREIGN KEY (all_messages) REFERENCES messages (id)
-- );
-- CREATE TABLE users_in_chat(
--   id INTEGER PRIMARY KEY,
--   user INTEGER DEFAULT NULL,
-- );
-- CREATE TABLE messages(
--   id INTEGER PRIMARY KEY,
--   mas_message INTEGER DEFAULT NULL,
--   FOREIGN KEY (mas_message) REFERENCES mas_message (id)
-- );
-- CREATE TABLE mas_message(
--   id INTEGER PRIMARY KEY,
--   sender_id INTEGER DEFAULT NULL,
--   content TEXT DEFAULT NULL,
--   timetimestamp DATETIME DEFAULT NULL,
--   is_read BOOLEAN DEFAULT NULL,
--   FOREIGN KEY (sender_id) REFERENCES users (id)
-- );