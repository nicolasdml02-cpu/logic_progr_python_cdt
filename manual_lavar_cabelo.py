def aplicar_shampoo():
    print("   -> Aplicar no couro cabeludo 2 'dedos' de shampoo ou mais à depender do comprimento do cabelo.")
    print("   -> Massagear suavemente com as pontas dos dedos.")
    print("   -> Enxaguar completamente.")

def aplicar_condicionador_ou_mascára_hidratante():
    print("   -> Aplicar condicionador apenas no comprimento e pontas e um tan menor em relação ao shampoo.")
    print("   -> Deixar agir por 4 à 6 minutos.")
    print("   -> Enxaguar bem.")

# Função principal que coordena o processo
def lavar_cabelo(usar_condicionador_ou_máscara=True):
    print("\n---🧴 Iniciando processo de Lavar o Cabelo e hidratar🧴---")
    print("1. Entrar no chuveiro e molhar bem o cabelo.")
    print("2. Passo do Shampoo:")
    aplicar_shampoo() # Chama a primeira subfunção
    
    if usar_condicionador_ou_máscara:
        print("3. Passo do Condicionador ou máscara hidratante:")
        aplicar_condicionador_ou_mascára_hidratante() # Chama a segunda subfunção
        
    print("4. Tirar o excesso de água com a toalha.")
    return "Cabelo limpinho, cheiroso e pronto para pentear com creme pós-banho!"

# Executando
cabelo_pronto = lavar_cabelo(usar_condicionador_ou_máscara=True)
print(f"Resultado: {cabelo_pronto}")