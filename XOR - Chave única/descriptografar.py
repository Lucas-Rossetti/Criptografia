# Script para descriptografar códigos binários com cifra de chave única
# Feito por Lucas Rossetti

# Pega a string com a cifra
c = list(input("Cifra: "))

# Pega a string com a chave
k = list(input("Chave: "))

# Resultado
r = []

# Transforma os números de string para integers e desfaz o XOR 
for i in range(len(c)):
    # c[i] é o inteiro dele mesmo
    c[i] = int(c[i])

    # k[i] é o inteiro dele mesmo
    k[i] = int(k[i])

    # Faz a operação contrária
    r.append((c[i] and (not k[i])) or ((not c[i]) and k[i])) 

# Faz uma string para o resultado
result = ''

# Loop
for i in range(len(c)):
    # Adiciona no resultado
    result += str(int(r[i])) 

# Escreve na tela o resultado
print("Resultado: {}".format(result))
