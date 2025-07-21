from validador import validar_cpf
from utils import cor

print("=== Validador de CPF ===")
print("Digite 'sair' para encerrer.\n")

while True:
    cpf_usuario = input("Digite o cpf: ").strip()

    if cpf_usuario.upper().strip() == 'SAIR':
        print("Encerrando o validador...")
        break

    if validar_cpf(cpf_usuario):
        print(cor(1, "CPF válido.\n"))
    else:
        print(cor(2, "CPF inválido.\n"))
