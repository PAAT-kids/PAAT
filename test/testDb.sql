-- Inserting dummy data into tables Manually
--

INSERT INTO Users
VALUES('Anas', 'anas123@hotmail.com', '3a42c503953909637f7');

INSERT INTO Contacts
VALUES('Ahmed', '217.164.55.113');

INSERT INTO Sent
VALUES('A123', 20, '2021-10-26', '07:45:55', '172.16.0.9', '186.15.2.10', 'f4:d1:08:0f:84:12', 'c4:e9:0a:54:be:01', 'IPv4', 4, 'None', '0x0', 'None', 1, '', 0, 64, 'udp', 'None', '1.2.3.4', '1.2.3.4', 'None', 'domain', 'domain', 'None');
INSERT INTO Sent
VALUES('A456', 20, '2021-10-26', '07:45:55', '172.16.0.9', '186.15.2.10', 'f4:d1:08:0f:84:12', 'c4:e9:0a:54:be:01', 'IPv4', 4, 'None', '0x0', 'None', 1, '', 0, 64, 'udp', 'None', '1.2.3.4', '1.2.3.4', 'None', 'domain', 'domain', 'None');
INSERT INTO Sent
VALUES('A789', 20, '2021-10-26', '07:45:55', '172.16.0.9', '186.15.2.10', 'f4:d1:08:0f:84:12', 'c4:e9:0a:54:be:01', 'IPv4', 4, 'None', '0x0', 'None', 1, '', 0, 64, 'udp', 'None', '1.2.3.4', '1.2.3.4', 'None', 'domain', 'domain', 'None');


INSERT INTO NTP
VALUES('A123', 61, 4, 'client', 2, 10, 0, 0, 0, '127.0.0.1', 0, '01:15:25', '02:25:35', '03:35:45', '04:45:55');


INSERT INTO DNS
VALUES('A456', 'b www.example.com', 1, 1);


INSERT INTO SSDP
VALUES('A789', '239.255.255.250.1900', '1900', 'ssdp:all', 'ssdp:discover', 2);


INSERT INTO Received
VALUES('A123', 20, 'NTP', '2021-10-10', '08:00:00', '172.16.0.9', '186.15.2.10', 40, 2,'');

INSERT INTO Drafts
VALUES('B3ZX', '2021-10-10', '07:45:55', 'f4:d1:08:0f:84:12', 'c4:e9:0a:54:be:01', 'IPv4', 4, 'None', '0x0', 'None', 1, '', 0, 64, 'udp', 'None', '1.2.3.4', '1.2.3.4', 'None', 'domain', 'domain', 'None', 'ntp', 60);
INSERT INTO Drafts
VALUES('B4ZX', '2021-10-10', '07:45:55', 'f4:d1:08:0f:84:12', 'c4:e9:0a:54:be:01', 'IPv4', 4, 'None', '0x0', 'None', 1, '', 0, 64, 'udp', 'None', '1.2.3.4', '1.2.3.4', 'None', 'domain', 'domain', 'None', 'dns', 61);
INSERT INTO Drafts
VALUES('B5ZX', '2021-10-10', '07:45:55', 'f4:d1:08:0f:84:12', 'c4:e9:0a:54:be:01', 'IPv4', 4, 'None', '0x0', 'None', 1, '', 0, 64, 'udp', 'None', '1.2.3.4', '1.2.3.4', 'None', 'domain', 'domain', 'None', 'ssdp', 62);

INSERT INTO NTP2
VALUES('B3ZX', 61, 4, 'client', 2, 10, 0, 0, 0, '127.0.0.1', 0, '01:15:25', '02:25:35', '03:35:45', '04:45:55');


INSERT INTO DNS2
VALUES('B4ZX', 'b www.example.com', 1, 1);


INSERT INTO SSDP2
VALUES('B5ZX', '239.255.255.250.1900', '1900', 'ssdp:all', 'ssdp:discover', 2);


INSERT INTO Sends
VALUES('Anas', 'A123');

INSERT INTO Receives
VALUES('Anas', 'A123');

INSERT INTO Creates
VALUES('Anas', 'B3ZX');

INSERT INTO Saves
VALUES('Anas', 'Ahmed');

INSERT INTO AutoSend
VALUES('A123', 20, '2021-10-26', '07:45:55', '172.16.0.9', '186.15.2.10', 'f4:d1:08:0f:84:12', 'c4:e9:0a:54:be:01', 'IPv4', 4, 'None', '0x0', 'None', 1, '', 0, 64, 'udp', 'None', '1.2.3.4', '1.2.3.4', 'None', 'domain', 'domain', 'None');

INSERT INTO AutoReceive
VALUES('A123', 20, 'NTP', '2021-10-10', '08:00:00', '172.16.0.9', '186.15.2.10', 40, 2);