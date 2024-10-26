use brokercba;

INSERT INTO accion (nombre_accion, simbolo_accion)
VALUES ( "Yacimientos", "YPF"),
		("Aceitera", "AGD"),
        ("ArcorArgentina", "ARCOR"),
        ("Google", "GOO");

INSERT INTO cotizacion (id_accion, fecha_hora, precio_venta, precio_compra)
VALUES (1,"2024-10-20 15:20:09.000000", 1.79, 1,89),
		(1, "2024-10-20 10:04:12.000000",	1.09,	1.18),
		(3,	"2024-10-20 10:04:27.000000",	1.09,	1.18),
		(3,	"2024-10-20 10:36:04.000000",	1.29,	1.38),
		(2,	"2024-10-20 10:36:29.000000",	2.29,	2.3),
		(4,	"2024-10-19 10:20:29.000000",	1.3,	1.50);


INSERT INTO inversor (id_tipo_inversor, cuit_o_cuil, nombre, apellido, email, contrasena, fecha_alta_inversor, saldo_inicial)
VALUES (1, "27217183974", "Mariela", "Suarez", "marielarosa@gmail.com", "Hola567*", "15/9/24", 1000000),
		(0, "20112223338", "Estela", "Cáceres", "caceres.estela@gmail.com", "Yo$567pp", "19/9/24", 1000000),
        (0, "20999999990", "Juan Pablo", "Rodriguez", "juanpi@gmail.com", "JProdr#23", "10/10/24", 1000000);
-----
        
INSERT INTO tipo_inversor ( id_tipo_inversor, tipo_inversor)
VALUES ( 0, "Física"),
		(1, "Jurídica");
        
INSERT INTO tipo_transaccion ( tipo_transaccion)
VALUES ( "Compra"),
		( "Venta");
        

INSERT INTO transaccion ( id_tipo_transaccion, cuit_o_cuil, id_cotizacion_accion, cantidad_acciones_transaccion, fecha_hora_transaccion, valor_transaccion)
VALUES ( 1, "27217183974", 2 , 5, "24/10/20 23:56:0", 1.09 ),
		( 2, "27217183974", 3 , 5, "24/10/20 19:56:0", 1.38 ),
         (1, "20112223338", 2 , 15, "24/10/21 23:56:0", 1.09 );
		
INSERT INTO broker ( id_num_transaccion, comision)
VALUES ( 1, 1.64),
		(2, 1.09),
        (3, 1.38),
        (4, 3.27);
	
        
SELECT * FROM transaccion;