entrada = open('entrada.txt', 'r') #abre o arquivo

for instrucao in entrada: #para cada linha na entrada
    instrucao = instrucao[2:] #retira o 0x
    if instrucao[:2] == "00":
        print("é aritmetico")