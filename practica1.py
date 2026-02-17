#1 PAR O IMPAR 
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("Par")
else:
    print("Impar")

#2 n O P 
numero = float(input("Ingresa un número: "))
if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Es cero")

#3 MA O mN
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

#4 AP O RE
calificacion = float(input("Ingresa la calificación: "))
if calificacion >= 60:
    print("Aprobado")
else:
    print("Reprobado")

#5 CALFI 
nota = float(input("Ingresa la nota numérica: "))

if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("F")

#6 AGUA 
temp = float(input("Ingresa la temperatura en °C: "))

if temp < 0:
    print("Sólido")
elif 0 <= temp <= 100:
    print("Líquido")
else:
    print("Vapor")
    