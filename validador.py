def validar_cpf(cpf: str) -> bool:
    # Remove caracteres que não forem dígitos
    cpf = ''.join(filter(str.isdigit, cpf))

    # CPF deve ter 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais (ex: 11111111111)
    if cpf == cpf[0] * 11:
        return False

    # Calcula o 1º dígito verificador
    soma1 = 0
    for i in range(9):
        soma1 += int(cpf[i]) * (10 - i)
    resto1 = soma1 % 11
    if resto1 < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto1

    # Calcula o 2º dígito verificador
    soma2 = 0
    for i in range(9):
        soma2 += int(cpf[i]) * (11 - i)
    soma2 += digito1 * 2
    resto2 = soma2 % 11
    if resto2 < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto2

    # Verifica se os dígitos calculados são iguais aos dois últimos do CPF
    return cpf[-2:] == f"{digito1}{digito2}"
