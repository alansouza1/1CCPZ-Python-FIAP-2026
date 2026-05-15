temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]
maior_registro_critico = 0
sala_com_maior_registro_critico = 1

for i in range(len(temperaturas)):
    total = 0
    registros_criticos = 0

    for j in range(len(temperaturas[i])):
        temperatura = temperaturas[i][j]
        total += temperatura
        if temperatura >= 33:
            registros_criticos += 1

    media = total / len(temperaturas[i])
    print(f"Sala {i + 1}")
    print(f"Média: {media}")
    print(f"Registros críticos: {registros_criticos}")
    print()

    if registros_criticos > maior_registro_critico:
        maior_registro_critico = registros_criticos
        sala_com_maior_registro_critico = i + 1

print(f"Sala com maior risco: Sala {sala_com_maior_registro_critico}")
