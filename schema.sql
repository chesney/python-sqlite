CREATE TABLE users(id INTEGER NOT NULL primary key default 1, name varchar(20), age INTEGER);
CREATE TABLE blog(id INTEGER NOT NULL primary key default 1, title varchar(20) NOT NULL, content varchar(50) NOT NULL, author varchar(20) NOT NULL, date timestamp NOT NULL DEFAULT CURRENT_TIME);
