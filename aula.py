numero = int(input("insira um número: "))

print("tabela de multiplicação para", numero,":")
for i in range(1, 11):
    produto = numero + i
    print(numero, "x", i, "=", produto)