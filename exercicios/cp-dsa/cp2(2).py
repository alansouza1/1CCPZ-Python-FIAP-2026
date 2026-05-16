import time
inicio = time.time()
soma = 0
for i in range (0, 10**6, 4):
    soma += i
    soma += i + 1
    soma += i + 2
    soma += i + 3
fim = time.time()
print(fim - inicio, "segundos")

n = 10**6
inicio = time.time()
soma = n * (n - 1) / 2
fim = time.time()
print(fim - inicio, "segundos")
