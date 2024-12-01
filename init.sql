CREATE DATABASE IF NOT EXISTS estoque;
USE estoque;
CREATE TABLE IF NOT EXISTS produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quantidade INT NOT NULL,
    nome_produto VARCHAR(255) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    categoria VARCHAR(255) NOT NULL
);

INSERT INTO produtos (quantidade, nome_produto, preco, categoria) VALUES
(50, 'Cimento Portland 50kg', 35.00, 'Cimentos'),
(100, 'Areia Fina', 15.00, 'Areia'),
(80, 'Bloco Cerâmico 39x19x14', 3.50, 'Blocos'),
(200, 'Tinta Látex Acrílica 18L', 120.00, 'Tintas'),
(150, 'Parafuso 3x25mm', 1.20, 'Ferragens'),
(60, 'Cadeira de Alumínio', 80.00, 'Móveis'),
(40, 'Piso Cerâmico 40x40cm', 35.00, 'Pisos e Revestimentos'),
(100, 'Cabo Elétrico 2,5mm', 2.50, 'Elétrica'),
(30, 'Tábua de Madeira 2x20cm', 10.00, 'Madeiras'),
(20, 'Tubulação PVC 25mm', 5.00, 'Tubos e Conexões');

