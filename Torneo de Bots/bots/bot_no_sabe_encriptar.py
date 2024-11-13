from bot_abstract import BotAbstract

# Este bot, no sabe encriptar, por lo que simplemente encripta todas las letras como "A"
# y desencripta todas las letras como "B"
class BotNoSabeEncriptar(BotAbstract):
    @property
    def Nombre(self) -> str:
        return "BotNoSabeEncriptar"

    def Encriptar(self, texto_plano: str, clave: int) -> str:
        return "A" * len(texto_plano)

    def Desencriptar(self, texto_cifrado: str, clave: int) -> str:
        return "B" * len(texto_cifrado)

    def Romper(self, texto_cifrado: str) -> int:
        return 0
