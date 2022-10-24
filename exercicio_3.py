alt_1 = float(input("Digite a altura da 1a pessoa (em metros):\n"))
alt_2 = float(input("Digite a altura da 2a pessoa (em metros):\n"))
alt_3 = float(input("Digite a altura da 3a pessoa (em metros):\n"))

alturas = [alt_1, alt_2, alt_3]
alturas.sort()

mais_baixo = alturas[0]
est_media = alturas[1]
mais_alto = alturas[2]

print(f"\n{mais_alto}m, {est_media}m e {mais_baixo}m")
