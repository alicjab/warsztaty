CREATE TABLE Users(
	id int auto_increment,
    name varchar(255),
    hashed_password varchar(255),
    email varchar(255) unique,
    primary key(id)
);