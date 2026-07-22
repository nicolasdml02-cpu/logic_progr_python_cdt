'''





'''

#1. Abre o arquivo para leitura ('r')
leitura_arquivo = open('arquivo_leitura_nicolasantana.txt', 'r', encoding="utf-8")

#2. Lê todo o conteúdo do arquivo
conteudo_arquivo = leitura_arquivo.read()

#3. Exibe o conteúdo na tela
print(conteudo_arquivo)

#4. Fecha o arquivo
leitura_arquivo.close()