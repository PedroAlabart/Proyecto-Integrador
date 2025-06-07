from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import pandas as pd
from src.logger.logger import LoggerFactory

from decouple import config
from src.database.db_querier import QueryBuilder, WhereClause

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._initialize_engine()
        return cls._instance

    def _initialize_engine(self):
        user = config("DB_USER")
        password = config("DB_PASSWORD")
        host = config("DB_HOST")
        port = config("DB_PORT")
        db = config("DB_NAME")

        connection_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
        self.engine: Engine = create_engine(connection_url,
                                            pool_pre_ping=True, # Create Engine tiene lazy instiation. El atributo pool_pre_ping hace un ping para ver que la db funciona
                                            echo=True #Activa un log mas completo
                                            )
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()
    def query(self, query, param):
        with self.get_session() as session: #El with se asegura que la conexion se cierre al finalizar la query
            result = session.execute(text(query), param)
            return self.prettify_to_dataframe(result)

    def prettify_to_dataframe(self, result):
        print(pd.DataFrame.from_records(result))
        return 



# log = LoggerFactory.get_logger(name="main")
# db = DatabaseConnection()


# # Crear cláusulas WHERE seguras
# cl1 = WhereClause("TotalPrice", ">=", 18)

# # Armar el query
# builder = QueryBuilder()
# query, params = (
#     builder
#     .select_table("sales")
#     .select_columns("SalesPerson", "SalesID", "Quantity")
#     .add_where_clause(cl1)
#     .build()
# )

# print(query)
# print(params)
# db.query(query, params)