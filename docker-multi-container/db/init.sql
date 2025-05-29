CREATE DATABASE IF NOT EXISTS userdb;
USE userdb;

DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255),
    gender ENUM('Male', 'Female', 'Other'),
    profession VARCHAR(100),
    country VARCHAR(100)
);
