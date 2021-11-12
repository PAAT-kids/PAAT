CREATE DATABASE PAAT;
USE PAAT;
set sql_mode='';
-- Creating tables 
--

CREATE TABLE Users
(	
	Username CHAR(50) NOT NULL,
	Email CHAR(50) NULL,
	UserPassword VARCHAR(4096) NULL,
	PRIMARY KEY(Username)
);

CREATE TABLE Contacts
(	
	ContactName CHAR(50) NOT NULL,
	DestinationAdd CHAR(50) NOT NULL,
	PRIMARY KEY(ContactName)
);

CREATE TABLE Sent
(	
	ID CHAR(50) NOT NULL,
	Sizee INT(50) NULL,
	Datee DATE NULL,
	Time TIME(0) NULL,
	SenderAdd CHAR(50) NULL,
	ReceiverAdd CHAR(50) NULL,
	SourceETH CHAR(50) NULL,
	DestinationETH CHAR(50) NULL, 
	Type CHAR(50) NULL,
	Version INT(50) NULL,
	IHL CHAR(50) NULL,
	TOS VARBINARY(50) NULL,
	TotalLength CHAR(50) NULL,
	Identification INT(50) NULL,
	Flags CHAR(50) NULL,
	FragmentOffset INT(50) NULL,
	TTL INT(50) NULL,
	Protocol CHAR(50) NULL,
	HeaderChecksum VARBINARY(50) NULL,
	SourceIP CHAR(50) NULL,
	DestinationIP CHAR(50) NULL, 
	Options CHAR(50) NULL,
	SourcePort CHAR(50) NULL,
	DestinationPort CHAR(50) NULL,
	Checksum VARBINARY(50) NULL,
	PRIMARY KEY(ID)
);

CREATE TABLE NTP
(	
	ID CHAR(50) NOT NULL,
	Leap INT(50) NULL,
	Version INT(50) NULL,
	Modee CHAR(50) NULL,
	Stratum INT(50) NULL,
	Poll INT(50) NULL,
	Precisionn INT(50) NULL,
	Delay INT(50) NULL,
	Dispersion INT(50) NULL,
	ID2 CHAR(50) NULL,
	ReferenceID INT(50) NULL,
	Reference TIME(0) NULL,
	Origin TIME(0) NULL,
	Receive TIME(0) NULL,
	Sent TIME(0) NULL,
	FOREIGN KEY(ID) REFERENCES Sent(ID),
	PRIMARY KEY(ID)
);

CREATE TABLE DNS
(	
	ID CHAR(50) NOT NULL,
	Qname CHAR(50) NULL,
	Qtype INT(50) NULL,
	Qclass INT(50) NULL,
	FOREIGN KEY(ID) REFERENCES Sent(ID),
	PRIMARY KEY(ID)
);

CREATE TABLE SSDP
(	
	ID CHAR(50) NOT NULL,
	Hostt CHAR(50) NULL,
	Port CHAR(50) NULL,
	MAN CHAR(50) NULL,
	MX CHAR(50) NULL,
	ST INT(50) NULL,
	FOREIGN KEY(ID) REFERENCES Sent(ID),
	PRIMARY KEY(ID)
);
CREATE TABLE Received
(	
	ID CHAR(50) NOT NULL,
	Sizee INT(50) NULL,
	Type CHAR(50) NULL,
	Datee DATE NULL,
	Time TIME(0) NULL,
	SenderAdd CHAR(50) NULL,
	ReceiverAdd CHAR(50) NULL,
	FinalSize INT(50) NULL,
	Amplification INT(50) NULL,
	SentID CHAR(50) NULL,
	PRIMARY KEY(ID)
);


