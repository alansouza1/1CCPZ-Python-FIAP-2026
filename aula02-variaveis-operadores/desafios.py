# Desafio 01
nome = input("Digite o seu nome: ")

print(f"Seja bem vindo {nome}")

# Desafio 02
dia = input("Digite o dia do seu nascimento: ")
mes = input("Digite o mês do seu nascimento: ")
ano = input("Digite o ano do seu nascimento: ")

print(f"Sua data de nascimento é {dia}/{mes}/{ano}")

# Desafio 03
primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite outro número: "))

soma = primeiro_numero + segundo_numero

print(f"{primeiro_numero} + {segundo_numero} = {soma}")

produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade que você quer comprar: "))
desconto_percentual = float(input("Digite o percentual do seu desconto: "))

valor_bruto = preco * quantidade
valor_desconto = valor_bruto * (desconto_percentual / 100)
valor_final = valor_bruto - valor_desconto

print(f"\nProduto: {produto}\nValor bruto: R$ {valor_bruto}\nDesconto: R$ {valor_desconto}\nValor final: R$ {valor_final}")




nome = input("Digite o seu nome: ")
hora_valor = float(input("Digite o valor da sua hora trabalhada: "))
quantidade_horas = float(input("Digite a quantidade horas trabalhadas no mês: "))
bonus = float(input("Digite o valor do bônus: "))
desconto_mes = float(input("Digite o desconto total do mês: "))

salario_bruto = (hora_valor * quantidade_horas) + bonus
salario_liquido = salario_bruto - desconto_mes

print(f"\nColaborador: {nome}\nSalário bruto: R$ {salario_bruto}\nSalário líquido: R$ {salario_liquido}")
