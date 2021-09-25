CREATE DATABASE PAAT;
USE PAAT;

-- Creating tables 
--

CREATE TABLE Users
(	
	Username CHAR(50) NOT NULL,
	Email CHAR(50) NULL,
	UserPassword VARCHAR(4096) NULL,
	
	PRIMARY KEY(Username)
);

-- Procedures to add values
--
DELIMITER $$
CREATE PROCEDURE insUser(a CHAR(50), b CHAR(50), c VARCHAR (4096))
BEGIN
	IF (a IS NOT NULL) THEN
		INSERT INTO Users VALUES (a,b,c);
	END IF;
END$$

DELIMITER ;