#Jose Luis Mata Lomeli
#A01377205

#Obtener velocidad promedio de un conductor que registro el tiempo que le llevo su ultimo viaje y la distanciaa recorrida.

#Analisis;
#Entrada: Tiempo de viaje y Distancia Recorrida
#Salida: Velocidad Promedio
#E/S: Velocidad = Distancia / Tiempo

#Programacion;
#1. Leer distancia y tiempo
#2. Formula de Velocidad
#3. Imprimir Velocidad

distancie = int(input("Teclea la distancia recorrida (kms. enteros): "))
tiempo = int(input("Tiempo en el que llego a su punto de destino (hrs. enteras): "))

velocidad = distancie / tiempo

print("Tu velocidad fue de", velocidad, "kms/h")
