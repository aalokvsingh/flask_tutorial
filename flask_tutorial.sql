
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

DROP TABLE IF EXISTS user;
CREATE TABLE post (
    id int NOT NULL AUTO_INCREMENT,
    ptitle varchar(255) NOT NULL,
    pcontent varchar(255),
    create_at varchar(255) NOT NULL,
    image_path varchar(255) NOT NULL,
    pstatus int(1) DEFAULT 1,
    PRIMARY KEY (id)
);