CREATE DATABASE IF NOT EXISTS estoque;
USE estoque;
CREATE TABLE IF NOT EXISTS produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quantidade INT NOT NULL,
    nome_produto VARCHAR(255) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    categoria VARCHAR(255)
);

