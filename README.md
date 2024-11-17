# atenciones_md_laboral
Programa para contar las atenciones realizadas como medica laboral

Respondiendo a la la necesidad de contar cuantas atenciones se realizaron de manera presencial o virtual como medica en el consultorio de medicina ocupacinal, es que me puse a desarrollar este codigo.

La tarea a mano, de la manera que me la planteó mi jefa, consistía en ir leyendo cada celda de observaciones del excel mensual (que contenía aproximadamente 100 registros), y anotando en dos columna adyacentes llamadas: virtual y presencial, un 1 cuando reconocia una atencion de cada tipo en esa celda o 2, luego al final sumar cada columna y asi obtener el total de atenciones virtuales y presenciales de ese mes.

No me tomó la verdad taaanto tiempo hacerlo, pero saber que iba a tener que volver a hacer esa tarea con las planillas de meses anteriores y cada mes futuro tambien, parecia un poco tedioso. Iluminada por la ultima clase que habia tenido en el curso de ciencia de datos, la solucion era obvia. Tirar unas lineas de codigo que lo hagan sistematicamente: que busquen esas frases, palabras, binomios que yo buscaba cuando leia las observaciones y las vaya sumando. 

Ademas queria hacerlo facil de usar, sin tener que exportar el archivo o la columna como csv, por lo que un input donde copiar y pegar el contenido de las celdas se haga facil e intuitivo. 

Lo que resta por hacer es pasarlo a alguna plataforma como StremIt para poder acceder al programa desde cualquier navegador y poder hacer el copy paste en el input y que analice el texto y diga cuantas atenciones virtuales y presenciales se realizaron en ese texto.