CREATE TABLE Drafts
(	
	ID CHAR(50) NOT NULL,
	Datee DATE NULL,
	Time TIME(0) NULL,
	SourceETH CHAR(50) NULL,
	DestinationETH CHAR(50) NULL, 
	Type CHAR(50) NULL,
	Version INT(50) NULL,
	IHL CHAR(50) NULL,
	TOS VARBINARY(50) NULL,
	TotalLength CHAR(50) NULL,
	Identification INT(50) NULL,
	Flags CHAR(50) NULL,
	FragmentOffset INT(50) NULL,
	TTL INT(50) NULL,
	Protocol CHAR(50) NULL,
	HeaderChecksum VARBINARY(50) NULL,
	SourceIP CHAR(50) NULL,
	DestinationIP CHAR(50) NULL, 
	Options CHAR(50) NULL,
	SourcePort CHAR(50) NULL,
	DestinationPort CHAR(50) NULL,
	Checksum VARBINARY(50) NULL,
	PacketType CHAR(50) NOT NULL,
	Length INT(50),
	PRIMARY KEY(ID)
);

CREATE TABLE NTP2
(	
	ID CHAR(50) NOT NULL,
	Leap INT(50) NULL,
	Version INT(50) NULL,
	Modee CHAR(50) NULL,
	Stratum INT(50) NULL,
	Poll INT(50) NULL,
	Precisionn INT(50) NULL,
	Delay INT(50) NULL,
	Dispersion INT(50) NULL,
	ID2 CHAR(50) NULL,
	ReferenceID INT(50) NULL,
	Reference TIME(0) NULL,
	Origin TIME(0) NULL,
	Receive TIME(0) NULL,
	Sent TIME(0) NULL,
	FOREIGN KEY(ID) REFERENCES Drafts(ID),
	PRIMARY KEY(ID)
);

CREATE TABLE DNS2
(	
	ID CHAR(50) NOT NULL,
	Qname CHAR(50) NULL,
	Qtype INT(50) NULL,
	Qclass INT(50) NULL,
	FOREIGN KEY(ID) REFERENCES Drafts(ID),
	PRIMARY KEY(ID)
);

CREATE TABLE SSDP2
(	
	ID CHAR(50) NOT NULL,
	Hostt CHAR(50) NULL,
	Port CHAR(50) NULL,
	MAN CHAR(50) NULL,
	MX CHAR(50) NULL,
	ST INT(50) NULL,
	FOREIGN KEY(ID) REFERENCES Drafts(ID),
	PRIMARY KEY(ID)
);

CREATE TABLE Sends
(	
	Username CHAR(50) NOT NULL,
	ID CHAR(50) NOT NULL,
	FOREIGN KEY(ID) REFERENCES Sent(ID),
	FOREIGN KEY(Username) REFERENCES Users(Username)
);

CREATE TABLE Receives
(	
	Username CHAR(50) NOT NULL,
	ID CHAR(50) NOT NULL,
	FOREIGN KEY(Username) REFERENCES Users(Username),
	FOREIGN KEY(ID) REFERENCES Received(ID)
);

CREATE TABLE Creates
(	
	Username CHAR(50) NOT NULL,
	ID CHAR(50) NOT NULL,
	FOREIGN KEY(ID) REFERENCES Drafts(ID),
	FOREIGN KEY(Username) REFERENCES Users(Username)
);

CREATE TABLE Saves
(	
	Username CHAR(50) NOT NULL,
	ContactName CHAR(50) NOT NULL,
	FOREIGN KEY(Username) REFERENCES Users(Username),
	FOREIGN KEY(ContactName) REFERENCES Contacts(ContactName)
);

