
DROP TABLE IF EXISTS user;
CREATE TABLE user (
    id int NOT NULL AUTO_INCREMENT,
    firstname varchar(255) NOT NULL,
    lastname varchar(255),
    username varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    status int(1) DEFAULT 1,
    PRIMARY KEY (id)
);

alter table flask_tutorial.user ADD CONSTRAINT unique_credentials unique (username); 