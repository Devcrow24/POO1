# Hilos y Red

## Explicación
Los hilos permiten ejecutar funciones sin la necesidad de que sea un metodo lineal, ademas de la ventaja de tener un intervalo de tiempo que podemos modificar para que las funciones se vayan ejecutando

## Estructura
Existen tres codigos que muestran los diferentes escenarios.

- 1. [Ejemplo 1](https://github.com/Devcrow24/POO1/blob/main/Actividad%2016%20-%20Hilos%20y%20red/thread.py)
El codigo contiene una clase. La clase 'Hilo' que tiene un constructor y una función, en el constructor muestra el nombre del hilo y el intervalo de tiempo en el que se estará ejecutando. La funcion simplemente ejecuta el hilo.

- 2. [Ejemplo 2](https://github.com/Devcrow24/POO1/blob/main/Actividad%2016%20-%20Hilos%20y%20red/thread2.py)
El codigo contiene una función. La dunción 'tarea' que tiene los parametrs, 'nombre' y el intervalo de tiempo en el que se estará ejecutando. El 'hilo 1' y el 'Hilo 2' se ejecutan, aunque uno finaliza antes que el otro, cuando todas finalicen se ejecutará la siguiente tarea

- 3. [asyncio](https://github.com/Devcrow24/POO1/blob/main/Actividad%2016%20-%20Hilos%20y%20red/asyncio.py)
El codigo contiene un ejercicio sobre la creación de funciones asincronas que permiten esperar a que una función termine sin terminar la ejecución.