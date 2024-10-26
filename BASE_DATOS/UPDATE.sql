USE brokercba;

UPDATE cotizacion
SET precio_venta=1.19, precio_compra=1.15
WHERE id_cotizacion_accion=2;

UPDATE inversor
SET nombre="Stella"
WHERE cuit_o_cuil="20112223338";

UPDATE inversor
SET fecha_alta_inversor="24-10-10"
WHERE cuit_o_cuil="20999999990";

UPDATE transaccion
SET cantidad_accion=8
WHERE id_transaccion=3;

UPDATE transaccion
SET valor_transaccion=1.65
WHERE cuit_o_cuil=2721718397 AND id_cotizacion_accion=2;