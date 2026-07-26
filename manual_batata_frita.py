import time

def fritar_batata(quantidade_porcoes):
    print(f"\n--- 🍟 Como fritar Batatas 🍟 ---")
    print("1. modo caseiro: Descascar e cortar as batatas em palito / comprada: comprar um pacote de " \
    "batatas fritas congelado e pronto para fazer.")
    print("2. modo caseiro: Secar bem as batatas e garantir que estejam limpas / pacote pronto: desembalar as batatas"
    "e remover excesso de gelo caso tenha.")
    print("3. modo de preparo com óleo: Aquecer o óleo na temperatura ideal / modo de preparo na air frayer: " \
    "pré aquecer e manté-la fechada.")
    print("4. modo de preparo no óleo: Colocar as batatas no óleo quente e mexe-la levemente a cada 2-3min"
    "modo de preparo na air frayer: espalhar as batatas na air frayer de forma uniforme e fechar a tampa, deixe por 25-30min"
    "a 200°graus.")
    
    # Simulando o tempo de fritura com um loop
    minutos = 3
    while minutos <= 4:
        print(f"... Fritando... minuto {minutos}...")
        time.sleep(0.5) # Simula o tempo passando mais rápido
        minutos += 2
        
    print("5. Retirar, escorrer o óleo ou remover da air frayer, colocar num recipiente que dê para adicionar o sal e espalhar.")
    return "Batatas fritas douradas e crocantes prontas!"

# Executando
porcao_fds = fritar_batata(2)
print(f"Resultado: {porcao_fds}")