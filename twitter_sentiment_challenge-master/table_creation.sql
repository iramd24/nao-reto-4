--CREATE TABLE tweets(
--id INT(11) unsigned NOT NULL AUTO_INCREMENT,
--text VARCHAR(255) DEFAULT NULL,
--user VARCHAR(55) DEFAULT NULL,
--hashtags VARCHAR(255) DEFAULT NULL,
--tweet_creation_date DATE DEFAULT NULL,
--retweets INT(11) DEFAULT NULL,
--favs INT(11) DEFAULT NULL,
--PRIMARY KEY (id)
--);

--DDL después de agregar columnas que no creí necesarias al empezar el proyecto
CREATE TABLE `tweets` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `text` varchar(255) DEFAULT NULL,
  `user` varchar(55) DEFAULT NULL,
  `hashtags` varchar(255) DEFAULT NULL,
  `tweet_creation_date` date DEFAULT NULL,
  `retweets` int DEFAULT NULL,
  `favs` int DEFAULT NULL,
  `sentiment` varchar(20) DEFAULT NULL,
  `sentiment_score` decimal(16,16) DEFAULT NULL,
  `subjectivity` varchar(20) DEFAULT NULL,
  `subjectivity_score` decimal(16,16) DEFAULT NULL,
  `translated_text` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) 