"""
Práctica Strings, Indexing, Slicing y Stride
Objetivo

Descifrar los "Mensajes Secretos de una Carta de Amor" usando strings, indexación, slicing, stride y strings de múltiples líneas en Python.

Instrucciones:

Se te proporcionará una carta de amor que contiene tres párrafos, cada uno con un mensaje secreto oculto.

Tu tarea es escribir un programa en Python que utilice técnicas de indexación, slicing y stride para descifrar estos mensajes.

Cada párrafo tiene un patrón de codificación diferente:

En el primer párrafo, el mensaje secreto está formado por cada decimoctavo (18) caracter, comenzando desde el segundo caracter.

En el segundo párrafo, el mensaje secreto se encuentra entre el caracter 138 y 147 de la cadena de texto.

En el tercer párrafo, el mensaje secreto está formado por las letras que se encuentran en las siguientes posiciones de la cadena de texto:

Primera letra: posición 125

Segunda letra: posición 94

Tercera letra: posición 35

Cuarta letra: posición 107

Quinta letra: posición 20

Sexta letra: posición 1

Usa print para mostrar los mensajes secretos decodificados.

IMPORTANTE: Ten en cuenta que los números de posición que se proporcionan cuentan el 0 como primer caracter.



Resultado esperado:

Mensajes Secretos Decodificados:

Mensaje secreto 1:

[Mensaje decodificado del primer párrafo]

Mensaje secreto 2:

[Mensaje decodificado del segundo párrafo]

Mensaje secreto 3:

[Primera letra decodificada del mensaje del tercer párrafo]

[Segunda letra decodificada del mensaje del tercer párrafo]

[Tercera letra decodificada del mensaje del tercer párrafo]

[Cuarta letra decodificada del mensaje del tercer párrafo]

[Quinta letra decodificada del mensaje del tercer párrafo]

[Sexta letra decodificada del mensaje del tercer párrafo]
"""
parrafo1 = "Cada dia te quiero mas y nunca lo he olvidado."

parrafo2 = "En el corazón de una historia de amor tecnológica, Lucas y Carla compartían su pasión por la programación. Cada día, mientras aprendían a programar, sus corazones se sincronizaban con cada línea de código."

parrafo3 = "En cada amanecer, veo el brillo de tus ojos; en cada atardecer, siento el calor de tu abrazo; y en cada noche estrellada, me pierdo en el infinito de tu amor."

print("Mensajes Secretos Decodificados:")
print("Mensaje secreto 1:")
print(parrafo1[1::18])

print("Mensaje secreto 2:")
print(parrafo2[138:147])

print("Mensaje secreto 3:")
print(parrafo3[125])
print(parrafo3[94])
print(parrafo3[35])
print(parrafo3[107])
print(parrafo3[20])
print(parrafo3[1])
