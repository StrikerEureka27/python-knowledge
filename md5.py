import hashlib


md5 = 'eca00607b2bdf09ccbdbcfb89de65d4f'
sum = 30*(30+1)/2
print(sum)
print(hashlib.md5('hola'.encode('utf-8')).hexdigest())

text = """Friedrich Gauss nació en Brunswick, Alemania, el 30 de abril de 1777. Gauss es, sin duda, uno de los mejores matemáticos de todos los tiempos. 
Cuando Gauss tenía solamente 7 años de edad y asistía a la escuela primaria, uno de sus maestros, para castigarlo porque no ponía atención a
la clase, le pidió que sumara todos los números del 1 al 100. El maestro pensaba que el niño tardaría varias horas en resolver el problema
pero, para su sorpresa, a los cinco minutos de haberle puesto el ejercicio, Gauss le entregó la solución. Sorprendido por la rapidez, el
maestro pidió a Gauss que le explicara el procedimiento que había seguido. En lugar de sumar todos los números, uno por uno, Gauss hizo lo
siguiente: 
Acomodó en una fila todos los números del 1 al 100 y debajo de esa fila acomodó, en otra fila, todos los números del 100 al 1. 
Después sumo las dos filas. Tenía entonces 100 veces el número 101, así que se dio cuenta que si multiplicaba 100 por 101 obtendría dos veces
la suma de todos los números del 1 al 100, por tanto si quería obtener la suma de todos los números del 1 al 100 una sola vez, bastaría con
dividir entre 2 el resultado de la multiplicación.

Siendo su fórmula final la siguiente:
Suma = N*(N+1)/2

!Una brillante resolución matemática sin lugar a dudas!
"""

list = text.split()
#print(list)

for word in list:
    hash = hashlib.md5('MATH.FORMULA'.encode('utf-8')).hexdigest()
    if hash == md5 or hash[0:3] == md5[0:3]:
        print(hash)

