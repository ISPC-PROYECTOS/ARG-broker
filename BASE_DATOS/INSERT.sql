use brokercba;

INSERT INTO accion (nombre_accion, simbolo_accion) VALUES
('YPF Sociedad Anónima', 'YPF'),
('Banco Macro S.A.', 'BMA'),
('Grupo Financiero Galicia S.A.', 'GGAL'),
('Transportadora de Gas del Sur S.A.', 'TGSU2'),
('Aluar Aluminio Argentino S.A.I.C.', 'ALUA'),
('Pampa Energía S.A.', 'PAMP'),
('Telecom Argentina S.A.', 'TEO'),
('Cresud S.A.C.I.F. y A.', 'CRES'),
('Molinos Río de la Plata S.A.', 'MOLI'),
('Edenor S.A.', 'EDN');

INSERT INTO cotizacion (id_accion, fecha_hora, precio_venta, precio_compra, cantidad_disponible) VALUES
(1, '2024-10-20 14:30:00.000000', 120.5, 118.75, 10),
(2, '2024-10-20 14:30:00.000000', 340.2, 335.8, 2),
(3, '2024-10-20 14:30:00.000000', 75.3, 74.5, 25),
(4, '2024-10-20 14:30:00.000000', 245, 242.8, 13),
(5, '2024-10-20 14:30:00.000000', 35.7, 34.9, 37),
(6, '2024-10-20 14:30:00.000000', 600.4, 595, 50),
(7, '2024-10-20 14:30:00.000000', 110.1, 108.75, 4),
(8, '2024-10-20 14:30:00.000000', 220.65, 218.9, 14),
(9, '2024-10-20 14:30:00.000000', 520, 515.3, 16),
(10, '2024-10-20 14:30:00.000000', 85.5, 83.9, 100);


INSERT INTO inversor (id_tipo_inversor, cuit_o_cuil, nombre, apellido, email, contrasena, fecha_alta_inversor, saldo_inicial) VALUES
(1, '12345678910', 'Fernando', 'Caballero', 'fer@gmail.com', 'Fer1234!', '2024-10-20', 1000000),
(0, '20123456789', 'Damian', 'Delgado', 'damian@gmail.com', 'Damian!87', '2024-10-20', 1000000),
(1, '20555555553', 'Roberto', 'Ramirez', 'robertito@gmail.com', 'Tito4321!', '2024-10-27', 1000000),
(1, '27010101013', 'Pablo', 'Perez', 'pablito@gmail.com', 'Pablo123!', '2024-10-27', 1000000),
(0, '27123456780', 'Pedro', 'Juarez', 'pepe@gmail.com', 'Pepe123!', '2024-10-17', 1000000),
(1, '27123456789', 'Hebe', 'Pereyra', 'hebepereyra@gmail.com', 'Hebep!33', '2024-10-18', 1000000),
(0, '27134574289', 'Adriana', 'Moral', 'agmoral@gmail.com', 'Agmoral!57', '2024-10-17', 1000000),
(1, '27395460094', 'Victoria', 'Picco', 'vpicco@gmail.com', 'Vicki37!', '2024-10-17', 1000000),
(0, '27541927420', 'Magdalena', 'Picco', 'magda@gmail.com', 'Magda16!', '2024-10-17', 1000000);
        
INSERT INTO tipo_inversor ( id_tipo_inversor, tipo_inversor)
VALUES ( 0, "Física"),
		(1, "Jurídica");
        
INSERT INTO tipo_transaccion ( tipo_transaccion)
VALUES ("Compra"),
		("Venta");
        
INSERT INTO transaccion (id_tipo_transaccion, cuit_o_cuil, id_cotizacion_accion, cantidad_acciones_transaccion, fecha_hora_transaccion, valor_transaccion) VALUES
(1, '12345678910', 1, 100, '2024-10-20 10:00:00.000000', -12000),
(2, '20123456789', 2, 50, '2024-10-20 10:15:00.000000', 17000),
(1, '27123456780', 3, 200, '2024-10-20 10:30:00.000000', -14500),
(2, '27123456789', 4, 75, '2024-10-20 10:45:00.000000', 18500),
(1, '27134574289', 5, 30, '2024-10-20 11:00:00.000000', -15000),
(2, '27395460094', 6, 120, '2024-10-20 11:15:00.000000', 10800),
(1, '27395460094', 7, 80, '2024-10-20 11:30:00.000000', -8500);
		
INSERT INTO broker ( id_num_transaccion, comision)
VALUES ( 1, 1.64),
		(2, 1.09),
        (3, 1.38),
        (4, 3.27);