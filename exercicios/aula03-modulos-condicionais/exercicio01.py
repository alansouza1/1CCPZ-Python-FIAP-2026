produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade que você quer comprar: "))
desconto_percentual = float(input("Digite o percentual do seu desconto: "))

valor_bruto = preco * quantidade
valor_desconto = valor_bruto * (desconto_percentual / 100)
valor_final = valor_bruto - valor_desconto

print(f"\nProduto: {produto}\nValor bruto: R$ {valor_bruto}\nDesconto: R$ {valor_desconto}\nValor final: R$ {valor_final}")
