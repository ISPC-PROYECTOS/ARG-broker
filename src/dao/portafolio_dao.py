"""
#en construccion
import mysql.connector
from mysql.connector import errorcode
from interface_dao import DataAccessDAO
from models.portafolio_model import Portafolio

class PortafolioDAO(DataAccessDAO):

    def get(self,id:int) -> Portafolio:
        with self.__connect_to_mysql() as conn:
            try: 
                cursor=conn.cursor()
                    query=""
                
                cursor.execute(query,(id,))
                row=cursor.fetchone()
                if row:
                    return Portafolio(row [0],row[1],row[2],row[3])
                return None
            except mysql.connector.Error as error:
                raise error

"""