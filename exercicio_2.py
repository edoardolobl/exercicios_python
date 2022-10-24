from math import sqrt


def calcular_lado(xa, ya, xb, yb):
    lado = sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
    return lado


# Coordenadas X e Y do ponto 1
x1 = float(input("Informe a coordenada X do Ponto 1:\n"))
y1 = float(input("Informe a coordenada Y do Ponto 1:\n"))

# Coordenadas X e Y do ponto 2
x2 = float(input("Informe a coordenada X do Ponto 2:\n"))
y2 = float(input("Informe a coordenada Y do Ponto 2:\n"))

# Coordenadas X e Y do ponto 3
x3 = float(input("Informe a coordenada X do Ponto 3:\n"))
y3 = float(input("Informe a coordenada Y do Ponto 3:\n"))

# Calcula os lados do triângulo
L1 = calcular_lado(x1, y1, x2, y2) # Distância entre P1 e P2
L2 = calcular_lado(x1, y1, x3, y3) # Distância entre P1 e P3
L3 = calcular_lado(x2, y2, x3, y3) # Distância entre P2 e P3

# Considera que as três condições de existência são verdadeiras
cond1 = True
cond2 = True
cond3 = True

# Verifica se algum lado é igual a zero
if L1 == 0 or L2 == 0 or L3 == 0:
    cond1 = False

# Verifica se algum lado é  maior que a soma dos outros dois
if L1 > (L2 + L3) or L2 > (L1 + L3) or L3 > (L1 + L2):
    cond2 = False

# Algum lado é menor que o módulo da diferença entre os outros dois
if L1 <= abs(L2 - L3) or L2 <= abs(L1 - L3) or L3 <= abs(L1 - L2):
    cond3 = False

triangulo = True

# ALguma condição de inexistência foi identificada?
if cond1 == False or cond2 == False or cond3 == False:
    triangulo = False
    print("\nNenhum triângulo formado.\nMotivo(s):")
    if cond1 == False:
        print("Pelo menos um dos lados é igual a 0")
    elif cond2 == False:
        print("Pelo menos um lado é maior que a soma dos outros dois.")
    elif cond3 == False:
        print("Um dos lados é menor ou igual ao módulo da diferença")

# Triângulo existe
elif L1 == L2 == L3:
    print("\nTriângulo equilátero.")
elif L1 != L2 and L1 != L3 and L2 != L3:
    print("\nTriângulo escaleno")
else:
    print("\nTriângulo isósceles")

# Todas as condições de existência do triângulo foram satisfeitas
if triangulo:
    print(f"Medida do lado 1: {L1}")
    print(f"Medida do lado 2: {L2}")
    print(f"Medida do lado 3: {L3}")

