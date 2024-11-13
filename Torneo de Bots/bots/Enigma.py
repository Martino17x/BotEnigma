from bot_abstract import BotAbstract
import re
from collections import Counter

class BotEnigma(BotAbstract):
    def __init__(self):
        self.FRECUENCIAS_ESPERADAS = {
            'A': 12.53, 'B': 1.42, 'C': 4.68, 'D': 5.86, 'E': 13.68, 'F': 0.69,
            'G': 1.01, 'H': 0.70, 'I': 6.25, 'J': 0.44, 'K': 0.02, 'L': 4.97,
            'M': 3.15, 'N': 6.71, 'Ñ': 0.31, 'O': 8.68, 'P': 2.51, 'Q': 0.88,
            'R': 6.87, 'S': 7.98, 'T': 4.63, 'U': 3.93, 'V': 0.90, 'W': 0.01,
            'X': 0.22, 'Y': 0.90, 'Z': 0.52
        }
        self.PALABRAS_COMUNES = set(['EL', 'LA', 'LOS', 'LAS', 'UN', 'UNA', 'UNOS', 'UNAS', 'Y', 'E', 'O', 'U', 'DE', 'DEL', 'AL', 'A', 'ANTE', 'CON', 'EN', 'PARA', 'POR', 'SEGUN', 'SIN', 'SOBRE', 'TRAS', 'QUE', 'COMO', 'CUANDO', 'DONDE', 'CUAL', 'QUIEN', 'CUYO'])

    @property
    def Nombre(self) -> str:
        return "BotEnigma"

    def Encriptar(self, texto_plano: str, clave: int) -> str:
        texto_cifrado = ""
        for i, letra in enumerate(texto_plano):
            if letra in self.Alfabeto():
                indice = self.Alfabeto().index(letra)
                if i % 2 == 0:
                    nuevo_indice = (indice + clave) % len(self.Alfabeto())
                else:
                    nuevo_indice = (indice + clave + 1) % len(self.Alfabeto())
                texto_cifrado += self.Alfabeto()[nuevo_indice]
            else:
                texto_cifrado += letra
        return texto_cifrado

    def Desencriptar(self, texto_cifrado: str, clave: int) -> str:
        texto_descifrado = ""
        for i, letra in enumerate(texto_cifrado):
            if letra in self.Alfabeto():
                indice = self.Alfabeto().index(letra)
                if i % 2 == 0:
                    nuevo_indice = (indice - clave) % len(self.Alfabeto())
                else:
                    nuevo_indice = (indice - clave - 1) % len(self.Alfabeto())
                texto_descifrado += self.Alfabeto()[nuevo_indice]
            else:
                texto_descifrado += letra
        return texto_descifrado

    def Romper(self, texto_cifrado: str) -> int:
        mejor_clave = 0
        mejor_puntuacion = float('-inf')

        for clave in range(len(self.Alfabeto())):
            texto_descifrado = self.Desencriptar(texto_cifrado, clave)
            frecuencias = self.calcular_frecuencias(texto_descifrado)
            
            puntuacion_freq = 100 - self.puntuacion_frecuencias(frecuencias)
            puntuacion_comunes = self.puntuacion_palabras_comunes(texto_descifrado) * 10
            puntuacion_longitud = self.puntuacion_longitud_palabras(texto_descifrado) * 5
            
            puntuacion_total = puntuacion_freq + puntuacion_comunes + puntuacion_longitud
            
            if puntuacion_total > mejor_puntuacion:
                mejor_puntuacion = puntuacion_total
                mejor_clave = clave

        return mejor_clave

    def calcular_frecuencias(self, texto):
        contador = Counter(letra for letra in texto if letra in self.Alfabeto())
        total = sum(contador.values())
        return {letra: (count / total) * 100 for letra, count in contador.items()}

    def puntuacion_frecuencias(self, frecuencias):
        return sum(abs(frecuencias.get(letra, 0) - self.FRECUENCIAS_ESPERADAS[letra]) for letra in self.Alfabeto())

    def puntuacion_palabras_comunes(self, texto):
        palabras = re.findall(r'\b[A-ZÑ]+\b', texto)
        return sum(1 for palabra in palabras if palabra in self.PALABRAS_COMUNES)

    def puntuacion_longitud_palabras(self, texto):
        palabras = re.findall(r'\b[A-ZÑ]+\b', texto)
        return sum(len(palabra) for palabra in palabras) / len(palabras) if palabras else 0