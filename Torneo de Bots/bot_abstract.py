from abc import ABC, abstractmethod

# Esta clase es una clase abstracta que define los métodos que deben ser implementados por 
# las clases que hereden de ella.
# Cada grupo deberá implementar una clase Bot<XXX> que herede de esta clase y que implemente
class BotAbstract(ABC):
    # Este es el alfabeto que se usará para encriptar y desencriptar los mensajes.
    @classmethod
    def Alfabeto(cls):
        return "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    # Devuelve el nombre del Bot
    @property
    @abstractmethod
    def Nombre(self) -> str:
        pass
    
    # Encripta el texto plano con la clave indicada.
    # El algoritmo suma "clave" a cada caracter par del texto plano
    # y "clave + 1" a cada caracter impar.
    # Importante: Recordar que nuestro alfabeto contiene la letra "Ñ"
    # Los textos que recibirá son en mayúsculas y sin tildes. 
    # Cualquier otro caracter (espacios, signos de puntuación, etc) no se encriptan.
    @abstractmethod
    def Encriptar(self, texto_plano: str, clave: int) -> str:
        pass

    # Desenclipta el texto cifrado con la clave indicada.
    @abstractmethod
    def Desencriptar(self, texto_cifrado: str, clave: int) -> str:
        pass

    # Rompe el texto cifrado sin conocer la clave.
    @abstractmethod
    def Romper(self, texto_cifrado: str) -> int:
        pass

    