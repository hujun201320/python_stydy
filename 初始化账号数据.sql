
create database mini_chat;


use mini_chat;

CREATE TABLE `users` (
    `user_id` int(11) NOT NULL AUTO_INCREMENT,
    `user_name` varchar(30) CHARACTER SET utf8 NOT NULL,
    `user_password` varchar(30) CHARACTER SET utf8 NOT NULL,
    `user_nickname` varchar(20) CHARACTER SET utf8 NOT NULL,
    PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEfAULT CHARSET=latinl;


insert into users values(0,'user1','111111','itcast1');
insert into users values(0,'user2','111111','itcast2');
insert into users values(0,'user3','111111','itcast3');
select * from users;



CREATE TABLE IF NOT EXISTS `users`(
   `user_id` int(11) NOT NULL AUTO_INCREMENT,
    `user_name` varchar(30) CHARACTER SET utf8 NOT NULL,
    `user_password` varchar(30) CHARACTER SET utf8 NOT NULL,
    `user_nickname` varchar(20) CHARACTER SET utf8 NOT NULL,
    PRIMARY KEY (`user_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;