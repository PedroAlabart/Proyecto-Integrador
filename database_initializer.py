import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    port=3306,
    user = "root", #Cambialo en venv
    password = "ABCD1234", # Cambialo en variables de entorno
      database="db" #Cambialo a un nombre mas especifico
)


if __name__ == '__main__':
    pass