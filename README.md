# Calculadora de índice de masa corporal.

## Reflexiones.

> Aprendi a usar un poco más python y entendi mejor su sintaxis, tuve que investigar y comprender cosas nuevas como el ciclo while que no funciona como en javascript o php, sin embargo no es tan compliado, pude aplicar POO y funciones sin problema alguno, ademas de que me parecio un proyecto escalable y muy bueno para empezar a practicar este lenguaje. Hasta el momento el curso me ha enseñado que python es un lenguaje de programacion muy versatil y con una curva de aprendizaje tolerable.
> Forma en la que cree el programa:
> Dividi el problema en funciones.
> 4 funciones para ser exacto,
> calculadora():Se encarga de hacer el calculo del IMC
> decision()::Se encarga de hacer decidir al usuario si seguir con la ejecucion del programa o terminarla.
> verificacion()::Se encarga de verificar que los campos numericos sean numericos.
> captura()::Devuelve el dato transformado o retorna false
> Tambien utilizamos listas con tuplas para los datos constantes

Se utilizaron ciclos for y while:
for: para recorrer las tuplas de la lista Categorias_adultos
while:para solicitar informacion

Se utilizo try:
Para intentar transformar un dato str a float y en caso de error devolver false y que no hubiese un error en consola.

## Descripción.

Crear un programa que pida al usuario su nombre, apellido paterno, apellido materno, edad, peso y estatura, desplegarlos en pantalla junto con su Índice de Masa Corporal (IMC).

El programa no puede permitir que ningún dato quede vacío, además de asegurarse de que en los campos de edad, peso y estatura el usuario introduzca una cifra. Todo esto antes de proceder con el cálculo del IMC siguiendo la fórmula:

Peso / estatura2 -> Peso sobre estatura al cuadrado

## Objetivos.

Aprenderá a capturar datos introducidos por el usuario.
Aprenderá a validar los datos que le brinde el usuario.
Dominará el uso de operadores matemáticos.
