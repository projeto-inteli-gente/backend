CREATE TABLE brazil_idh (
    year INTEGER NOT NULL,
    idh NUMERIC NOT NULL
);

CREATE TABLE region_idh (
    region_id INTEGER NOT NULL,
    year INTEGER NOT NULL,
    idh NUMERIC NOT NULL
);

CREATE TABLE state_idh (
    state_id INTEGER NOT NULL,
    year INTEGER NOT NULL,
    idh NUMERIC NOT NULL
);

CREATE TABLE city_idh (
    city_id INTEGER NOT NULL,
    year INTEGER NOT NULL,
    idh NUMERIC NOT NULL
);

INSERT INTO brazil_idh (year, idh) VALUES
(2020, 0.765),
(2021, 0.786),
(2022, 0.723);

INSERT INTO region_idh (region_id, year, idh) VALUES
(1, 2020, 0.720),
(1, 2021, 0.709),
(1, 2022, 0.729),

(2, 2020, 0.690),
(2, 2021, 0.700),
(2, 2022, 0.695),

(3, 2020, 0.690),
(3, 2021, 0.700),
(3, 2022, 0.695),

(4, 2020, 0.720),
(4, 2021, 0.709),
(4, 2022, 0.729),

(5, 2020, 0.720),
(5, 2021, 0.709),
(5, 2022, 0.729);

INSERT INTO state_idh (state_id, year, idh) VALUES
(1, 2020, 0.720),
(1, 2021, 0.709),
(1, 2022, 0.729),

(2, 2020, 0.690),
(2, 2021, 0.700),
(2, 2022, 0.695),

(3, 2020, 0.710),
(3, 2021, 0.715),
(3, 2022, 0.720),

(4, 2020, 0.730),
(4, 2021, 0.735),
(4, 2022, 0.740),

(5, 2020, 0.680),
(5, 2021, 0.685),
(5, 2022, 0.690),

(6, 2020, 0.705),
(6, 2021, 0.710),
(6, 2022, 0.715),

(7, 2020, 0.800),
(7, 2021, 0.805),
(7, 2022, 0.810),

(8, 2020, 0.790),
(8, 2021, 0.795),
(8, 2022, 0.800),

(9, 2020, 0.750),
(9, 2021, 0.755),
(9, 2022, 0.760),

(10, 2020, 0.670),
(10, 2021, 0.675),
(10, 2022, 0.680),

(11, 2020, 0.730),
(11, 2021, 0.735),
(11, 2022, 0.740),

(12, 2020, 0.740),
(12, 2021, 0.745),
(12, 2022, 0.750),

(13, 2020, 0.770),
(13, 2021, 0.775),
(13, 2022, 0.780),

(14, 2020, 0.710),
(14, 2021, 0.715),
(14, 2022, 0.720),

(15, 2020, 0.700),
(15, 2021, 0.705),
(15, 2022, 0.710),

(16, 2020, 0.750),
(16, 2021, 0.755),
(16, 2022, 0.760),

(17, 2020, 0.740),
(17, 2021, 0.745),
(17, 2022, 0.750),

(18, 2020, 0.680),
(18, 2021, 0.685),
(18, 2022, 0.690),

(19, 2020, 0.780),
(19, 2021, 0.785),
(19, 2022, 0.790),

(20, 2020, 0.720),
(20, 2021, 0.725),
(20, 2022, 0.730),

(21, 2020, 0.750),
(21, 2021, 0.755),
(21, 2022, 0.760),

(22, 2020, 0.710),
(22, 2021, 0.715),
(22, 2022, 0.720),

(23, 2020, 0.680),
(23, 2021, 0.685),
(23, 2022, 0.690),

(24, 2020, 0.780),
(24, 2021, 0.785),
(24, 2022, 0.790),

(25, 2020, 0.810),
(25, 2021, 0.815),
(25, 2022, 0.820),

(26, 2020, 0.760),
(26, 2021, 0.765),
(26, 2022, 0.770),

(27, 2020, 0.750),
(27, 2021, 0.755),
(27, 2022, 0.760);



