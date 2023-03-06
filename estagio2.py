string = input("Digite uma string: ")  # entrada da string pelo usuário
string_invertida = ""

# laço que percorre a string de trás para frente e adiciona cada caractere na nova string
for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

print("String invertida: ", string_invertida)  # exibe a nova string invertida
