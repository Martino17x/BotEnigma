import re
from collections import Counter

ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

FRECUENCIAS_ESPERADAS = {
    'A': 12.53, 'B': 1.42, 'C': 4.68, 'D': 5.86, 'E': 13.68, 'F': 0.69,
    'G': 1.01, 'H': 0.70, 'I': 6.25, 'J': 0.44, 'K': 0.02, 'L': 4.97,
    'M': 3.15, 'N': 6.71, 'Ñ': 0.31, 'O': 8.68, 'P': 2.51, 'Q': 0.88,
    'R': 6.87, 'S': 7.98, 'T': 4.63, 'U': 3.93, 'V': 0.90, 'W': 0.01,
    'X': 0.22, 'Y': 0.90, 'Z': 0.52
}

PALABRAS_COMUNES = set(['EL', 'LA', 'LOS', 'LAS', 'UN', 'UNA', 'UNOS', 'UNAS', 'Y', 'E', 'O', 'U', 'DE', 'DEL', 'AL', 'A', 'ANTE', 'CON', 'EN', 'PARA', 'POR', 'SEGUN', 'SIN', 'SOBRE', 'TRAS', 'QUE', 'COMO', 'CUANDO', 'DONDE', 'CUAL', 'QUIEN', 'CUYO'])

def encriptar(texto_plano, clave):
    texto_cifrado = ""
    for i, letra in enumerate(texto_plano):
        if letra in ALFABETO:
            indice = ALFABETO.index(letra)
            if i % 2 == 0:
                nuevo_indice = (indice + clave) % len(ALFABETO)
            else:
                nuevo_indice = (indice + clave + 1) % len(ALFABETO)
            texto_cifrado += ALFABETO[nuevo_indice]
        else:
            texto_cifrado += letra
    return texto_cifrado

def desencriptar(texto_cifrado, clave):
    texto_descifrado = ""
    for i, letra in enumerate(texto_cifrado):
        if letra in ALFABETO:
            indice = ALFABETO.index(letra)
            if i % 2 == 0:
                nuevo_indice = (indice - clave) % len(ALFABETO)
            else:
                nuevo_indice = (indice - clave - 1) % len(ALFABETO)
            texto_descifrado += ALFABETO[nuevo_indice]
        else:
            texto_descifrado += letra
    return texto_descifrado

def calcular_frecuencias(texto):
    contador = Counter(letra for letra in texto if letra in ALFABETO)
    total = sum(contador.values())
    return {letra: (count / total) * 100 for letra, count in contador.items()}

def puntuacion_frecuencias(frecuencias):
    return sum(abs(frecuencias.get(letra, 0) - FRECUENCIAS_ESPERADAS[letra]) for letra in ALFABETO)

def puntuacion_palabras_comunes(texto):
    palabras = re.findall(r'\b[A-ZÑ]+\b', texto)
    return sum(1 for palabra in palabras if palabra in PALABRAS_COMUNES)

def puntuacion_longitud_palabras(texto):
    palabras = re.findall(r'\b[A-ZÑ]+\b', texto)
    return sum(len(palabra) for palabra in palabras) / len(palabras) if palabras else 0

def romper_cifrado(texto_cifrado):
    mejor_clave = 0
    mejor_puntuacion = float('-inf')
    mejor_texto = ""

    for clave in range(len(ALFABETO)):
        texto_descifrado = desencriptar(texto_cifrado, clave)
        frecuencias = calcular_frecuencias(texto_descifrado)
        
        puntuacion_freq = 100 - puntuacion_frecuencias(frecuencias)
        puntuacion_comunes = puntuacion_palabras_comunes(texto_descifrado) * 10
        puntuacion_longitud = puntuacion_longitud_palabras(texto_descifrado) * 5
        
        puntuacion_total = puntuacion_freq + puntuacion_comunes + puntuacion_longitud
        
        if puntuacion_total > mejor_puntuacion:
            mejor_puntuacion = puntuacion_total
            mejor_clave = clave
            mejor_texto = texto_descifrado

    return mejor_clave, mejor_texto

def menu():
    while True:
        print("\n--- Menú del Cifrado Enigma ---")
        print("1. Encriptar mensaje")
        print("2. Desencriptar mensaje")
        print("3. Romper cifrado")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            mensaje = input("Ingrese el mensaje a encriptar: ").upper()
            clave = int(input("Ingrese la clave numérica: "))
            mensaje_encriptado = encriptar(mensaje, clave)
            print(f"Mensaje encriptado: {mensaje_encriptado}")
        
        elif opcion == '2':
            mensaje = input("Ingrese el mensaje a desencriptar: ").upper()
            clave = int(input("Ingrese la clave numérica: "))
            mensaje_desencriptado = desencriptar(mensaje, clave)
            print(f"Mensaje desencriptado: {mensaje_desencriptado}")
        
        elif opcion == '3':
            mensaje = input("Ingrese el mensaje cifrado a romper: ").upper()
            clave, mensaje_descifrado = romper_cifrado(mensaje)
            print(f"Clave encontrada: {clave}")
            print(f"Mensaje descifrado: {mensaje_descifrado}")
        
        elif opcion == '4':
            print("Gracias por usar el Cifrado Enigma. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    menu()
