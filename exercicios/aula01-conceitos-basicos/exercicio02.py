preco = float(input("Digite o preço do produto: "))
desconto = 0.05
if preco > 200:
    desconto = 0.25

preco_com_desconto = preco - (preco * desconto)
print(f"O preço com desconto é: {preco_com_desconto:.2f}")
