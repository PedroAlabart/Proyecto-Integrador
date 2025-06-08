## 🧹 Carga de Datos en MySQL

Este proyecto utiliza un único script SQL llamado `load_data.sql` que centraliza todo el proceso de carga de datos desde archivos CSV hacia una base de datos en MySQL.

### 📄 Contenido del archivo `load_data.sql`

El script contiene tres grandes secciones:

1. **Creación de schema y tablas**

   * Se crea la base de datos `SalesTransactions` desde cero.
   * Se definen todas las tablas necesarias junto con sus claves primarias y foráneas.

2. **Definición de funciones auxiliares**

   * Se incluye la función `convert_time_to_seconds()` para convertir campos de hora en segundos y permitir el cálculo de fechas absolutas.

3. **Carga de datos (`LOAD DATA INFILE`)**

   * Se realiza la carga de todos los archivos CSV ubicados en la carpeta `/data/`, con los comandos `LOAD DATA INFILE`.


---

### ✅ Validaciones y transformaciones de datos

* **`MiddleInitial` (tabla `customers`)**
  Esta columna es de tipo `VARCHAR(1)` y puede venir como `NULL` en formato string desde el archivo CSV.
  Se aplica la lógica:

  ```sql
  MiddleInitial = LEFT(NULLIF(@MiddleInitial, 'NULL'), 1)
  ```

  Esto transforma `"NULL"` en un valor `NULL` real y limita el contenido a un solo carácter.

* **`convert_time_to_seconds()`**
  Algunos archivos CSV (como `products` y `sales`) contienen valores de tiempo relativos (ej. `14:01.7`) en lugar de un `DATETIME`.
  Para estandarizar, se usa esta función para convertir el tiempo a segundos y restarlo de la fecha actual:

  ```sql
  SET @now_fixed = NOW();
  ...
  ModifyDate = @now_fixed - INTERVAL convert_time_to_seconds(...) SECOND;
  ```

  Por ejemplo:

  ```
  '14:01.7' → 5041.7 segundos → Fecha actual - 5041.7 segundos
  ```

---

### 💡 Nota sobre la organización

Aunque la consigna solicita incluir todo en un solo archivo, una mejor práctica (si no estuviera limitado por los requerimientos) sería modularizar el proceso en tres archivos distintos:

* `create_schema.sql`
* `functions.sql`
* `load_data.sql`

---

### 🚀 Instrucciones de uso

1. Asegurate de tener permisos habilitados para usar `LOAD DATA INFILE` en MySQL.
2. Abrí tu cliente MySQL (Workbench, DBeaver, terminal, etc.).
3. Modificá las rutas de los CSV si es necesario (las rutas absolutas en el script deben apuntar a tu sistema).
4. Ejecutá el script completo

> ⚠️ **Importante:** Si usás una instalación de MySQL con `secure_file_priv`, asegurate de que los archivos CSV estén ubicados en la carpeta autorizada o modificá la configuración.
