DROP TABLE IF EXISTS Users;

CREATE TABLE Users (
	username varchar(255),
	password varchar(255),
	PRIMARY KEY (username)
);

INSERT INTO Users VALUES (
	"thebillington",
	"password"
);

INSERT INTO Users VALUES (
	"testaccount",
	"pass1234"
);