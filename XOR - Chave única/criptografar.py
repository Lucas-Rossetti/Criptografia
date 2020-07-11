# Script para criptografar códigos binários com cifra de chave única
# Feito por Lucas Rossetti

# Imports
import random

# Pega a string com o código binário
c = list(input("Código: "))

# Cria a array que vai ficar com a chave única
k = []

# Transforma os números de string para integers e faz o XOR 
for i in range(len(c)):
    # c[i] é o inteiro dele mesmo
    c[i] = int(c[i])

    # Appenda nas chaves o número aleatório
    k.append(bool(random.getrandbits(1)))

    # Faz o XOR
    c[i] = (c[i] and (not k[i])) or ((not c[i]) and k[i])

# Faz uma string para a chave e uma para a cifra
# Chave
key = ''

# Cifra
cypher = ''

# Loop
for i in range(len(c)):
    # Adiciona na chave
    key += str(int(k[i]))

    # Adiciona na cifra
    cypher += str(int(c[i]))

# Escreve na tela o resultado e a chave
print("Cifra: {}".format(cypher))
print("Chave única: {}".format(key))
