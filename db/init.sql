-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS dbsecurity CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Use the database
USE dbsecurity;

-- Create user table
CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    lastname VARCHAR(100),
    nickname VARCHAR(50),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    country_code VARCHAR(6),
    phone_number VARCHAR(20),
    country VARCHAR(100),
    profile_photo LONGBLOB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


CREATE TABLE revoked_token_jti (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    jti VARCHAR(128) NOT NULL,
    exp TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY (jti),
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
);

CREATE TABLE login_attempts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    failed_attempts INT DEFAULT 0,
    last_failed_at TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
);
