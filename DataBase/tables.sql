use applicationhesabdari;

CREATE TABLE accessories (
    systemId INT NOT NULL AUTO_INCREMENT,
    ID VARCHAR(255) NOT NULL,
    category VARCHAR(255),
    model VARCHAR(255),
    quantity INT,
    buy BIGINT,
    `date` date,
    PRIMARY KEY (systemId)
);
-- _label   , _input  

CREATE TABLE phones (
    systemId INT NOT NULL AUTO_INCREMENT,
    ID VARCHAR(255) NOT NULL,
    brand VARCHAR(255),
    model VARCHAR(255),
    quantity INT,
    buy BIGINT,
    `date` date,
    PRIMARY KEY (systemId)
);

CREATE TABLE watchs (
    systemId INT NOT NULL AUTO_INCREMENT,
    ID VARCHAR(255) NOT NULL,
    category VARCHAR(255),
    model VARCHAR(255),
    quantity INT,
    buy BIGINT,
    `date` date,
    PRIMARY KEY (systemId)
);

CREATE TABLE airpods (
    systemId INT NOT NULL AUTO_INCREMENT,
    ID VARCHAR(255) NOT NULL,
    category VARCHAR(255),
    model VARCHAR(255),
    quantity INT,
    buy BIGINT,
    `date` date,
    PRIMARY KEY (systemId)
);

CREATE TABLE speaker_and_headsets (
    systemId INT NOT NULL AUTO_INCREMENT,
    ID VARCHAR(255) NOT NULL,
    category VARCHAR(255),
    model VARCHAR(255),
    quantity INT,
    buy BIGINT,
    `date` date,
    PRIMARY KEY (systemId)
);

CREATE TABLE electrical_tools (
    systemId INT NOT NULL AUTO_INCREMENT,
    ID VARCHAR(255) NOT NULL,
    category VARCHAR(255),
    model VARCHAR(255),
    quantity INT,
    buy BIGINT,
    `date` date,
    PRIMARY KEY (systemId)
);

CREATE TABLE sales (
    systemId INT NOT NULL AUTO_INCREMENT,
    ID VARCHAR(255) NOT NULL,
    price BIGINT,
    `date` date,
    PRIMARY KEY (systemId)
);

create table cheques (
	systemId INT NOT NULL AUTO_INCREMENT,
	`date` date not null,
    amount bigint,
    target varchar(255),
    status varchar(255),
    PRIMARY KEY (systemId)
);

create table in_outs(
	systemId INT NOT NULL AUTO_INCREMENT,
    ID varchar(255),
    status varchar(255),
    price bigint,
    `date` date,
    PRIMARY KEY (systemId)
);

create table sellers_info(
	name varchar(255),
    price bigint,
    `date` datetime
);
