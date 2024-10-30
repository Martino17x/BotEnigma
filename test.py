import re
from difflib import SequenceMatcher

# Alfabeto español completo incluyendo la ñ
ALFABETO_ESPANOL = "abcdefghijklmnñopqrstuvwxyz"

def cargar_lista_desde_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as file:
            return set(line.strip().lower() for line in file)
    except FileNotFoundError:
        print(f"Advertencia: El archivo {nombre_archivo} no se encontró. Se usará una lista vacía.")
        return set()

# Cargar nombres y palabras comunes desde archivos externos
nombres_comunes = cargar_lista_desde_archivo('nombres_comunes.txt')
palabras_comunes = cargar_lista_desde_archivo('palabras_comunes.txt')

def normalizar_letra(letra):
    conversion = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'a', 'É': 'e', 'Í': 'i', 'Ó': 'o', 'Ú': 'u',
        'Ü': 'u', 'ü': 'u',
        'Ñ': 'ñ'
    }
    return conversion.get(letra, letra.lower())

def es_letra_espanola(caracter):
    return caracter.lower() in ALFABETO_ESPANOL

def cifrar_mensaje(mensaje, k=3):
    cifrado = ""
    for i, letra in enumerate(mensaje):
        letra_normalizada = normalizar_letra(letra)
        if es_letra_espanola(letra_normalizada):
            indice = ALFABETO_ESPANOL.index(letra_normalizada)
            if i % 2 == 0:  # Posiciones pares
                nuevo_indice = (indice + k) % len(ALFABETO_ESPANOL)
            else:  # Posiciones impares
                nuevo_indice = (indice + k + 1) % len(ALFABETO_ESPANOL)
            cifrado += ALFABETO_ESPANOL[nuevo_indice]
        else:
            cifrado += letra
    return cifrado

def descifrar_mensaje(mensaje, k=3):
    descifrado = ""
    for i, letra in enumerate(mensaje):
        letra_normalizada = normalizar_letra(letra)
        if es_letra_espanola(letra_normalizada):
            indice = ALFABETO_ESPANOL.index(letra_normalizada)
            if i % 2 == 0:  # Posiciones pares
                nuevo_indice = (indice - k) % len(ALFABETO_ESPANOL)
            else:  # Posiciones impares
                nuevo_indice = (indice - k - 1) % len(ALFABETO_ESPANOL)
            descifrado += ALFABETO_ESPANOL[nuevo_indice]
        else:
            descifrado += letra
    return descifrado

def descifrar_mensaje_cesar(mensaje, k):
    descifrado = ""
    for letra in mensaje:
        letra_normalizada = normalizar_letra(letra)
        if es_letra_espanola(letra_normalizada):
            indice = ALFABETO_ESPANOL.index(letra_normalizada)
            nuevo_indice = (indice - k) % len(ALFABETO_ESPANOL)
            descifrado += ALFABETO_ESPANOL[nuevo_indice]
        else:
            descifrado += letra
    return descifrado

def verificar_descifrado_correcto(texto):
    palabras = re.findall(r'\b[a-záéíóúñ]+\b', texto.lower())
    puntuacion = 0
    for palabra in palabras:
        if palabra in palabras_comunes:
            puntuacion += len(palabra) * 2  # Puntuación mayor para palabras comunes
        elif palabra in nombres_comunes:
            puntuacion += len(palabra) * 3  # Puntuación aún mayor para nombres comunes
        else:
            # Buscar coincidencias parciales
            for palabra_comun in palabras_comunes.union(nombres_comunes):
                ratio = SequenceMatcher(None, palabra, palabra_comun).ratio()
                if ratio > 0.8:  # Si hay una coincidencia del 80% o más
                    puntuacion += len(palabra)
                    break
    return puntuacion

def romper_cifrado(mensaje):
    print("Intentando romper el cifrado. Probando diferentes métodos...\n")
    
    mejor_k = None
    mejor_puntuacion = 0
    mejor_descifrado = ""
    mejor_metodo = ""

    # Método 1: Cifrado con diferenciación entre pares e impares
    print("Método 1: Cifrado por pares e impares\n")
    for k in range(1, len(ALFABETO_ESPANOL)):
        intento_descifrado = descifrar_mensaje(mensaje, k)
        puntuacion = verificar_descifrado_correcto(intento_descifrado)
        
        print(f"k={k}: {intento_descifrado} (Puntuación: {puntuacion})")
        
        if puntuacion > mejor_puntuacion:
            mejor_puntuacion = puntuacion
            mejor_k = k
            mejor_descifrado = intento_descifrado
            mejor_metodo = "Cifrado por pares e impares"

    # Método 2: Cifrado César normal (sin diferenciación entre pares e impares)
    print("\nMétodo 2: Cifrado César estándar\n")
    for k in range(1, len(ALFABETO_ESPANOL)):
        intento_descifrado = descifrar_mensaje_cesar(mensaje, k)
        puntuacion = verificar_descifrado_correcto(intento_descifrado)
        
        print(f"k={k}: {intento_descifrado} (Puntuación: {puntuacion})")
        
        if puntuacion > mejor_puntuacion:
            mejor_puntuacion = puntuacion
            mejor_k = k
            mejor_descifrado = intento_descifrado
            mejor_metodo = "Cifrado César estándar"
    
    if mejor_k is not None:
        print(f"\nEl cifrado más probable es con k={mejor_k} usando el método: {mejor_metodo}. Descifrado: {mejor_descifrado}")
    else:
        print("\nNo se encontró un descifrado claro.")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Romper cifrado")
        print("4. Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            mensaje = input("Ingrese el mensaje a cifrar: ").lower()
            resultado = cifrar_mensaje(mensaje)
            print(f"Mensaje cifrado: {resultado}")

        elif opcion == "2":
            mensaje = input("Ingrese el mensaje a descifrar: ").lower()
            resultado = descifrar_mensaje(mensaje)
            print(f"Mensaje descifrado: {resultado}")

        elif opcion == "3":
            mensaje = input("Ingrese el mensaje cifrado: ").lower()
            romper_cifrado(mensaje)

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    menu()