import numpy as np

# Loop tradicional
soma = 0
for i in range(10**6):
    soma += i

print(soma)
# Numpy vetorizado
soma_np = np.sum(np.arange(10**6))
print(soma_np)