INSERT INTO city_idh (city_id, year, idh) VALUES
(1, 2020, 0.720),
(1, 2021, 0.709),
(1, 2022, 0.729),

(2, 2020, 0.690),
(2, 2021, 0.700),
(2, 2022, 0.695),

(3, 2020, 0.710),
(3, 2021, 0.715),
(3, 2022, 0.720),

(4, 2020, 0.730),
(4, 2021, 0.735),
(4, 2022, 0.740),

(5, 2020, 0.680),
(5, 2021, 0.685),
(5, 2022, 0.690),

(6, 2020, 0.705),
(6, 2021, 0.710),
(6, 2022, 0.715),

(7, 2020, 0.800),
(7, 2021, 0.805),
(7, 2022, 0.810),

(8, 2020, 0.790),
(8, 2021, 0.795),
(8, 2022, 0.800),

(9, 2020, 0.750),
(9, 2021, 0.755),
(9, 2022, 0.760),

(10, 2020, 0.670),
(10, 2021, 0.675),
(10, 2022, 0.680),

(11, 2020, 0.730),
(11, 2021, 0.735),
(11, 2022, 0.740),

(12, 2020, 0.740),
(12, 2021, 0.745),
(12, 2022, 0.750),

(13, 2020, 0.770),
(13, 2021, 0.775),
(13, 2022, 0.780),

(14, 2020, 0.710),
(14, 2021, 0.715),
(14, 2022, 0.720),

(15, 2020, 0.700),
(15, 2021, 0.705),
(15, 2022, 0.710),

(16, 2020, 0.750),
(16, 2021, 0.755),
(16, 2022, 0.760),

(17, 2020, 0.740),
(17, 2021, 0.745),
(17, 2022, 0.750),

(18, 2020, 0.680),
(18, 2021, 0.685),
(18, 2022, 0.690),

(19, 2020, 0.780),
(19, 2021, 0.785),
(19, 2022, 0.790),

(20, 2020, 0.720),
(20, 2021, 0.725),
(20, 2022, 0.730),

(21, 2020, 0.750),
(21, 2021, 0.755),
(21, 2022, 0.760),

(22, 2020, 0.710),
(22, 2021, 0.715),
(22, 2022, 0.720),

(23, 2020, 0.680),
(23, 2021, 0.685),
(23, 2022, 0.690),

(24, 2020, 0.780),
(24, 2021, 0.785),
(24, 2022, 0.790),

(25, 2020, 0.810),
(25, 2021, 0.815),
(25, 2022, 0.820),

(26, 2020, 0.760),
(26, 2021, 0.765),
(26, 2022, 0.770),

(27, 2020, 0.750),
(27, 2021, 0.755),
(27, 2022, 0.760),

(28, 2020, 0.810),
(28, 2021, 0.815),
(28, 2022, 0.820),

(29, 2020, 0.760),
(29, 2021, 0.765),
(29, 2022, 0.770),

(30, 2020, 0.720),
(30, 2021, 0.725),
(30, 2022, 0.730),

(31, 2020, 0.750),
(31, 2021, 0.755),
(31, 2022, 0.760),

(32, 2020, 0.710),
(32, 2021, 0.715),
(32, 2022, 0.720),

(33, 2020, 0.680),
(33, 2021, 0.685),
(33, 2022, 0.690),

(34, 2020, 0.780),
(34, 2021, 0.785),
(34, 2022, 0.790),

(35, 2020, 0.810),
(35, 2021, 0.815),
(35, 2022, 0.820),

(36, 2020, 0.760),
(36, 2021, 0.765),
(36, 2022, 0.770),

(37, 2020, 0.750),
(37, 2021, 0.755),
(37, 2022, 0.760),

(38, 2020, 0.810),
(38, 2021, 0.815),
(38, 2022, 0.820),

(39, 2020, 0.760),
(39, 2021, 0.765),
(39, 2022, 0.770),

(40, 2020, 0.720),
(40, 2021, 0.725),
(40, 2022, 0.730),

