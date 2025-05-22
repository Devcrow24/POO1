# Try

## Explicación
Try, except y finally nos sirven para validar datos que pueden o no ser correctos ante una entrada, en este codigo, volveremos a hacer uso del Enum para desplegar una lista de dias y en las entradas verificar si es un dia valido el que se introduce.

## Estructura
El codigo cuenta con una clase.
La clase Dias contiene una lista de variables con todos los dias de la semana y una funcón. La función 'Verificar Dia' contiene una serie de try's, except y finally que validaran la entrada que demos.
El try verifica primero que sea un string, en caso de que no, se avisa, despues convierte la entrada a un solo formato de letra, y al final verifica si el dia se encuentra dentro de la lista de Enum.
El except lanza advertencias o errores que puede contener el formato de la entrada.
El finally, finaliza la ejecución dejando un mensaje al termino de esta.

## Codigo
[Try.py](https://github.com/Devcrow24/POO1/blob/main/Actividad%2012%20-%20Try/diasEnum.py)