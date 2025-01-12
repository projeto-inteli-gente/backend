-- Dados MOC para testes do backend

CREATE TABLE region (
    id SERIAL PRIMARY KEY,
    name VARCHAR(15) NOT NULL
);

CREATE TABLE state (
    id SERIAL PRIMARY KEY,
    name VARCHAR(2) NOT NULL,
    region_id INTEGER NOT NULL
);

CREATE TABLE city (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    state_id INTEGER NOT NULL,
    region_id INTEGER NOT NULL
);

INSERT INTO region (id, name) VALUES
(1, 'Norte'),
(2, 'Nordeste'),
(3, 'Centro-Oeste'),
(4, 'Sudeste'),
(5, 'Sul');

INSERT INTO state (id, name, region_id) VALUES
(1, 'AC', 1),
(2, 'AL', 2),
(3, 'AP', 1),
(4, 'AM', 1),
(5, 'BA', 2),
(6, 'CE', 2),
(7, 'DF', 3),
(8, 'ES', 4),
(9, 'GO', 3),
(10, 'MA', 2),
(11, 'MT', 3),
(12, 'MS', 3),
(13, 'MG', 4),
(14, 'PA', 1),
(15, 'PB', 2),
(16, 'PR', 5),
(17, 'PE', 2),
(18, 'PI', 2),
(19, 'RJ', 4),
(20, 'RN', 2),
(21, 'RS', 5),
(22, 'RO', 1),
(23, 'RR', 1),
(24, 'SC', 5),
(25, 'SP', 4),
(26, 'SE', 2),
(27, 'TO', 1);


INSERT INTO city (name, state_id, region_id) VALUES
-- Norte
('Rio Branco', 1, 1),
('Cruzeiro do Sul', 1, 1),
('Sena Madureira', 1, 1),

('Macapá', 3, 1),
('Santana', 3, 1),
('Oiapoque', 3, 1),

('Manaus', 4, 1),
('Parintins', 4, 1),
('Itacoatiara', 4, 1),

('Belém', 14, 1),
('Santarém', 14, 1),
('Marabá', 14, 1),

('Porto Velho', 22, 1),
('Ji-Paraná', 22, 1),
('Ariquemes', 22, 1),

('Boa Vista', 23, 1),
('Rorainópolis', 23, 1),
('Caracaraí', 23, 1),

('Palmas', 27, 1),
('Araguaína', 27, 1),
('Gurupi', 27, 1),

-- Nordeste
('Maceió', 2, 2),
('Arapiraca', 2, 2),
('Palmeira dos Índios', 2, 2),

('Salvador', 5, 2),
('Feira de Santana', 5, 2),
('Vitória da Conquista', 5, 2),

('Fortaleza', 6, 2),
('Juazeiro do Norte', 6, 2),
('Sobral', 6, 2),

('São Luís', 10, 2),
('Imperatriz', 10, 2),
('Caxias', 10, 2),

('João Pessoa', 15, 2),
('Campina Grande', 15, 2),
('Patos', 15, 2),

('Recife', 17, 2),
('Olinda', 17, 2),
('Caruaru', 17, 2),

('Teresina', 18, 2),
('Parnaíba', 18, 2),
('Picos', 18, 2),

('Natal', 20, 2),
('Mossoró', 20, 2),
('Parnamirim', 20, 2),

('Aracaju', 26, 2),
('Nossa Senhora do Socorro', 26, 2),
('Lagarto', 26, 2),

-- Centro-Oeste
('Brasília', 7, 3),
('Ceilândia', 7, 3),
('Taguatinga', 7, 3),

('Goiânia', 9, 3),
('Aparecida de Goiânia', 9, 3),
('Anápolis', 9, 3),

('Cuiabá', 11, 3),
('Várzea Grande', 11, 3),
('Rondonópolis', 11, 3),

('Campo Grande', 12, 3),
('Dourados', 12, 3),
('Três Lagoas', 12, 3),

-- Sudeste
('Belo Horizonte', 13, 4),
('Uberlândia', 13, 4),
('Contagem', 13, 4),

('Vitória', 8, 4),
('Vila Velha', 8, 4),
('Serra', 8, 4),

('São Paulo', 25, 4),
('Campinas', 25, 4),
('Santos', 25, 4),

('Rio de Janeiro', 19, 4),
('Niterói', 19, 4),
('Petrópolis', 19, 4),

-- Sul
('Curitiba', 16, 5),
('Londrina', 16, 5),
('Maringá', 16, 5),

('Porto Alegre', 21, 5),
('Caxias do Sul', 21, 5),
('Pelotas', 21, 5),

('Florianópolis', 24, 5),
('Joinville', 24, 5),
('Blumenau', 24, 5);