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
apl -f ForTest.apl
A 10
A 30
A 25
```

Y retornará lo solicitado, el numero de 10, 30 25 y asi...

Hay un script con python para verificar (se que es top codigos mas ineficientes pero estaba cansao y estaba probando nada mas que los resultados fuesen acorde)

```
python3 prueba.py
```

## Explicacion y pseudo degolf:

```
n←⎕
B←⌊2⍟n
x←({⍵,+/¯3↑⍵}⍣n)1 2
x[(⌊2⍟(B!n)×((B-1)!n)÷n)+1]
```

```
n←⎕
```
Declara n y ese cuadrado es solicitar que el usuario marque el input numerico

```
B←⌊2⍟n
```
Declara B y le asigna el valor de el piso (⌊) del logaritmo base 2 de n (2⍟n)

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
x[(⌊2⍟(B!n)×((B-1)!n)÷n)+1]
```

Por ultimo imprimo el valor de tribonacci de el logaritmo base 2 de:

Binomial de B entre n, multiplicado por el binomial de b-1 entre n y todo dividido entre n

# Se logró

## Sección con chistes malos/chinazos

¿A la otra gente cuánto le medirá? ¿Y el código?

¿Te sirve que me mida 85?

### Juan merece su subsección aparte

Samuel, no entiendo por qué sigues esquizo si ya te lo vi y eres el que mas pequeño lo tiene

Ese lo tiene muy grande, es impresionante

Definitivamente lo tengo mas grande que tu

Ella lo tenia muy largo y ayude a que lo tuviese mas pequeño