CREATE TABLE AutoSend
(	
	ID CHAR(50) NOT NULL,
	Sizee INT(50) NULL,
	Datee DATE NULL,
	Time TIME(0) NULL,
	SenderAdd CHAR(50) NULL,
	ReceiverAdd CHAR(50) NULL,
	SourceETH CHAR(50) NULL,
	DestinationETH CHAR(50) NULL, 
	Type CHAR(50) NULL,
	Version INT(50) NULL,
	IHL CHAR(50) NULL,
	TOS VARBINARY(50) NULL,
	TotalLength CHAR(50) NULL,
	Identification INT(50) NULL,
	Flags CHAR(50) NULL,
	FragmentOffset INT(50) NULL,
	TTL INT(50) NULL,
	Protocol CHAR(50) NULL,
	HeaderChecksum VARBINARY(50) NULL,
	SourceIP CHAR(50) NULL,
	DestinationIP CHAR(50) NULL, 
	Options CHAR(50) NULL,
	SourcePort CHAR(50) NULL,
	DestinationPort CHAR(50) NULL,
	Checksum VARBINARY(50) NULL,
	PRIMARY KEY(ID)
);

CREATE TABLE AutoReceive
(	
	ID CHAR(50) NOT NULL,
	Sizee INT(50) NULL,
	Type CHAR(50) NULL,
	Datee DATE NULL,
	Time TIME(0) NULL,
	SenderAdd CHAR(50) NULL,
	ReceiverAdd CHAR(50) NULL,
	FinalSize INT(50) NULL,
	Amplification INT(50) NULL,
	PRIMARY KEY(ID)
);
DELIMITER $$

-- Procedures to delete values from autocreate tables
--

CREATE PROCEDURE deleteSent()
BEGIN
	Delete FROM AutoSend;
END$$

CREATE PROCEDURE deleteReceived()
BEGIN
	Delete FROM AutoReceive;
END$$

-- Procedures to add values
--

CREATE PROCEDURE insUser(a CHAR(50), b CHAR(50), c VARCHAR (4096))
BEGIN
	IF (a IS NOT NULL) THEN
		INSERT INTO Users VALUES (a,b,c);
	END IF;
END$$

CREATE PROCEDURE insContacts(a CHAR(50), b CHAR(50))
BEGIN
	IF (a IS NOT NULL) THEN
		INSERT INTO Contacts VALUES (a,b);
	END IF;
END$$

CREATE PROCEDURE insSent(a CHAR(50), b INT(50), c DATE, d TIME(0), e CHAR(50), f CHAR(50), g CHAR(50), h CHAR(50), i CHAR(50), j INT(50), k CHAR(50), l VARBINARY(50), m CHAR(50), n INT(50), o CHAR(50), p INT(50), q INT(50), r CHAR(50), s VARBINARY(50), t CHAR(50), u CHAR(50), v CHAR(50), w CHAR(50), x CHAR(50), y VARBINARY(50))
BEGIN
	IF (a IS NOT NULL) THEN
		INSERT INTO Sent VALUES (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y);
	END IF;
END$$

CREATE PROCEDURE insNTP(a CHAR(50), b INT(50), c INT(50), d CHAR(50), e INT(50), f INT(50), g INT(50), h INT(50), i INT(50), j CHAR(50), k INT(50), l TIME(0), m TIME(0), n TIME(0), o TIME(0))
BEGIN
	IF (a IS NOT NULL) THEN
		INSERT INTO NTP VALUES (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o);
	END IF;
END$$

CREATE PROCEDURE insDNS(a CHAR(50), b CHAR(50), c INT(50), d INT(50))
BEGIN
	IF (a IS NOT NULL) THEN
		INSERT INTO DNS VALUES (a,b,c,d);
	END IF;
END$$

CREATE PROCEDURE insSSDP(a CHAR(50), b CHAR(50), c CHAR(50), d CHAR(50), e CHAR(50), f INT(50))
BEGIN
	IF (a IS NOT NULL) THEN
		INSERT INTO SSDP VALUES (a,b,c,d,e,f);
	END IF;
END$$

CREATE PROCEDURE insReceived(a CHAR(50), b INT(50), c CHAR(50), d DATE, e TIME(0), f CHAR(50), g CHAR(50), h INT(50), i INT(50), j CHAR(50))
BEGIN
	
	IF (a IS NOT NULL) THEN
		INSERT INTO Received VALUES (a,b,c,d,e,f,h,g,i,j);
	END IF;
