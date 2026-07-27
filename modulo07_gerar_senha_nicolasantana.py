"""
tabela ascii;

tabela hexadecimal;



"""

import random
import string

def gerar_senhas(tamanho):
    senha_caracteres = string.ascii_letters + string.digits + string.punctuation

    senha_gerada = ''.join(
        random.choice(senha_caracteres)for _ in range
        (tamanho)
    )

    return senha_gerada

if __name__ == "__main__":
    senha_usuario = gerar_senhas(12)
    print(f'sua senha gerada será: {senha_usuario}')