-- Inserting dummy data into tables Using Procedures
--

CALL insUser('Anas2', 'anas123@hotmail.com', '3a42c503953909637f7');

CALL insContacts('Ahmed2', '217.164.55.113');

CALL insSent('A1234', 20, '2021-10-26', '07:45:55', '172.16.0.9', '186.15.2.10', 'f4:d1:08:0f:84:12', 'c4:e9:0a:54:be:01', 'IPv4', 4, 'None', '0x0', 'None', 1, '', 0, 64, 'udp', 'None', '1.2.3.4', '1.2.3.4', 'None', 'domain', 'domain', 'None');
CALL insSent('A4567', 20, '2021-10-26', '07:45:55', '172.16.0.9', '186.15.2.10', 'f4:d1:08:0f:84:12', 'c4:e9:0a:54:be:01', 'IPv4', 4, 'None', '0x0', 'None', 1, '', 0, 64, 'udp', 'None', '1.2.3.4', '1.2.3.4', 'None', 'domain', 'domain', 'None');
CALL insSent('A7899', 20, '2021-10-26', '07:45:55', '172.16.0.9', '186.15.2.10', 'f4:d1:08:0f:84:12', 'c4:e9:0a:54:be:01', 'IPv4', 4, 'None', '0x0', 'None', 1, '', 0, 64, 'udp', 'None', '1.2.3.4', '1.2.3.4', 'None', 'domain', 'domain', 'None');

CALL insNTP('A1234', 61, 4, 'client', 2, 10, 0, 0, 0, '127.0.0.1', 0, '01:15:25', '02:25:35', '03:35:45', '04:45:55');

CALL insDNS('A4567', 'b www.example.com', 'A', 'IN');

CALL insSSDP('A7899', '239.255.255.250.1900', '1900', 'ssdp:all', 2, 'ssdp:discover');

CALL insReceived('A1234', 20, 'NTP', '2021-10-10', '08:00:00', '172.16.0.9', '186.15.2.10', 40, 2, '');

CALL insDrafts('B33ZX', '2021-10-10', '07:45:55', 'f4:d1:08:0f:84:12', 'c4:e9:0a:54:be:01', 'IPv4', 4, 'None', '0x0', 'None', 1, '', 0, 64, 'udp', 'None', '1.2.3.4', '1.2.3.4', 'None', 'domain', 'domain', 'None', 'ntp', 60);
CALL insDrafts('B44ZX', '2021-10-10', '07:45:55', 'f4:d1:08:0f:84:12', 'c4:e9:0a:54:be:01', 'IPv4', 4, 'None', '0x0', 'None', 1, '', 0, 64, 'udp', 'None', '1.2.3.4', '1.2.3.4', 'None', 'domain', 'domain', 'None', 'dns', 61);
CALL insDrafts('B55ZX', '2021-10-10', '07:45:55', 'f4:d1:08:0f:84:12', 'c4:e9:0a:54:be:01', 'IPv4', 4, 'None', '0x0', 'None', 1, '', 0, 64, 'udp', 'None', '1.2.3.4', '1.2.3.4', 'None', 'domain', 'domain', 'None', 'ssdp', 62);

CALL insNTP2('B33ZX', 61, 4, 'client', 2, 10, 0, 0, 0, '127.0.0.1', 0, '01:15:25', '02:25:35', '03:35:45', '04:45:55');

CALL insDNS2('B44ZX', 'b www.example.com', 'A', 'IN');

CALL insSSDP2('B55ZX', '239.255.255.250.1900', '1900', 'ssdp:all', 2, 'ssdp:discover');

CALL insSends('Anas2', 'A1234');

CALL insReceives('Anas2', 'A1234');

CALL insCreates('Anas2', 'B33ZX');

CALL insSaves('Anas2', 'Ahmed2');



