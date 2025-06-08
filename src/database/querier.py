from src.database.querier_helper import (
    SelectClause,
    FromClause,
    WhereClause,
    OrderByClause,
    LimitClause
)

class SQLQueryBuilder:
    """
    Clase Builder para construir consultas SQL de forma fluida y modular.

    Utiliza objetos Clause especializados para encapsular cada parte de la consulta.

    Métodos encadenables permiten una experiencia DSL (Domain-Specific Language) limpia.
    """

    def __init__(self):
        """Inicializa los componentes de la consulta SQL."""
        self.select_clause = SelectClause()
        self.from_clause = FromClause()
        self.where_clause = WhereClause()
        self.order_by_clause = OrderByClause()
        self.limit_clause = LimitClause()

    def select(self, *columns):
        """
        Agrega columnas a la cláusula SELECT.

        Args:
            *columns: Lista de columnas a seleccionar (como strings).

        Returns:
            self: permite encadenamiento de métodos.
        """
        self.select_clause.add(*columns)
        return self

    def from_table(self, table_name: str):
        """
        Define la tabla fuente para la cláusula FROM.

        Args:
            table_name (str): Nombre de la tabla.

        Returns:
            self
        """
        self.from_clause.set(table_name)
        return self

    def where(self, condition: str):
        """
        Agrega una condición a la cláusula WHERE.

        Args:
            condition (str): Condición en formato SQL con placeholders (%s).
            *params: Parámetros que reemplazan los placeholders.

        Returns:
            self
        """
        self.where_clause.add(condition)
        return self

    def order_by(self, *columns):
        """
        Agrega columnas a la cláusula ORDER BY.

        Args:
            *columns: Columnas por las que se ordena la consulta.

        Returns:
            self
        """
        self.order_by_clause.add(*columns)
        return self

    def limit(self, n: int):
        """
        Limita la cantidad de resultados.

        Args:
            n (int): Número máximo de filas a devolver.

        Returns:
            self
        """
        self.limit_clause.set(n)
        return self

    def build(self) -> str:
        """
        Construye la consulta SQL final y los parámetros asociados.

        Returns:
            tuple:
                - query (str): Consulta SQL construida con placeholders.
                - params (list): Lista de valores para los placeholders.
        """
        # Construcción en orden correcto de cláusulas SQL
        query_parts = [
            self.select_clause.build(),
            self.from_clause.build(),
            self.where_clause.build(),
            self.order_by_clause.build(),
            self.limit_clause.build(),
        ]

        # Se filtran cláusulas vacías y se concatenan
        query = " ".join(filter(None, query_parts)) + ";"

        # Se obtienen los parámetros de la cláusula WHERE
        return query

