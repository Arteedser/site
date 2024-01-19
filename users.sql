DROP DATABASE IF EXISTS users;
CREATE DATABASE IF NOT EXISTS users;

USE users;

DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users;
(
    id INT auto_increment PRIMARY KEY,
    email VARCHAR(45) NOT NULL,
    hash_psswd VARCHAR(200) NOT NULL,
    CONSTRAINT email
);

INSERT INTO users.users (id, email, hash_psswd) VALUES (3, 'ruslan020507@gmail.com', 'scrypt:32768:8:1$B7W75Lm2liPgRpuf$858f288b6cf6afedf4d829cc9e8f9f0a623210353c4e765b223bac59948a72f66d13708e92dc5c5c88f9f123f1bdf6c3b659cee3cc83fe481f71e21c5c857e77');
INSERT INTO users.users (id, email, hash_psswd) VALUES (4, 'rusik1486@gmail.com', 'scrypt:32768:8:1$GRZ9ikWWrm1Jd8lZ$8b076f21937cea315612cf0b7a8bc0d97ad631a359e364dc4a94c541d51d918221bea6960e0ee843275876c20ff783203a578443227245d7f54f803d84dd89a2');
