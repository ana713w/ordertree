import mysql
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()


class DatabaseConnection:
    
    def __init__(self):
        self.host = os.getenv("DB_HOST", "localhost")
        self.user = os.getenv("DB_USER", "root")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME", "music_api")
        self.mydb = None

    def get_connection(self):
        """
        Obtiene una conexión a la base de datos.
        Si no existe, la crea; si existe, la reutiliza.
        """
        try:
            if self.mydb is None:
                self.mydb = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
                )
                print("Conexión exitosa a la base de datos")
            return self.mydb
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            raise e

    def close_connection(self):
        """
        Cierra la conexión a la base de datos.
        """
        if self.mydb and self.mydb.is_connected():
            self.mydb.close()
            print("Conexión cerrada")


# Instancia global para reutilizar en toda la aplicación
db = DatabaseConnection()