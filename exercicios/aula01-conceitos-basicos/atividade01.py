# Atividade 1: Exercício A
nome = input("Digite o seu nome: ")
print(f"Seja bem-vindo, {nome}!")

# Atividade 1: Exercício B
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
print(f"A soma de {num1} e {num2} é: {soma}")

# Atividade 1: Exercício C
ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
idade = ano_atual - ano_nascimento
print(f"Você tem {idade} anos.")

# Atividade 1: Exercício D
preco = float(input("Digite o preço do produto: "))
desconto = preco * 0.27
preco_com_desconto = preco - desconto
print(f"O preço com desconto é: {preco_com_desconto:.2f}")
