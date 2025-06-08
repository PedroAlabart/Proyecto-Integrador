from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class Clause(ABC):
    "ABC para clausulas"
    @abstractmethod
    def build(self) -> str:
        pass

class AddableClause(Clause):
    "ABC que permite añadir multiples valores a esa clausula. Ej: SELECT que permite mas de una columna"
    @abstractmethod
    def add(self, *args):
        pass

class SettableClause(Clause):
    "ABC que permite settear un valores a esa clausula. Ej: FROM que solo puede tener un valor."
    @abstractmethod
    def set(self, value):
        pass


class SelectClause(AddableClause):
    def __init__(self):
        self.columns = []

    def add(self, *cols):
        self.columns.extend(cols)

    def build(self):
        if not self.columns:
            return "SELECT *"
        return f"SELECT {', '.join(self.columns)}"


class FromClause(SettableClause):
    def __init__(self):
        self.table = ""

    def set(self, value):
        self.table = value

    def build(self):
        return f"FROM {self.table}" if self.table else ""


class WhereClause(AddableClause):
    def __init__(self):
        self.conditions = []

    def add(self, *conditions: str):
        """
        Agrega una o más condiciones SQL en texto plano.

        Args:
            *conditions: Una o más condiciones como strings, que serán unidas con AND.
        """
        self.conditions.extend(conditions)  # agrega cada string individualmente

    def build(self):
        if not self.conditions:
            return ""
        return f"WHERE {' AND '.join(self.conditions)}"


class OrderByClause(AddableClause):
    def __init__(self):
        self.columns = []

    def add(self, *cols):
        self.columns.extend(cols)

    def build(self):
        if not self.columns:
            return ""
        return f"ORDER BY {', '.join(self.columns)}"


class LimitClause(SettableClause):
    def __init__(self):
        self.limit = None

    def set(self, value: int):
        self.limit = value

    def build(self):
        return f"LIMIT {self.limit}" if self.limit is not None else ""
