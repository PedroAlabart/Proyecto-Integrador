from src.database.db_facade import DatabaseFacade
from src.database.querier import SQLQueryBuilder

facade = DatabaseFacade()

# Query usando el builder
builder = (
    SQLQueryBuilder()
    .select("ProductName")
    .from_table("products")
    .where("categoryID = 1")
    .limit(10)
)

df = facade.execute_query(builder)

# Query SQL manual
query = "SELECT * FROM sales WHERE TotalPrice > 100"

df2 = facade.execute_query(query)
