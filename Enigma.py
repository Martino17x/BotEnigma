import re

# Alfabeto español completo incluyendo la ñ
ALFABETO_ESPANOL = "abcdefghijklmnñopqrstuvwxyz"

# Diccionario de palabras comunes en español (ampliable)
diccionario_palabras_comunes = {"hola", "mundo", "como", "estas", "el", "ella", "es", "un", "una", "yo", "tu", "la", "que", "de", "a", "en", "más", "se", "quedaron", "divertidos", "ñandu"}

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
    # Elimina caracteres no alfabéticos y divide el texto en palabras
    palabras = re.findall(r'\b[a-záéíóúñ]+\b', texto.lower())
    # Compara cada palabra con el diccionario
    coincidencias = sum(1 for palabra in palabras if palabra in diccionario_palabras_comunes)
    return coincidencias

def romper_cifrado(mensaje):
    print("Intentando romper el cifrado. Probando diferentes métodos...\n")
    
    mejor_k = None
    mejor_coincidencia = 0
    mejor_descifrado = ""
    mejor_metodo = ""

    # Método 1: Cifrado con diferenciación entre pares e impares
    print("Método 1: Cifrado por pares e impares\n")
    for k in range(1, len(ALFABETO_ESPANOL)):
        intento_descifrado = descifrar_mensaje(mensaje, k)
        coincidencias = verificar_descifrado_correcto(intento_descifrado)
        
        print(f"k={k}: {intento_descifrado} (Coincidencias: {coincidencias})")
        
        if coincidencias > mejor_coincidencia:
            mejor_coincidencia = coincidencias
            mejor_k = k
            mejor_descifrado = intento_descifrado
            mejor_metodo = "Cifrado por pares e impares"

    # Método 2: Cifrado César normal (sin diferenciación entre pares e impares)
    print("\nMétodo 2: Cifrado César estándar\n")
    for k in range(1, len(ALFABETO_ESPANOL)):
        intento_descifrado = descifrar_mensaje_cesar(mensaje, k)
        coincidencias = verificar_descifrado_correcto(intento_descifrado)
        
        print(f"k={k}: {intento_descifrado} (Coincidencias: {coincidencias})")
        
        if coincidencias > mejor_coincidencia:
            mejor_coincidencia = coincidencias
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