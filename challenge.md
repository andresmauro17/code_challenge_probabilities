Procesamiento y Almacenamiento de Datos CSV

Objetivo: Desarrollar una aplicación que lea datos de un archivo CSV, procese uno de sus campos para calcular una probabilidad, y almacene la información resultante en una base de datos.

Contexto: Se le proporcionará un archivo CSV con los siguientes encabezados:

id: Identificador único.
name: Nombre del elemento, que incluye un coeficiente numérico.
brand: Marca asociada.
score: Puntuación.
probability: Este campo debe ser calculado.

Tarea:
Tu misión es crear una aplicación que cumpla con los siguientes puntos:

- Lectura del CSV: La aplicación debe ser capaz de leer y analizar el archivo CSV proporcionado. Descargar aqui
- Extracción del Coeficiente: El campo name contendrá un nombre junto con un coeficiente numérico. Tu tarea es extraer este coeficiente. Por ejemplo, si name es "Producto A 1.25", el coeficiente a extraer sería 1.25. Puedes asumir que el coeficiente será un número decimal o entero.
- Cálculo de probability: Usa el coeficiente extraído del campo name para calcular el valor de probability. La fórmula para este cálculo es la siguiente:
probability=coeficiente x score​
- Almacenamiento en Base de Datos: Los datos procesados, incluyendo el id, name (original o modificado según tu criterio), brand, score, y la probability calculada, deben ser almacenados en una base de datos de tu elección (por ejemplo, SQLite, PostgreSQL, MySQL, etc.). La estructura de la tabla de la base de datos debe ser lógica y adecuada para los datos.

Tecnologías:
Puede usar Laravel / python, las librerías, las técnicas y las herramientas que consideres más apropiadas para completar esta tarea.

Entregables:

- El código fuente completo de tu solución.
- Una breve explicación de tus decisiones de diseño y cualquier suposición realizada.
