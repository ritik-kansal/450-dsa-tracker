CREATE TABLE `user`
(
 `id`       int NOT NULL AUTO_INCREMENT ,
 `name`     varchar(45) NOT NULL ,
 `username` varchar(45) NOT NULL ,
 `email`    varchar(255) NOT NULL ,
 `linkedin` varchar(255) NOT NULL ,
 `github`   varchar(255) NOT NULL ,
 `password` varchar(255) NOT NULL ,

PRIMARY KEY (`id`)
);

CREATE TABLE `user_asked_for_pair_programming`
(
 `id`      int NOT NULL AUTO_INCREMENT ,
 `user_id` int NOT NULL ,

PRIMARY KEY (`id`),
KEY `fkIdx_74` (`user_id`),
CONSTRAINT `FK_73` FOREIGN KEY `fkIdx_74` (`user_id`) REFERENCES `user` (`id`)
);

CREATE TABLE `pair_programmers`
(
 `id`     int NOT NULL AUTO_INCREMENT ,
 `user_1` int NOT NULL ,
 `user_2` int NOT NULL ,

PRIMARY KEY (`id`),
KEY `fkIdx_64` (`user_1`),
CONSTRAINT `FK_63` FOREIGN KEY `fkIdx_64` (`user_1`) REFERENCES `user` (`id`),
KEY `fkIdx_67` (`user_2`),
CONSTRAINT `FK_66` FOREIGN KEY `fkIdx_67` (`user_2`) REFERENCES `user` (`id`)
);


CREATE TABLE `topic`
(
 `id`   int NOT NULL AUTO_INCREMENT ,
 `name` varchar(100) NULL ,

PRIMARY KEY (`id`)
);


CREATE TABLE `question`
(
 `id`       int NOT NULL AUTO_INCREMENT ,
 `link`     text NOT NULL ,
 `level`    int NOT NULL ,
 `topic_id` int NOT NULL ,

PRIMARY KEY (`id`),
KEY `fkIdx_40` (`topic_id`),
CONSTRAINT `FK_39` FOREIGN KEY `fkIdx_40` (`topic_id`) REFERENCES `topic` (`id`)
);


CREATE TABLE `question_user_mark`
(
 `id`          int NOT NULL AUTO_INCREMENT ,
 `user_id`     int NOT NULL ,
 `question_id` int NOT NULL ,
 `mark`        int NOT NULL ,
 `created_at`  timestamp NOT NULL ,

PRIMARY KEY (`id`),
KEY `fkIdx_46` (`user_id`),
CONSTRAINT `FK_45` FOREIGN KEY `fkIdx_46` (`user_id`) REFERENCES `user` (`id`),
KEY `fkIdx_49` (`question_id`),
CONSTRAINT `FK_48` FOREIGN KEY `fkIdx_49` (`question_id`) REFERENCES `question` (`id`)
);

CREATE TABLE `mark_updates`
(
 `id`                    int NOT NULL AUTO_INCREMENT ,
 `question_user_mark_id` int NOT NULL ,
 `updated_at`            timestamp NOT NULL ,

PRIMARY KEY (`id`),
KEY `fkIdx_57` (`question_user_mark_id`),
CONSTRAINT `FK_56` FOREIGN KEY `fkIdx_57` (`question_user_mark_id`) REFERENCES `question_user_mark` (`id`)
);


