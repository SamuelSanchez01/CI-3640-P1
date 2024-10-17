# Creo que con esto se gana 

## Usando APL

[gnu-apl](https://github.com/ilovezfs/gnu-apl)

Para correr:

```
apl -f A.apl
```

Se inicia el arhivo y solicita la entrada del usuario por entrada estándar

Como puede ser tedioso correrlo 40 y tantas veces creé ForTest.apl que cuando se inicia debe usarse de la siguiente manera

```
A n
```

Y retornara lo solicitado con n

Hay un script con python para verificar (se que es top codigos mas ineficientes pero estaba cansao y estaba probando nada mas que los resultados fuesen acorde)

```
python3 prueba.py
```

## Explicacion y pseudo degolf:

```
n←⎕
B←⌊2⍟n
C←⌊2⍟(B!n)×((B-1)!n)÷n
x←({⍵,+/¯3↑⍵}⍣n)1 2
x[C+1]
```

```
n←⎕
```
Declara n y ese cuadrado es solicitar que el usuario marque el input numerico

```
B←⌊2⍟n
```
Declara B y le asigna el valor de el piso (⌊) del logaritmo base 2 de n (2⍟n)

```
C←⌊2⍟(B!n)×((B-1)!n)÷n
```
Declara C y le asigna el piso del logaritmo de base 2 de (B!n)×((B-1)!n)÷n. Normalmente ! seria not o factorial pero estamos en un lenguaje que se invento para tipear poco (y sufrir con el teclado aprendiendo), entonces B!n es el binomial de n entre B, o sea factorial de n entre factorial de B por factorial de n-B, por eso se declaro 2 B y  no se tipeo abajp, gastaba 4 caracteres mas

ahora falta algo

la mamalona

la maleducada

la malagradecida

TRIBONACCIIIIIIIII

```
x←({⍵,+/¯3↑⍵}⍣n)1 2
```

ok, aqui vamos a separar en 3 partes, le estamos asignando a x un valor el cual es ({⍵,+/¯3↑⍵}⍣n)1 2

1 2 es un vector que contiene al 1 y 2

({⍵,+/¯3↑⍵}⍣n) es un procedimiento que toma lo de la derecha como ⍵ y a ⍵ agrega un elemento (,) el cual ela suma (+) de los 3 valores anteriores (/¯3↑) de ⍵ pero, eso agregaria solo un numero de tribonacci, entonces hay que repetir el proceso hasta que tengamos toda la data de los numeros de tribonacci que necesitamos (⍣n) para ser mas exacto se podia poner el numero mas alto al que habia que calcular tribonacci pero era poner 30 y algo y eso ocupa 2 caracteres, n 1 y justamente busque y nunca iba a necesitar un tribonacci mas alto que n

Podria surgir una duda y es como estoy agregando null 1 y 2 y es que apl lo toma como 0 y asi obtengo mi tribonacci

```
x[C+1]
```

Por ultimo imprimo el valor de tribonacci de C+1 (el +1 del ejercicio)

# DECLARAR C NO ERA NECESARIO, BAJO EL NUMEROOOOOOOOOOOO