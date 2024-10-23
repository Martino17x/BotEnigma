import re

# Diccionario de palabras comunes en español (ampliable)
diccionario_palabras_comunes = {"hola", "mundo", "como", "estas", "el", "ella", "es", "un", "una", "yo", "tu", "la", "que", "de", "a", "en", "más", "se", "quedaron", "divertidos"}

# Función que convierte letras con tildes a su versión sin tilde
def normalizar_letra(letra):
    conversion = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'Á': 'A',
        'É': 'E',
        'Í': 'I',
        'Ó': 'O',
        'Ú': 'U',
        'Ü': 'U',
        'ü': 'U'
    }
    return conversion.get(letra, letra)

def es_letra_espanola(caracter):
    # Consideramos letras válidas del alfabeto español, incluyendo ñ
    return caracter.isalpha() and caracter in "abcdefghijklmnñopqrstuvwxyz"

def cifrar_mensaje(mensaje, k=3):
    cifrado = ""
    for i, letra in enumerate(mensaje):
        letra_normalizada = normalizar_letra(letra.lower())
        if es_letra_espanola(letra_normalizada):  # Solo ciframos si es una letra española
            if i % 2 == 0:  # Posiciones pares
                cifrado += chr((ord(letra_normalizada) + k - 97) % 26 + 97)
            else:  # Posiciones impares
                cifrado += chr((ord(letra_normalizada) + (k + 1) - 97) % 26 + 97)
        else:
            cifrado += letra  # Si no es una letra (como espacio o símbolo), lo dejamos igual
    return cifrado

def descifrar_mensaje(mensaje, k=3):
    descifrado = ""
    for i, letra in enumerate(mensaje):
        if es_letra_espanola(letra):  # Solo desciframos si es una letra española
            if i % 2 == 0:  # Posiciones pares
                descifrado += chr((ord(letra) - k - 97) % 26 + 97)
            else:  # Posiciones impares
                descifrado += chr((ord(letra) - (k + 1) - 97) % 26 + 97)
        else:
            descifrado += letra  # Si no es una letra (como espacio o símbolo), lo dejamos igual
    return descifrado

def descifrar_mensaje_cesar(mensaje, k):
    descifrado = ""
    for letra in mensaje:
        if es_letra_espanola(letra):  # Solo desciframos si es una letra española
            descifrado += chr((ord(letra) - k - 97) % 26 + 97)
        else:
            descifrado += letra  # Si no es una letra (como espacio o símbolo), lo dejamos igual
    return descifrado

def verificar_descifrado_correcto(texto):
    # Elimina caracteres no alfabéticos y divide el texto en palabras
    palabras = re.findall(r'\b[a-záéíóúñ]+\b', texto)
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
    for k in range(1, 26):
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
    for k in range(1, 26):
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

menu()
