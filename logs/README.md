# Registro de Log: `unknown_data_type`

Este log se utiliza para registrar los intentos de uso de tipos de datos no válidos en las columnas `Resistant` y `Class` de la tabla `products`.

Actualmente, el control se limita a estas dos columnas. Sin embargo, el sistema está diseñado para ser extensible, por lo que en el futuro podría abarcar otras columnas que también requieran validación de tipos de datos.

## Propósito

- Detectar y registrar inconsistencias en los tipos de datos asignados.
- Facilitar el monitoreo y depuración de errores en el procesamiento de datos.

## Ejemplo de registro

```json
{
  "timestamp": "2025-06-08T15:30:45Z",
  "column": "Resistant",
  "invalid_value": "maybe",
  "expected_type": "boolean"
}
