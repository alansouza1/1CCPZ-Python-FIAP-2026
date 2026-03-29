peca1 = input("Digite o nome da primeira peça: ")
peca1_preco = float(input("Digite o preço: "))
quantidade_peca1 = int(input("Digite a quantidade: "))

peca2 = input("Digite o nome da segunda peça: ")
peca2_preco = float(input("Digite o preço: "))
quantidade_peca2 = int(input("Digite a quantidade: "))

peca1_total = peca1_preco * quantidade_peca1
peca2_total = peca2_preco * quantidade_peca2

valor_pago = peca1_total + peca2_total

print(f"O valor total a ser pago dos produtos {peca1} e {peca2} será de R${valor_pago:.2f}.")

