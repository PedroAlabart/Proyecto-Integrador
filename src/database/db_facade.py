from sqlalchemy import text
from src.database.connector import DatabaseConnection
from src.database.query_builder import SQLQueryBuilder
from src.database.dataframe_prettifier import prettify_output
import pandas as pd

class DatabaseFacade:
    def __init__(self):
        self.db = DatabaseConnection()
    @prettify_output
    def execute_query(self, query_or_builder: str | SQLQueryBuilder):
        """
        Ejecuta una consulta SQL, ya sea construida manualmente como string
        o generada mediante SQLQueryBuilder.
        Se reconoce que esta función es vulnerable a inyecciones SQL; sin embargo, se prevé su uso exclusivamente en el entorno interno de la empresa.
        Args:
            query_or_builder (str | SQLQueryBuilder): Consulta SQL o builder.

        Returns:
            pd.DataFrame: Resultados formateados como DataFrame.
        """
        if isinstance(query_or_builder, SQLQueryBuilder):
            query = query_or_builder.build()
        else:
            query = query_or_builder

        with self.db.get_session() as session:
            engine = self.db.engine  # Obtener el engine SQLAlchemy
            # Si no tienes parámetros, no hace falta pasarlos
            return pd.read_sql(sql=text(query), con=engine)
