arq = open ('entrada.txt', 'r')

for line in arq:
    print(str(bin(line)))