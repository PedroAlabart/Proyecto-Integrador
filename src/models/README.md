📁 Estructura del Modulo
Este modulo contiene un archivo .py por cada tabla representada en los archivos CSV.

Cada clase está diseñada siguiendo principios de encapsulamiento, con el objetivo de evitar modificaciones erróneas en sus atributos. Una excepción a esto es el atributo ID, que no incluye un método setter, justamente para prevenir su alteración una vez definido.

Habia una superposicion de atributos entre las clases Customers y Employees, por lo que cree en abstracts.py una clase para que hereden.

En la entidad product tuve que cambiar el atributo class a class_type porque la palabra class es un termino reservado en python.

Agregue un constructor de data_types para los valores categoricos como Class y Resistant(ambos atributos de Product) para limitar los valores posibles.

La clase Sale, tiene el atributo TotalPrice. En la clase, este numero se calcula usando product.price, quantity y discount. En la data mockup que nos dan este TotalPrice es un numero random.

La clase Sale tampoco tiene un setter para la transaction_number porque no me parece que sea algo que se deberia modificar facil.

🧠 Consideraciones para futuras iteraciones
Como Ingeniero de Datos, propondría en futuras etapas conversar con los stakeholders para comenzar a recolectar la fecha de nacimiento de los customes. Esta información permitiría realizar análisis más avanzados, como identificar patrones de compra según la edad. Con esos insights, se podrían orientar campañas publicitarias más efectivas hacia los segmentos adecuados del público.