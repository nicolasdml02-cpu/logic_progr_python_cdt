def fazer_bolo(sabor, usar_cobertura=True):
    print(f"\n🥮 Iniciando: Bolo de {sabor.capitalize()}🥮")
    print("1. Reúna os seguintes ingredientes e utensílios: ovos, açúcar, óleo, farinha de trigo, " \
    ", fermento, manteiga, uma batedeira ou liquidificador e uma forma.")
    print("2. prepare a forma com manteiga nas lateterais e no fundo com uma camada fina.")
    print(f"3. Misturar o ingrediente principal: {sabor}, com os necessários, utilizando á batedeira")
    print("4. Colocar a mistura na forma e adicionar o fermento delicadamente.")
    print("5. Assar no forno a 180°C por 40 minutos.")
    
    if usar_cobertura:
        print("6. Adicionar uma cobertura caprichada por cima!")
        
    return f"Bolo de {sabor} quentinho e pronto para o café!"

# Criando bolos diferentes usando a mesma função
bolo_da_tarde = fazer_bolo("chocolate", usar_cobertura=True)
print(f"Resultado: {bolo_da_tarde}")

bolo_da_vovo = fazer_bolo("fubá", usar_cobertura=False)
print(f"Resultado: {bolo_da_vovo}")