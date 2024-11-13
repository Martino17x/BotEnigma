import sys
import time
from bots.bot_no_sabe_encriptar import BotNoSabeEncriptar
from bots.Enigma import BotEnigma
#from bots.bot_profe import BotProfe

def Probar(bot, texto_plano, texto_cifrado, clave):
    print(f"Probando bot: {bot.__class__.__name__}, Texto plano: '{texto_plano}', Texto cifrado: '{texto_cifrado}', Clave: {clave}")

    def print_colored(message, color):
        colors = {"green": "\033[92m", "red": "\033[91m", "end": "\033[0m"}
        print(f"{colors[color]}{message}{colors['end']}")

    def check_result(test_name, expected, obtained):
        if expected == obtained:
            print_colored(f"{test_name}: Ok", "green")
        else:
            print_colored(f"{test_name}: Error (esperado: '{expected}', obtenido: '{obtained}')", "red")
    
    texto_encriptado = bot.Encriptar(texto_plano, clave)
    check_result("Encriptar", texto_cifrado, texto_encriptado)

    texto_descriptado = bot.Desencriptar(texto_cifrado, clave)
    check_result("Desencriptar", texto_plano, texto_descriptado)

    clave_inferida = bot.Romper(texto_cifrado)
    check_result("Romper", clave, clave_inferida)

    print("\n")





# Probando nuestro bot (acá pueden cambiar la siguiente línea por su bot para probarlo)
bot = BotEnigma()
Probar(bot, "HOLA MUNDO. ES UN LINDO DIA"
          , "KSÑE PXQGS. HW YP ÑMPHR GMD"
        , 3)

Probar(bot, "LA SEGURIDAD INFORMATICA ES IMPORTANTE PARA PROTEGER LOS DATOS"
          , "OF XILYWMIEI NQKSWPFXNGF JW MQTTVYERXJ UEWE TWSYILIW PSX IEYSX"
          , 4)

Probar(bot, "QUE ONDA, TODO BIEN? COMO VIENEN CON EL BOT?"
          , "YDM WVLJ, BXLX KPNU? LWUW DQMVMV LWV NS JXB?"
          , 8)

Probar(bot, "LAS MEJORES MILANESAS SON LAS DE MI VIEJA"
          , "XÑF YRVCERF YVXÑZRFÑF FCZ XÑF PR ZU IVQWN"
          , 13)

Probar(bot, "BOCA PERDIO TRES A CERO CON TIGRE. HAY QUE DARLE TIEMPO A GAGO"
          , "UJVU KXMWCI NMXN U WXMI VJG NCZMX. BTS LÑY XTMEY ÑBYFKI T ZUZJ"
          , 20)


