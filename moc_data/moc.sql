-- Dados MOC para testes do backend

CREATE TABLE region (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE state (
    id SERIAL PRIMARY KEY,
    name VARCHAR(2) NOT NULL,
    region VARCHAR(50) NOT NULL
);

CREATE TABLE city (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    state VARCHAR(2) NOT NULL,
    region VARCHAR(50) NOT NULL
);

INSERT INTO region (name) VALUES
('norte'),
('nordeste'),
('centro-oeste'),
('sudeste'),
('sul');

INSERT INTO state (name, region) VALUES
('AC', 'norte'),
('AL', 'nordeste'),
('AP', 'norte'),
('AM', 'norte'),
('BA', 'nordeste'),
('CE', 'nordeste'),
('DF', 'centro-oeste'),
('ES', 'sudeste'),
('GO', 'centro-oeste'),
('MA', 'nordeste'),
('MT', 'centro-oeste'),
('MS', 'centro-oeste'),
('MG', 'sudeste'),
('PA', 'norte'),
('PB', 'nordeste'),
('PR', 'sul'),
('PE', 'nordeste'),
('PI', 'nordeste'),
('RJ', 'sudeste'),
('RN', 'nordeste'),
('RS', 'sul'),
('RO', 'norte'),
('RR', 'norte'),
('SC', 'sul'),
('SP', 'sudeste'),
('SE', 'nordeste'),
('TO', 'norte');


INSERT INTO city (name, state, region) VALUES
-- norte
('Rio Branco', 'AC', 'norte'),
('Cruzeiro do Sul', 'AC', 'norte'),
('Sena Madureira', 'AC', 'norte'),

('Macapá', 'AP', 'norte'),
('Santana', 'AP', 'norte'),
('Oiapoque', 'AP', 'norte'),

('Manaus', 'AM', 'norte'),
('Parintins', 'AM', 'norte'),
('Itacoatiara', 'AM', 'norte'),

('Belém', 'PA', 'norte'),
('Santarém', 'PA', 'norte'),
('Marabá', 'PA', 'norte'),

('Porto Velho', 'RO', 'norte'),
('Ji-Paraná', 'RO', 'norte'),
('Ariquemes', 'RO', 'norte'),

('Boa Vista', 'RR', 'norte'),
('Rorainópolis', 'RR', 'norte'),
('Caracaraí', 'RR', 'norte'),

('Palmas', 'TO', 'norte'),
('Araguaína', 'TO', 'norte'),
('Gurupi', 'TO', 'norte'),

-- nordeste
('Maceió', 'AL', 'nordeste'),
('Arapiraca', 'AL', 'nordeste'),
('Palmeira dos Índios', 'AL', 'nordeste'),

('Salvador', 'BA', 'nordeste'),
('Feira de Santana', 'BA', 'nordeste'),
('Vitória da Conquista', 'BA', 'nordeste'),

('Fortaleza', 'CE', 'nordeste'),
('Juazeiro do Norte', 'CE', 'nordeste'),
('Sobral', 'CE', 'nordeste'),

('São Luís', 'MA', 'nordeste'),
('Imperatriz', 'MA', 'nordeste'),
('Caxias', 'MA', 'nordeste'),

('João Pessoa', 'PB', 'nordeste'),
('Campina Grande', 'PB', 'nordeste'),
('Patos', 'PB', 'nordeste'),

('Recife', 'PE', 'nordeste'),
('Olinda', 'PE', 'nordeste'),
('Caruaru', 'PE', 'nordeste'),

('Teresina', 'PI', 'nordeste'),
('Parnaíba', 'PI', 'nordeste'),
('Picos', 'PI', 'nordeste'),

('Natal', 'RN', 'nordeste'),
('Mossoró', 'RN', 'nordeste'),
('Parnamirim', 'RN', 'nordeste'),

('Aracaju', 'SE', 'nordeste'),
('Nossa Senhora do Socorro', 'SE', 'nordeste'),
('Lagarto', 'SE', 'nordeste'),

-- centro-oeste
('Brasília', 'DF', 'centro-oeste'),
('Ceilândia', 'DF', 'centro-oeste'),
('Taguatinga', 'DF', 'centro-oeste'),

('Goiânia', 'GO', 'centro-oeste'),
('Aparecida de Goiânia', 'GO', 'centro-oeste'),
('Anápolis', 'GO', 'centro-oeste'),

('Cuiabá', 'MT', 'centro-oeste'),
('Várzea Grande', 'MT', 'centro-oeste'),
('Rondonópolis', 'MT', 'centro-oeste'),

('Campo Grande', 'MS', 'centro-oeste'),
('Dourados', 'MS', 'centro-oeste'),
('Três Lagoas', 'MS', 'centro-oeste'),

-- sudeste
('Belo Horizonte', 'MG', 'sudeste'),
('Uberlândia', 'MG', 'sudeste'),
('Contagem', 'MG', 'sudeste'),

('Vitória', 'ES', 'sudeste'),
('Vila Velha', 'ES', 'sudeste'),
('Serra', 'ES', 'sudeste'),

('São Paulo', 'SP', 'sudeste'),
('Campinas', 'SP', 'sudeste'),
('Santos', 'SP', 'sudeste'),

('Rio de Janeiro', 'RJ', 'sudeste'),
('Niterói', 'RJ', 'sudeste'),
('Petrópolis', 'RJ', 'sudeste'),

-- sul
('Curitiba', 'PR', 'sul'),
('Londrina', 'PR', 'sul'),
('Maringá', 'PR', 'sul'),

('Porto Alegre', 'RS', 'sul'),
('Caxias do Sul', 'RS', 'sul'),
('Pelotas', 'RS', 'sul'),

('Florianópolis', 'SC', 'sul'),
('Joinville', 'SC', 'sul'),
('Blumenau', 'SC', 'sul');
