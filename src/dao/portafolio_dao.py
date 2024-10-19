#en construccion
import mysql.connector
from mysql.connector import errorcode
from interface_dao import DataAccessDAO
from models.portafolio_model import Portafolio

class PortafolioDAO(DataAccessDAO):
    def __init__(sefl,db_conn:brokercba):
        self.__db_conn=db_conn.connect_to_mysql() #ver nombre del conector
        self.__db_name=db_conn.get_data_base_name()

    def obtener(self,cuit_o_cuil) -> Portafolio:
        with self.__connect_to_mysql() as conn:
            try: 
                cursor=conn.cursor()
                query= f"SELECT id_num_transaccion,id_tipo_transaccion,cuit_o_cuil,\
                          id_cotizacion_accion,cantidad_acciones_transaccion,\
                            fecha_hora_transaccion,valor_transaccion FROM \
                                {self.__bd_name}.transaccion WHERE cuit_o_cuil= %s"
                
                cursor.execute(query,(cuit_o_cuil,))
                row=cursor.fetchone()
                if row:
                    return Portafolio(row [0],row[1],row[2],row[3],row [4],row[5],row[6])
                return None
            except mysql.connector.Error as error:
                raise error

    def calcular_saldo_cuenta(self,cuit_o_cuil):
        with self.__connect_to_mysql() as conn:
            try: 
                cursor=conn.cursor()
                query= f"SELECT SUM(valor_transaccion) FROM \
                                {self.__bd_name}.transaccion WHERE cuit_o_cuil= %s"
                
                                
                cursor.execute(query,(cuit_o_cuil,))
                row=cursor.fetchone()
                if row:
                    return Portafolio(row [0])
                    saldo_inicial=1000000

                  
                return None
            except mysql.connector.Error as error:
                raise error     
    
