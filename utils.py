#Cores utilizadas
class Cores:
    VERDE = '\033[92m'
    VERMELHO = '\033[91m'
    RESET = '\033[0m'


def cor(numero: int, texto:str):
    if numero == 1:
        return f"{Cores.VERDE}{texto}{Cores.RESET}"
    elif numero == 2:
        return f"{Cores.VERMELHO}{texto}{Cores.RESET}"
    else:
        return texto
    