SELECT id_comision, comision
FROM broker
WHERE comision > 1.99;

SELECT id_accion, precio_venta, precio_compra
FROM cotizacion
WHERE fecha_hora BETWEEN "24-10-20 0:0:0" AND now();

SELECT nombre_accion, simbolo_accion
FROM accion
WHERE nombre_accion LIKE "Y%";

SELECT MAX(valor_transaccion), MIN(valor_transaccion)
FROM transaccion
WHERE id_tipo_transaccion=1;

SELECT cuit_o_cuil, apellido, nombre, email
FROM inversor
ORDER BY apellido, nombre;

SELECT id_tipo_transaccion, SUM(valor_transaccion)
FROM transaccion
GROUP BY id_tipo_transaccion;

-- CONSULTAS MULTITABLAS

SELECT accion.nombre_accion, cotizacion.fecha_hora, cotizacion.precio_venta
FROM accion JOIN cotizacion
ON accion.id_accion = cotizacion.id_accion;

SELECT inversor.apellido, inversor.nombre, transaccion.cantidad_acciones_transaccion, transaccion.valor_transaccion
FROM inversor left JOIN transaccion
ON inversor.cuit_o_cuil = transaccion.cuit_o_cuil;

SELECT inversor.apellido, inversor.nombre, tipo_transaccion.tipo_transaccion, transaccion.valor_transaccion
FROM inversor  JOIN transaccion
ON inversor.cuit_o_cuil = transaccion.cuit_o_cuil
JOIN tipo_transaccion
ON transaccion.id_tipo_transaccion = tipo_transaccion.id_tipo_transaccion;

