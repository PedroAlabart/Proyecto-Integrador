# 🛩️ Aplicación de Gestión y Validación de Datos de Ventas

Esta aplicación está diseñada para gestionar, consultar y validar datos de ventas almacenados en una base de datos MySQL.

---

## 📦 Estructura de Módulos

### `database`

Módulo encargado de la conexión y ejecución de consultas SQL. Proporciona:

* Un **singleton** para manejar la conexión a MySQL usando SQLAlchemy.
* Una **fachada (`DatabaseFacade`)** que abstrae el acceso a datos.
* Un **query builder (`SQLQueryBuilder`)** para construir consultas SQL de forma fluida y segura.
* Un decorador para **mejorar la visualización** de resultados en consola como `DataFrame`.


---

### `models`

Contiene las representaciones de las entidades del negocio (Customers, Employees, Products, Sales, etc.). Se diseñaron con encapsulamiento para evitar modificaciones indebidas, y se aplicaron mejoras como:

* Herencia común para atributos compartidos.
* Validación de atributos categóricos como `Resistant` y `Class` mediante un **constructor de tipos restringidos**.
* Cálculo automático del `TotalPrice` en `Sale`.
* Prevención de modificación del `transaction_number`.

---

### `sql`

Contiene el archivo load_data.sql utilizado para importar la información desde archivos CSV hacia las tablas de la base de datos de manera automatizada y estructurada.

---

### `logger`

Registro de errores para tipos de datos inválidos, centrado actualmente en los campos Resistant y Class del producto. 
Cuenta con un factory para crear diferentes archivos log. Ademas, permite:

- Monitorear entradas no válidas en datos categóricos.

- Generar logs estructurados (JSON) con detalles sobre el error detectado.

Pensado como base para una futura validación automatizada de calidad de datos.

---

##  📈 Avances
Contiene un archivo jupyter con los avances n°2 y 3 detallados