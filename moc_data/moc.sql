-- Dados MOC para testes do backend

CREATE TABLE regions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

INSERT INTO regions (name) VALUES
('Norte'),
('Nordeste'),
('Centro-Oeste'),
('Sudeste'),
('Sul');

CREATE TABLE states (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    region VARCHAR(50) NOT NULL
);

INSERT INTO states (name, region) VALUES
('Acre', 'norte'),
('Alagoas', 'nordeste'),
('Amapá', 'norte'),
('Amazonas', 'norte'),
('Bahia', 'nordeste'),
('Ceará', 'nordeste'),
('Distrito Federal', 'centro-oeste'),
('Espírito Santo', 'sudeste'),
('Goiás', 'centro-oeste'),
('Maranhão', 'nordeste'),
('Mato Grosso', 'centro-oeste'),
('Mato Grosso do Sul', 'centro-oeste'),
('Minas Gerais', 'sudeste'),
('Pará', 'norte'),
('Paraíba', 'nordeste'),
('Paraná', 'sul'),
('Pernambuco', 'nordeste'),
('Piauí', 'nordeste'),
('Rio de Janeiro', 'sudeste'),
('Rio Grande do norte', 'nordeste'),
('Rio Grande do Sul', 'sul'),
('Rondônia', 'norte'),
('Roraima', 'norte'),
('Santa Catarina', 'sul'),
('São Paulo', 'sudeste'),
('Sergipe', 'nordeste'),
('Tocantins', 'norte');
