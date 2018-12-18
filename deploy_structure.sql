CREATE DATABASE IF NOT EXISTS deploy_db;
USE deploy_db;

DROP TABLE IF EXISTS `teste_deploy`;

CREATE TABLE `teste_deploy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `componente` varchar(255) NOT NULL,
  `versao` varchar(255) NOT NULL,
  `responsavel` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL,
  `data` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;















