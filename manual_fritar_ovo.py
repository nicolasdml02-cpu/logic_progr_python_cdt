def fazer_ovo_frito(tipo_ponto_da_gema):
    print('🍳fazendo ovo frito - sistema simples🍳')
    print('1. réuna os seguintes ingredientes: quantidade de ovos à seu critério, sal, óleo, uma espátula e' \
    ' uma frigideira')
    print('2. ligue o fogão e pré-aqueça a frigideira levemente, adicione óleo e em seguida quebre os ovos' \
    ' na frigideira')
    print('3. deixe os ovos pegarem forma, e após pegarem cor e formarem "um só"(em caso de mais de 1 ovo) vire ' \
    'o lado utilizando a espátula e deixe por mais 2-3min à depender do eu ponto de gema')
    print('4. após fritar o ovo, espere esfriar levemente, e sirva à seu critério(lanche ou almoço/jantar)')

    if tipo_ponto_da_gema.lower() == 'firme':
        resultado = 'firme'
    else:
        resultado = 'mole'

    return resultado

meu_ponto_da_gema = fazer_ovo_frito('firme')
print(f'meu ovo frito com a gema: {meu_ponto_da_gema} ')