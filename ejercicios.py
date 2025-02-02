#Ejercicio #1 

import math

def tem_time(T0, Ts, k, t):
    return Ts + (T0 - Ts) * math.exp(-k * t)

def time_tem(T0, Ts, k, variacion):
    T_final = Ts - variacion
    t = -math.log((T_final - Ts) / (T0 - Ts)) / k
    return t


# Parámetros
T0 = 5  # Temperatura inicial en ºC
Ts = 40  # Temperatura ambiente en ºC
k = 0.45  # Constante

# Cálculo de temperaturas para 1, 5, 12 y 14 horas
tiempos = [1, 5, 12, 14]
temperaturas = {t: tem_time(T0, Ts, k, t) for t in tiempos}

# Mostrar resultados
for t, temp in temperaturas.items():
    print(f"Temperatura después de {t} horas: {temp:.2f} ºC")

# Cálculo del tiempo para estar a 0.5ºC menos que la temperatura ambiente
variacion = 0.5
tiempo_necesario = time_tem(T0, Ts, k, variacion)

print(f"\nTiempo necesario para que la temperatura esté a {variacion}ºC menos que la temperatura ambiente: {tiempo_necesario:.2f} horas")
#Ejercicio #2 


def letra_DNI(DNI):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    residuo = DNI % 23
    letra = letras[residuo]
    return letra

def main():
    print("Este programa te la da letra de tu DNI") 
    DNI = int(input("Introduce el número de tu DNI : "))
    letra = letra_DNI(DNI)
    print(f"La letra del DNI {DNI} es: {letra}")

if __name__ == "__main__":
    main()

#Ejercicio #3
def valor_de_pi(n):
    pi = 0
    for k in range(1, n + 1):
        pi += ((-1) ** (k + 1)) / (2 * k - 1)
    pi *= 4
    return pi


n = 200
valor_pi = valor_de_pi(n)
print(f"Valor aproximado de π con n={n}: {valor_pi}")

#Ejercicio #4

def fibonacci_suc(n):
    fib_s = [0, 1]
    for i in range(2, n):
        siguiente= fib_s[i - 1] + fib_s[i - 2]
        fib_s.append(siguiente)
    if n == 1:
        return [0]
    return fib_sequence[:n]

print(" Este programa calcula la sucesion Fibonacci de un #(n) dado") 
n = int(input("Introduce el valor de n: "))
lista = fibonacci_suc(n)
print(f"La sucesión de Fibonacci para n={n} es: {lista}")

#Ejercicio #5 

def crear_listado():
    listado = []
    for i in range(1, 101):
        if i % 2 == 0:
            listado.append(i ** 2)
        else:           
            listado.append(i ** 3)
     return listado

def suma_millon(listado):
    suma = 0
    cantidad = 0
    for numero in numeros:
        if suma + numero < 1000000:
            suma += numero
            cantidad+= 1
        else:
            break
     return suma, cantidad


lista_numeros = crear_listado()
resultado, cantidad = suma_millon(lista_numeros)

print(f"Números en la lista : {lista_numeros}")
print(f"La suma más cercana a un millón de estos numeros es: {resultado} y fueron sumados para obtenerlas {cantidad} números")

# Ejercicio #6
def desglosar_cantidad(cantidad):
    # Definimos los billetes y monedas disponibles
    billetes_monedas = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    desglose = {}

    for valor in billetes_monedas:
        if cantidad >= valor:
            num_billetes = cantidad // valor  # Número de billetes/monedas de este valor
            cantidad -= num_billetes * valor   # Restamos el valor total de esos billetes/monedas
            desglose[valor] = num_billetes      # Guardamos el número en el desglose

    return desglose

def main():
    while True:
        try:
            cantidad = int(input("Introduce una cantidad entera en euros: "))
            if cantidad < 0:
                print("Por favor, introduce un número entero positivo.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Debes introducir un número entero.")

    desglose = desglosar_cantidad(cantidad)

    print("\nDesglose de la cantidad en billetes y monedas:")
    for valor, cantidad in desglose.items():
        print(f"{cantidad} billete(s)/moneda(s) de {valor} euros")

if __name__ == "__main__":
    main()
