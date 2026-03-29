nome = input("Digite o seu nome: ")
hora_valor = float(input("Digite o valor da sua hora trabalhada: "))
quantidade_horas = float(input("Digite a quantidade horas trabalhadas no mês: "))
bonus = float(input("Digite o valor do bônus: "))
desconto_mes = float(input("Digite o desconto total do mês: "))

salario_bruto = (hora_valor * quantidade_horas) + bonus
salario_liquido = salario_bruto - desconto_mes

print(f"\nColaborador: {nome}\nSalário bruto: R$ {salario_bruto}\nSalário líquido: R$ {salario_liquido}")
