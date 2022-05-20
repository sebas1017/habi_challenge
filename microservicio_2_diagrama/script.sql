CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(120) NOT NULL,
  `password` varchar(120) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id_uindex` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=latin1;




CREATE TABLE `ranking` (
  `property_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `date_register` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`property_id`,`user_id`),
  KEY `ranking_user_id_fk` (`user_id`),
  KEY `ranking_property_id_fk` (`property_id`),
  CONSTRAINT `ranking_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `ranking_property_id_fk` FOREIGN KEY (`property_id`) REFERENCES `property` (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 81 DEFAULT CHARSET = latin1;

