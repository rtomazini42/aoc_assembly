
'''
arq = open ('entrada.txt', 'r')

while(arq.readline()=!""):
    a=arq.readline()
    print(a)

'''

with open('entrada.txt', 'r') as arq: #Inicia leitura do arquivo txt
	lista = arq.read().splitlines()

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
           print("add")
        elif((s1[26:])=="100001"):
            print("addu")
        elif((s1[26:])=="100100"):
            print("and")
        elif((s1[26:])=="011010"):
            print("div")
        elif((s1[26:])=="011011"):
            print("divu")
        elif((s1[26:])=="001000"):
            print("jr")
        elif((s1[26:])=="010000"):
            print("mfhi")
        elif((s1[26:])=="010010"):
            print("mflo")
        elif((s1[26:])=="011000"):
            print("mult")
        elif((s1[26:])=="011001"):
            print("multu")
        elif((s1[26:])=="100111"):
            print("nor")
        elif((s1[26:])=="100101"):
            print("or")
        elif((s1[26:])=="000000"):
            print("sll")
        elif((s1[26:])=="000100"):
            print("sllv")
        elif((s1[26:])=="101010"):
            print("slt")
        elif((s1[26:])=="000011"):
            print("sra")
        elif((s1[26:])=="000111"):
            print("srav")
        elif((s1[26:])=="000010"):
            print("srl")
        elif((s1[26:])=="000110"):
            print("srlv")
        elif((s1[26:])=="100010"):
            print("sub")
        elif((s1[26:])=="100011"):
            print("subu")
        elif((s1[26:])=="001100"):
            print("syscall")
        elif((s1[26:])=="100110"):
            print("xor")
        break
    if((s1[:6])=="000010"):
        print("j")
    elif((s1[:6])=="000011"):
        print("jal")
    elif((s1[:6])=="001000"):
        print("addi")
    elif((s1[:6])=="001001"):
        print("addiu")
    elif((s1[:6])=="001100"):
        print("andi")
    elif((s1[:6])=="000111"):
        print("bgtz")
    elif((s1[:6])=="000100"):
        print("beq")
    elif((s1[:6])=="000001"):
        print("bltz")
    elif((s1[:6])=="000110"):
        print("blez")
    elif((s1[:6])=="000101"):
        print("bne")
    elif((s1[:6])=="100000"):
        print("lb")
    elif((s1[:6])=="100100"):
        print("lbu")
    elif((s1[:6])=="001111"):
        print("lui")
    elif((s1[:6])=="100011"):
        print("lw")
    elif((s1[:6])=="001101"):
        print("ori")
    elif((s1[:6])=="101000"):
        print("sb")
    elif((s1[:6])=="001010"):
        print("slti")
    elif((s1[:6])=="101011"):
        print("sw")
    elif((s1[:6])=="001110"):
        print("xori")
   
    #print(s1)

        
        
    cont+=1
    

                  
        
     
       
   


   


    
    






