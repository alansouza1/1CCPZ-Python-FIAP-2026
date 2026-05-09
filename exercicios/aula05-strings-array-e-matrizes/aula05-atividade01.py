nomes = ["Ana", "João", "Léo", "Bia"]

for i in range(len(nomes)):
    for j in range((i + 1), len(nomes)):
        print(f"{nomes[i]} + {nomes[j]}")
