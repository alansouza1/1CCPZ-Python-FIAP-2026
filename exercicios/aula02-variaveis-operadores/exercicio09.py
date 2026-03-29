valor_produto = float(input("Digite o valor do produto: "))
valor_pago = float(input("Digite o valor pago: "))

troco = valor_pago - valor_produto

print(f"O valor do seu troco é de R$ {troco:.2f}")

