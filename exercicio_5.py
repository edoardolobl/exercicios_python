escolha_fruta = int(input("Qual fruta deseja comprar?\n(1) Morango\n(2) Maçã\n(3) Morango e Maçã\n"))

if escolha_fruta < 1 or escolha_fruta > 3:
    raise Exception("Opção inválida")

if escolha_fruta == 1 or escolha_fruta == 2:
    quantidade_fruta = float(input("Qual a quantidade desejada? (em Kg)\n"))
else:
    quantidade_morango = float(input("Qual a quantidade de morango desejada? (em Kg)\n"))
    quantidade_maca = float(input("Qual a quantidade de maçã desejada? (em Kg)\n"))


def calculo_valor(quantidade)

if quantidade < 5:
    preco_morango = 2.50 * quantidade
    preco_maca = 1.8 * quantidade

elif quantidade > 5 and quantidade <= 8:
    preco_morango = 2.20 * quantidade
    preco_maca = 1.50 * quantidade

if quantidade > 8 or valor_total > 25.0:
    valor_total = valor_total * 0.1
