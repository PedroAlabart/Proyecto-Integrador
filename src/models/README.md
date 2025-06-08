## 📁 Estructura del Módulo

Este módulo contiene un archivo `.py` por cada tabla representada en los archivos CSV.

Cada clase está diseñada siguiendo principios de **encapsulamiento**, con el objetivo de evitar modificaciones erróneas en sus atributos. Una excepción a esto es el atributo `ID`, que **no incluye un método setter**, precisamente para prevenir su alteración una vez definido.

Se identificó una superposición de atributos entre las clases `Customers` y `Employees`, por lo que se creó en `abstracts.py` una clase base que ambas heredan.

En la entidad `Product`, se cambió el atributo `class` a `class_type` ya que `class` es una palabra reservada en Python.

Se agregó un **constructor de `data_types`** para los valores categóricos como `Class` y `Resistant` (ambos atributos de `Product`) con el objetivo de **limitar los valores posibles**.

La clase `Sale` incluye el atributo `TotalPrice`. Sin embargo, en la clase este valor se **calcula** usando `product.price`, `quantity` y `discount`. En la data brindada por Henry, este campo es un número aleatorio.

Asimismo, la clase `Sale` no incluye un setter para `transaction_number` dado que no debería ser modificado de forma trivial una vez asignado.

---

## 🧠 Consideraciones para futuras iteraciones

Como Ingeniero de Datos, propondría en futuras etapas mantener conversaciones con los stakeholders para comenzar a **recolectar la fecha de nacimiento de los `customers`**. Esta información permitiría realizar análisis más avanzados, como identificar patrones de compra según la edad. Con estos insights, se podrían orientar **campañas publicitarias más efectivas** hacia los segmentos adecuados del público.
