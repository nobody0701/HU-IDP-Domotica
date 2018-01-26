DROP TABLE IF EXISTS meldingen CASCADE;
DROP TABLE IF EXISTS gordijnen CASCADE;
DROP TABLE IF EXISTS stofzuiger CASCADE;
DROP TABLE IF EXISTS kamer CASCADE;

CREATE TABLE kamer (
kamerid int4 NOT NULL, 
naambewoner varchar(255) NOT NULL, 
kamernr int4 NOT NULL, 
PRIMARY KEY (kamerid, naambewoner));

CREATE TABLE gordijnen (
kamerid int4 NOT NULL,  
opentijd time NOT NULL,
sluittijd time NOT NULL,
gordijnopen varchar(3) NOT NULL);

CREATE TABLE stofzuiger (
kamerid int4 NOT NULL, 
starttijd time NOT NULL,
stoptijd time NOT NULL, 
actief varchar(3) NOT NULL);

CREATE TABLE alarm (
kamerid int4 NOT NULL, 
starttijd time NOT NULL,
stoptijd time NOT NULL, 
actief varchar(3) NOT NULL);

CREATE TABLE meldingen (
kamerid int4 NOT NULL, 
meldingtekst varchar(255) NOT NULL);

INSERT INTO kamer(kamerid, naambewoner, kamernr) VALUES (1, 'Bram' , 101);
INSERT INTO meldingen(kamerid, meldingtekst) VALUES (1, 'help');
INSERT INTO gordijnen(kamerid, opentijd, sluittijd, gordijnopen) VALUES (1, '08:30', '22:00', 'ja');
INSERT INTO stofzuiger(kamerid, starttijd, stoptijd, actief) VALUES (1, '12:30', '13:00', 'ja');
INSERT INTO alarm(kamerid, starttijd, stoptijd, actief) VALUES (1, '22:00', '08:00', 'ja');