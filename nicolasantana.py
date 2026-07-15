'''
COMO FAZER UM HAMBURGUER;

1. passo: primeiramente, reúna os seguintes ingrentes e utensílios: uma frigideira,
uma tampa adequada à frigideira, 1 ou mais hamburgueres, e uma espatula.

2. passo: desembale o hamburguer(s), coloque a frigideira em uma das bocas do fogão em fogo baixo 
e coloque o hamburguer(s) no centro da frigideira e antes da frigideira esquentar demais,
caso haja mais de 1 hamburguer, posicione eles de acordo com o espaço da frigideira.

3. passo: após o segundo passo, tampe a frigideira já com o hamburguer(s) sendo feito,
após aproximadamente entre 6-8 minutos, destampe a frigideira e vire de lado do hamburguer(s)
utilizando a espatula, e tampe novamente a frigideira após isso,
lembre-se sempre de deixar em fogo bixo até o fim.

4. passo: após o terceiro passo, aguarde entre 4-5 minutos, destampe novamente a frigideira e
verifique o estado do hamburguer(s) com a espatula, caso não apresente nenhuma parte clara ou 
diferente da maioria, desligue o fogo, tampe novamente, e espere esfriar para servir, 
caso apresente, deixe por mais 2 minutos no fogo baixo e tampado, após isso, verifique novamente
com a espatula, desligue o fogo, tampe novamente, e espere esfriar para servir.

'''
def fazer_hamburguer(tipo_ponto_da_carne):
    print('🍔fazendo hamburguer - sistema simples🍔')
    print('1. primeiramente, reúna os seguintes ingrentes e utensílios: uma frigideira' \
    'uma tampa adequada à frigideira, 1 ou mais hamburgueres, e uma espatula.')
    print('2. desembale o hamburguer(s), coloque a frigideira em uma das bocas do fogão em fogo baixo ' \
    'e coloque o hamburguer(s) no centro da frigideira e antes da frigideira esquentar demais,' \
    'caso haja mais de 1 hamburguer, posicione eles de acordo com o espaço da frigideira.')
    print('3. após o segundo passo, tampe a frigideira já com o hamburguer(s) sendo feito,' \
    'após aproximadamente entre 6-8 minutos, destampe a frigideira e vire de lado do hamburguer(s)' \
    'utilizando a espatula, e tampe novamente a frigideira após isso,' \
    'lembre-se sempre de deixar em fogo bixo até o fim.')
    print('4. após o terceiro passo, aguarde entre 4-5 minutos, destampe novamente a frigideira e' \
    'verifique o estado do hamburguer(s) com a espatula, caso não apresente nenhuma parte clara ou ' \
    'diferente da maioria, desligue o fogo, tampe novamente, e espere esfriar para servir, ' \
    'caso apresente, deixe por mais 2 minutos no fogo baixo e tampado, após isso, verifique novamente' \
    'com a espatula, desligue o fogo, tampe novamente, e espere esfriar para servir.')

    if tipo_ponto_da_carne.lower() == 'no ponto':
        resultado = 'no ponto'
    else:
        resultado = 'mal passado'

    return resultado

meu_hamburguer = fazer_hamburguer('no ponto')
print(f'meu_hamburguer está:{meu_hamburguer} ')