END$$

CREATE PROCEDURE insDrafts(a CHAR(50), b DATE, c TIME(0), d CHAR(50), e CHAR(50),  f CHAR(50), g INT(50), h CHAR(50), i VARBINARY(50),j CHAR(50), k INT(50), l CHAR(50), m INT(50), n INT(50), o CHAR(50), p VARBINARY(50), q CHAR(50), r CHAR(50),  s CHAR(50), t CHAR(50), u CHAR(50), v VARBINARY(50), w CHAR(50), x INT(50))
BEGIN
	IF (a IS NOT NULL) THEN
		INSERT INTO Drafts VALUES (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x);
	END IF;
END$$

CREATE PROCEDURE insNTP2(a CHAR(50), b INT(50), c INT(50), d CHAR(50), e INT(50), f INT(50), g INT(50), h INT(50), i INT(50), j CHAR(50), k INT(50), l TIME(0), m TIME(0), n TIME(0), o TIME(0))
BEGIN
	IF (a IS NOT NULL) THEN
		INSERT INTO NTP2 VALUES (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o);
	END IF;
END$$

CREATE PROCEDURE insDNS2(a CHAR(50), b CHAR(50), c INT(50), d INT(50))
BEGIN
	IF (a IS NOT NULL) THEN
		INSERT INTO DNS2 VALUES (a,b,c,d);
	END IF;
END$$

CREATE PROCEDURE insSSDP2(a CHAR(50), b CHAR(50), c CHAR(50), d CHAR(50), e CHAR(50), f INT(50))
BEGIN
	IF (a IS NOT NULL) THEN
		INSERT INTO SSDP2 VALUES (a,b,c,d,e,f);
	END IF;
END$$

CREATE PROCEDURE insSends(a CHAR(50), b CHAR(50))
BEGIN
	IF (a IS NOT NULL AND b IS NOT NULL) THEN
		INSERT INTO Sends VALUES (a,b);
	END IF;
END$$

CREATE PROCEDURE insReceives(a CHAR(50), b CHAR(50))
BEGIN
	IF (a IS NOT NULL AND b IS NOT NULL) THEN
		INSERT INTO Receives VALUES (a,b);
	END IF;
END$$

CREATE PROCEDURE insCreates(a CHAR(50), b CHAR(50))
BEGIN
	IF (a IS NOT NULL AND b IS NOT NULL) THEN
		INSERT INTO Creates VALUES (a,b);
	END IF;
END$$

CREATE PROCEDURE insSaves(a CHAR(50), b CHAR(50))
BEGIN
	IF (a IS NOT NULL AND b IS NOT NULL) THEN
		INSERT INTO Saves VALUES (a,b);
	END IF;
END$$

CREATE PROCEDURE insAutoSend(a CHAR(50), b INT(50), c DATE, d TIME(0), e CHAR(50), f CHAR(50), g CHAR(50), h CHAR(50), i CHAR(50), j INT(50), k CHAR(50), l VARBINARY(50), m CHAR(50), n INT(50), o CHAR(50), p INT(50), q INT(50), r CHAR(50), s VARBINARY(50), t CHAR(50), u CHAR(50), v CHAR(50), w CHAR(50), x CHAR(50), y VARBINARY(50))
BEGIN
	IF (a IS NOT NULL) THEN
		INSERT INTO AutoSend VALUES (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y);
	END IF;
END$$

CREATE PROCEDURE insAutoReceive(a CHAR(50), b INT(50), c CHAR(50), d DATE, e TIME(0), f CHAR(50), g CHAR(50), h INT(50), i INT(50))
BEGIN
	IF (a IS NOT NULL) THEN
		INSERT INTO AutoReceive VALUES (a,b,c,d,e,f,h,g,i);
	END IF;
END$$

DELIMITER ;