(41, 2020, 0.750),
(41, 2021, 0.755),
(41, 2022, 0.760),

(42, 2020, 0.710),
(42, 2021, 0.715),
(42, 2022, 0.720),

(43, 2020, 0.680),
(43, 2021, 0.685),
(43, 2022, 0.690),

(44, 2020, 0.780),
(44, 2021, 0.785),
(44, 2022, 0.790),

(45, 2020, 0.810),
(45, 2021, 0.815),
(45, 2022, 0.820),

(46, 2020, 0.760),
(46, 2021, 0.765),
(46, 2022, 0.770),

(47, 2020, 0.750),
(47, 2021, 0.755),
(47, 2022, 0.760),

(48, 2020, 0.810),
(48, 2021, 0.815),
(48, 2022, 0.820),

(49, 2020, 0.760),
(49, 2021, 0.765),
(49, 2022, 0.770),

(50, 2020, 0.720),
(50, 2021, 0.725),
(50, 2022, 0.730),

(51, 2020, 0.750),
(51, 2021, 0.755),
(51, 2022, 0.760),

(52, 2020, 0.710),
(52, 2021, 0.715),
(52, 2022, 0.720),

(53, 2020, 0.680),
(53, 2021, 0.685),
(53, 2022, 0.690),

(54, 2020, 0.780),
(54, 2021, 0.785),
(54, 2022, 0.790),

(55, 2020, 0.810),
(55, 2021, 0.815),
(55, 2022, 0.820),

(56, 2020, 0.760),
(56, 2021, 0.765),
(56, 2022, 0.770),

(57, 2020, 0.750),
(57, 2021, 0.755),
(57, 2022, 0.760),

(58, 2020, 0.810),
(58, 2021, 0.815),
(58, 2022, 0.820),

(59, 2020, 0.760),
(59, 2021, 0.765),
(59, 2022, 0.770),

(60, 2020, 0.720),
(60, 2021, 0.725),
(60, 2022, 0.730),

(61, 2020, 0.750),
(61, 2021, 0.755),
(61, 2022, 0.760),

(62, 2020, 0.710),
(62, 2021, 0.715),
(62, 2022, 0.720),

(63, 2020, 0.680),
(63, 2021, 0.685),
(63, 2022, 0.690),

(64, 2020, 0.780),
(64, 2021, 0.785),
(64, 2022, 0.790),

(65, 2020, 0.810),
(65, 2021, 0.815),
(65, 2022, 0.820),

(66, 2020, 0.760),
(66, 2021, 0.765),
(66, 2022, 0.770),

(67, 2020, 0.750),
(67, 2021, 0.755),
(67, 2022, 0.760),

(68, 2020, 0.810),
(68, 2021, 0.815),
(68, 2022, 0.820),

(69, 2020, 0.760),
(69, 2021, 0.765),
(69, 2022, 0.770),

(70, 2020, 0.720),
(70, 2021, 0.725),
(70, 2022, 0.730),

(71, 2020, 0.750),
(71, 2021, 0.755),
(71, 2022, 0.760),

(72, 2020, 0.710),
(72, 2021, 0.715),
(72, 2022, 0.720),

(73, 2020, 0.680),
(73, 2021, 0.685),
(73, 2022, 0.690),

(74, 2020, 0.780),
(74, 2021, 0.785),
(74, 2022, 0.790),

(75, 2020, 0.810),
(75, 2021, 0.815),
(75, 2022, 0.820),

(76, 2020, 0.760),
(76, 2021, 0.765),
(76, 2022, 0.770),

(77, 2020, 0.750),
(77, 2021, 0.755),
(77, 2022, 0.760),

(78, 2020, 0.810),
(78, 2021, 0.815),
(78, 2022, 0.820),

(79, 2020, 0.760),
(79, 2021, 0.765),
(79, 2022, 0.770),

(80, 2020, 0.750),
(80, 2021, 0.755),
(80, 2022, 0.760),

(81, 2020, 0.810),
(81, 2021, 0.815),
(81, 2022, 0.820);
