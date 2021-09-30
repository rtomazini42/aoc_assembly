entrada = open('entrada.txt', 'r') #abre o arquivo

for instrucao in entrada: #para cada linha na entrada
    instrucao = instrucao[2:] #retira o 0x
    instrucao = bin(int(instrucao, 32))
    print(instrucao)


entrada.close()
