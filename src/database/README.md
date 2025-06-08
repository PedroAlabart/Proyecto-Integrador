# Módulo `database`

Módulo para la gestión y ejecución de consultas SQL en base de datos MySQL usando SQLAlchemy y un patrón Builder para construcción fluida y segura de queries. Cuenta ademas con una fachada

---

## Descripción

Este módulo proporciona una **fachada de acceso a base de datos** junto con un **query builder** para construir consultas SQL de forma programática y segura. Además, cuenta con un decorador que mejora la visualización de resultados (`pandas.DataFrame`) en consola.

---

## Componentes principales

### `DatabaseConnection`

- Singleton que maneja la conexión a la base de datos.
- Configura la conexión a MySQL usando variables de entorno definidas en `.env` (DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME).
- Proporciona sesiones SQLAlchemy para ejecutar consultas.

### `DatabaseFacade`

- Fachada que abstrae la ejecución de consultas SQL.
- Permite ejecutar consultas tanto manuales (strings SQL) como construidas con `SQLQueryBuilder`.
- Usa un decorador para mostrar resultados `pandas.DataFrame` en consola con formato agradable.

### `SQLQueryBuilder`

- Builder para construir consultas SQL (SELECT).
- Encadena métodos para definir cláusulas: `select()`, `from_table()`, `where()`, `order_by()`, `limit()`.
- Genera la consulta SQL completa en string.

### Decorador `prettify_output`

- Decora métodos para imprimir resultados `DataFrame` con un marco ajustado dinámicamente al contenido.
- Mejora la legibilidad del output en consola.

---
