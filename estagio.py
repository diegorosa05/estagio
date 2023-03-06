# Recebe um número do usuário
numero = int(input("Digite um número: "))

# Inicializa as variáveis para a sequência de Fibonacci
fib_ant_ant = 0
fib_ant = 1

# Verifica se o número está na sequência de Fibonacci
while fib_ant < numero:
    fib_ant_ant, fib_ant = fib_ant, fib_ant + fib_ant_ant

if fib_ant == numero:
    print(numero, "pertence à sequência de Fibonacci")
else:
    print(numero, "não pertence à sequência de Fibonacci")
7