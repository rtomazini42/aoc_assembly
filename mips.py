
'''
arq = open ('entrada.txt', 'r')

while(arq.readline()=!""):
    a=arq.readline()
    print(a)

'''

with open('entrada.txt', 'r') as arq: #Inicia leitura do arquivo txt
	lista = arq.read().splitlines()

saida = open('saida.txt', 'w')

cont=0

while(cont<len(lista)): #Ler a lista e começa converter hexa -> bin
    s1=""
    a=lista[cont]
    h=(a[2:])

    for i in h:
        if(i=='0'):
            s='0000'
        elif(i=='1'):
            s='0001'
        elif(i=='2'):
            s='0010'
        elif(i=='3'):
            s='0011'
        elif(i=='4'):
            s='0100'
        elif(i=='5'):
            s='0101'
        elif(i=='6'):
            s='0110'
        elif(i=='7'):
            s='0111'
        elif(i=='8'):
            s='1000'
        elif(i=='9'):
            s='1001'
        elif(i=='a'):
            s='1010'
        elif(i=='b'):
            s='1011'
        elif(i=='c'):
            s='1100'
        elif(i=='d'):
            s='1101'
        elif(i=='e'):
            s='1110'
        elif(i=='f'):
            s='1111'


        s1=s1+s

    while((s1[:6])=="000000"): # identifica tipo R
        if((s1[26:])=="100000"):
           #print("add")
           saida.write("add")
           saida.write("\n")
        elif((s1[26:])=="100001"):
            saida.write("addu")
            saida.write("\n")
        elif((s1[26:])=="100100"):
            saida.write("and")
            saida.write("\n")
        elif((s1[26:])=="011010"):
            saida.write("div")
            saida.write("\n")
        elif((s1[26:])=="011011"):
            saida.write("divu")
            saida.write("\n")
        elif((s1[26:])=="001000"):
            saida.write("jr")
            saida.write("\n")
        elif((s1[26:])=="010000"):
            saida.write("mfhi")
            saida.write("\n")
        elif((s1[26:])=="010010"):
            saida.write("mflo")
            saida.write("\n")
        elif((s1[26:])=="011000"):
            saida.write("mult")
            saida.write("\n")
        elif((s1[26:])=="011001"):
            saida.write("multu")
            saida.write("\n")
        elif((s1[26:])=="100111"):
            saida.write("nor")
            saida.write("\n")
        elif((s1[26:])=="100101"):
            saida.write("or")
            saida.write("\n")
        elif((s1[26:])=="000000"):
            saida.write("sll")
            saida.write("\n")
        elif((s1[26:])=="000100"):
            saida.write("sllv")
            saida.write("\n")
        elif((s1[26:])=="101010"):
            saida.write("slt")
            saida.write("\n")
        elif((s1[26:])=="000011"):
            saida.write("sra")
            saida.write("\n")
        elif((s1[26:])=="000111"):
            saida.write("srav")
            saida.write("\n")
        elif((s1[26:])=="000010"):
            saida.write("srl")
            saida.write("\n")
        elif((s1[26:])=="000110"):
            saida.write("srlv")
            saida.write("\n")
        elif((s1[26:])=="100010"):
            saida.write("sub")
            saida.write("\n")
        elif((s1[26:])=="100011"):
            saida.write("subu")
            saida.write("\n")
        elif((s1[26:])=="001100"):
            saida.write("syscall")
            saida.write("\n")
        elif((s1[26:])=="100110"):
            saida.write("xor")
            saida.write("\n")
        break
    if((s1[:6])=="000010"):
        saida.write("j")
        saida.write("\n")
    elif((s1[:6])=="000011"):
        saida.write("jal")
        saida.write("\n")
    elif((s1[:6])=="001000"):
        saida.write("addi")
        saida.write("\n")
    elif((s1[:6])=="001001"):
        saida.write("addiu")
        saida.write("\n")
    elif((s1[:6])=="001100"):
        saida.write("andi")
        saida.write("\n")
    elif((s1[:6])=="000111"):
        saida.write("bgtz")
        saida.write("\n")
    elif((s1[:6])=="000100"):
        saida.write("beq")
        saida.write("\n")
    elif((s1[:6])=="000001"):
        saida.write("bltz")
        saida.write("\n")
    elif((s1[:6])=="000110"):
        saida.write("blez")
        saida.write("\n")
    elif((s1[:6])=="000101"):
        saida.write("bne")
        saida.write("\n")
    elif((s1[:6])=="100000"):
        saida.write("lb")
        saida.write("\n")
    elif((s1[:6])=="100100"):
        saida.write("lbu")
        saida.write("\n")
    elif((s1[:6])=="001111"):
        saida.write("lui")
        saida.write("\n")
    elif((s1[:6])=="100011"):
        saida.write("lw")
        saida.write("\n")
    elif((s1[:6])=="001101"):
        saida.write("ori")
        saida.write("\n")
    elif((s1[:6])=="101000"):
        saida.write("sb")
        saida.write("\n")
    elif((s1[:6])=="001010"):
        saida.write("slti")
        saida.write("\n")
    elif((s1[:6])=="101011"):
        saida.write("sw")
        saida.write("\n")
    elif((s1[:6])=="001110"):
        saida.write("xori")
        saida.write("\n")

    #print(s1)



    cont+=1
