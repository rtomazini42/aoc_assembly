'''Projeto MIPS - 2 entrega
Andre Monteiro
Luiz José
Paulo Aureliano
Fábio Hatem
Renan Tomazini'''

saida= open('saida.txt', 'w')

def imprime():
    for n in range(32):
        print("$" + str(n) + "="+ str(reg[n]), end=" ") #imprime os registradores formatado :)
        saida.write("$" + str(n) + "="+ str(reg[n]))
reg=[0,0,6,5,8,10,12,15,2,8,11,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #Inicia Banco de Registradores

#inicia_reg() #inicia os registradores
imprime() #imprime os registradores
print()




arq = open ('entrada.txt', 'r')
'''
while(arq.readline()!=""):
    a=arq.readline()
    print(a)

'''
def converter(s):
    i=0
    soma=0
    temp=0
    ind=len(s)-1
    while(i<len(s)):
        if(s[ind]=="1"):
            temp=pow(2, i)
            soma+=temp

        ind-=1

        i+=1

    return soma

with open('entrada.txt', 'r') as arq: #Inicia leitura do arquivo txt
	lista = arq.read().splitlines()



func=""
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
            func="add"
        elif((s1[26:])=="100001"):
            func="addu"
        elif((s1[26:])=="100100"):
            func="and"
        elif((s1[26:])=="011010"):
            func="div"
        elif((s1[26:])=="011011"):
            func="divu"
        elif((s1[26:])=="001000"):
            func="jr"
        elif((s1[26:])=="010000"):
            func="mfhi"
        elif((s1[26:])=="010010"):
            func="mflo"
        elif((s1[26:])=="011000"):
            func="mult"
        elif((s1[26:])=="011001"):
            func="multu"
        elif((s1[26:])=="100111"):
            func="nor"
        elif((s1[26:])=="100101"):
            func="or"
        elif((s1[26:])=="000000"):
            func="sll"
        elif((s1[26:])=="000100"):
            func="sllv"
        elif((s1[26:])=="101010"):
            func="slt"
        elif((s1[26:])=="000011"):
            func="sra"
        elif((s1[26:])=="000111"):
            func="srav"
        elif((s1[26:])=="000010"):
            func="srl"
        elif((s1[26:])=="000110"):
            func="srlv"
        elif((s1[26:])=="100010"):
            func="sub"
        elif((s1[26:])=="100011"):
            func="subu"
        elif((s1[26:])=="001100"):
            func="syscall"
        elif((s1[26:])=="100110"):
            func="xor"

        break

    if((s1[:6])=="000010"):
        func="j"
    elif((s1[:6])=="000011"):
        func="jal"
    elif((s1[:6])=="001000"):
        func="addi"
    elif((s1[:6])=="001001"):
        func="addiu"
    elif((s1[:6])=="000111"):
        func="bgtz"
    elif((s1[:6])=="000100"):
        func="beq"
    elif((s1[:6])=="000001"):
        func="bltz"
    elif((s1[:6])=="000110"):
        func="blez"
    elif((s1[:6])=="000101"):
        func="bne"
    elif((s1[:6])=="100000"):
        func="lb"
    elif((s1[:6])=="100100"):
        func="lbu"
    elif((s1[:6])=="001111"):
        func="lui"
    elif((s1[:6])=="100011"):
        func="lw"
    elif((s1[:6])=="001101"):
        func="ori"
    elif((s1[:6])=="101000"):
        func="sb"
    elif((s1[:6])=="001010"):
        func="slti"
    elif((s1[:6])=="101011"):
        func="sw"
    elif((s1[:6])=="001110"):
        func="xori"
    elif((s1[:6])=="001100"):
        func="andi"


    if(func=="add" or func=="sub" or func=="slt" or func=="and" or func=="or" or func=="xor" or func=="nor" or func=="addu" or func=="subu"):

        rs=converter(s1[6:11])
        rt=converter(s1[11:16])
        rd=converter(s1[16:21])

        if(func=="add"):
            reg[rd]=reg[rs]+reg[rt]
            saida.write("\n{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))
            print("\n{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))
            imprime()
            print()

        elif(func=="sub"):
            reg[rd]=reg[rs]-reg[rt]
            saida.write("\n{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))
            print("\n{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))
            imprime()
            print()

        elif(func=="and"):
            reg[rd]=reg[rs] & reg[rt]
            saida.write("\n{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))
            print("\n{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))
            imprime()
            print()

        elif(func=="or"):
            reg[rd]=reg[rs]|reg[rt]
            saida.write("\n{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))
            print("\n{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))
            imprime()
            print()

        elif(func=="xor"):
            reg[rd]=reg[rs]^reg[rt]
            saida.write("\n{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))
            print("\n{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))
            imprime()
            print()

        elif(func=="slt"):
            if(reg[rs]<reg[rt]):
                reg[rd]=1
            else:
                reg[rd]=0
            saida.write("\n{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))
            print("\n{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))
            imprime()
            print()

        elif(func=="nor"):
            
            saida.write("\n{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))
            print("\n{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))
            
            
        elif(func=="addu"):
            
            saida.write("\n{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))
            print("\n{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))
          
            
        elif(func=="subu"):
            
            saida.write("\n{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))
            print("\n{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))
           
                

    elif(func=="sll" or func=="srl" or func=="sra"):   

        sh=converter(s1[21:26])

        if(func=="sll"):
            saida.write("\n{}\t${}\t${}\t{}\n".format(func, rd, rs, sh))
            print("\n{}\t${}\t${}\t{}\n".format(func, rd, rs, sh))

        elif(func=="srl"):
            saida.write("\n{}\t${}\t${}\t{}\n".format(func, rd, rs, sh))
            print("\n{}\t${}\t${}\t{}\n".format(func, rd, rs, sh))

        elif(func=="sra"):
            saida.write("\n{}\t${}\t${}\t{}\n".format(func, rd, rs, sh))
            print("\n{}\t${}\t${}\t{}\n".format(func, rd, rs, sh))
            
       


    elif(func=="sllv" or func=="srlv" or func=="srav"):

        if(func=="sllv"):
            saida.write("{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))
            print("\n{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))

        elif(func=="srlv"):
            saida.write("{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))
            print("\n{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))

        elif(func=="srav"):
            saida.write("{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))
            print("\n{}\t${}\t${}\t${}\n".format(func, rd, rs, rt))
            
     


    elif(func=="mfhi" or func=="mflo"or func=="jr"):

        if(func=="mfhi"):
            saida.write("\n{}\t${}\n".format(func, rd))
            print("\n{}\t${}\n".format(func, rd))

        if(func=="mflo"):
            saida.write("\n{}\t${}\n".format(func, rd))
            print("\n{}\t${}\n".format(func, rd))

        if(func=="jr"):
            saida.write("\n{}\t${}\n".format(func, rd))
            print("\n{}\t${}\n".format(func, rd))
            
        

    elif(func=="div" or func=="divu" or func=="mult" or func=="multu"):

        if(func=="div"):
            saida.write("\n{}\t${}\t${}\n".format(func, rd, rs))
            print("\n{}\t${}\t${}\n".format(func, rd, rs))

        if(func=="divu"):
            saida.write("\n{}\t${}\t${}\n".format(func, rd, rs))
            print("\n{}\t${}\t${}\n".format(func, rd, rs))

        if(func=="mult"):
            saida.write("\n{}\t${}\t${}\n".format(func, rd, rs))
            print("\n{}\t${}\t${}\n".format(func, rd, rs))

        if(func=="multu"):
            saida.write("\n{}\t${}\t${}\n".format(func, rd, rs))
            print("\n{}\t${}\t${}\n".format(func, rd, rs))



    elif(func=="addi" or func=="slti" or func=="andi" or func=="ori" or func=="xori" or func=="beq" or func=="bne" or func=="addiu"):
        operando=converter(s1[16:])

        if(func=="addi"):
            reg[rd]=reg[rs]+operando
            saida.write("\n{}\t${}\t${}\t{}\n".format(func, rd, rs, operando))
            print("\n{}\t${}\t${}\t{}\n".format(func, rd, rs, operando))
            imprime()
            print()

        elif(func=="slti"):
            if(reg[rs]<operando):
                reg[rd]=1
            else:
                reg[rd]=0
            saida.write("\n{}\t${}\t${}\t{}\n".format(func, rd, rs, operando))
            print("\n{}\t${}\t${}\t{}\n".format(func, rd, rs, operando))
            imprime()
            print()

        elif(func=="andi"):
            reg[rd]=reg[rs]&operando
            saida.write("\n{}\t${}\t${}\t{}\n".format(func, rd, rs, operando))
            print("\n{}\t${}\t${}\t{}\n".format(func, rd, rs, operando))
            imprime()
            print()

        elif(func=="ori"):
            reg[rd]=reg[rs]|operando
            saida.write("\n{}\t${}\t${}\t{}\n".format(func, rd, rs, operando))
            print("\n{}\t${}\t${}\t{}\n".format(func, rd, rs, operando))
            imprime()
            print()

        elif(func=="xori"):
            saida.write("\n{}\t${}\t${}\t{}\n".format(func, rd, rs, operando))
            print("\n{}\t${}\t${}\t{}\n".format(func, rd, rs, operando))

        elif(func=="beq"):
            saida.write("\n{}\t${}\t${}\t{}\n".format(func, rd, rs, operando))
            print("\n{}\t${}\t${}\t{}\n".format(func, rd, rs, operando))

        elif(func=="bne"):
            saida.write("\n{}\t${}\t${}\t{}\n".format(func, rd, rs, operando))
            print("\n{}\t${}\t${}\t{}\n".format(func, rd, rs, operando))

        elif(func=="addiu"):
            saida.write("\n{}\t${}\t${}\t{}\n".format(func, rd, rs, operando))
            print("\n{}\t${}\t${}\t{}\n".format(func, rd, rs, operando))

        
            
       

    elif(func=="lw" or func=="sw" or func=="lb" or func=="lbu" or func=="sb"):

        if(func=="lw"):
            saida.write("\n{}\t${}\t{}(${})\n".format(func, rd, operando, rs))
            print("\n{}\t${}\t{}(${})\n".format(func, rd, operando, rs))

        elif(func=="sw"):
            saida.write("\n{}\t${}\t{}(${})\n".format(func, rd, operando, rs))
            print("\n{}\t${}\t{}(${})\n".format(func, rd, operando, rs))

        elif(func=="lb"):
            saida.write("\n{}\t${}\t{}(${})\n".format(func, rd, operando, rs))
            print("\n{}\t${}\t{}(${})\n".format(func, rd, operando, rs))

        elif(func=="lbu"):
            saida.write("\n{}\t${}\t{}(${})\n".format(func, rd, operando, rs))
            print("\n{}\t${}\t{}(${})\n".format(func, rd, operando, rs))

        elif(func=="sb"):
            saida.write("\n{}\t${}\t{}(${})\n".format(func, rd, operando, rs))
            print("\n{}\t${}\t{}(${})\n".format(func, rd, operando, rs))
            

        

    elif(func=="lui" or func=="bltz"):

        rs=converter(s1[6:11])
        operando=converter(s1[16:])

        if(func=="lui"):
            saida.write("\n{}\t${}\t{}\n".format(func, rs, operando))
            print("\n{}\t${}\t{}\n".format(func, rs, operando))
            
        elif(func=="bltz"):
            saida.write("\n{}\t${}\t{}\n".format(func, rs, operando))
            print("\n{}\t${}\t{}\n".format(func, rs, operando))

        

    elif(func=="j" or func=="jal"):

        jump=converter(s1[:6])

        if(func=="j"):
            saida.write("\n{}\t{}\n".format(func,jump))
            print("\n{}\t{}\n".format(func,jump))

        elif(func=="jal"):
            saida.write("\n{}\t{}\n".format(func,jump))
            print("\n{}\t{}\n".format(func,jump))
            
            
    elif(func=="syscall"):

        saida.write("\n{}\n".format(func))
        print("\n{}\n".format(func))




    cont+=1

print("Gravado em saida.txt")
saida.close()