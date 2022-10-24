def calculo_valor(quantidade_morango=0.0, quantidade_maca=0.0):

    valor_total = 0
    quantidade_total = quantidade_morango + quantidade_maca

    if quantidade_morango <= 5:
        preco_morango = 2.50 * quantidade_morango
        valor_total = valor_total + preco_morango
    else:
        preco_morango = 2.20 * quantidade_morango
        valor_total = valor_total + preco_morango

    if quantidade_maca <= 5:
        preco_maca = 1.8 * quantidade_maca
        valor_total = valor_total + preco_maca
    else:
        preco_maca = 1.50 * quantidade_maca
        valor_total = valor_total + preco_maca

    if quantidade_total > 8 or valor_total > 25.0:
        valor_total = valor_total - (valor_total * 0.1)
        return round(valor_total, 2)
    else:
        return round(valor_total, 2)


def quantidade_cliente(fruta):
    quantidade = float(input(f"Qual a quantidade de {fruta} desejada? (em Kg)\n"))
    return quantidade


escolha_fruta = int(input("Qual fruta deseja comprar?\n(1) Morango\n(2) Maçã\n(3) Morango e Maçã\n"))

if escolha_fruta < 1 or escolha_fruta > 3:
    raise Exception("Opção inválida")

if escolha_fruta == 1:
    quantidade_morango = quantidade_cliente("morango")
    valor = calculo_valor(quantidade_morango, 0.0)
    print(f"{quantidade_morango}Kg de morango por R${valor}")
elif escolha_fruta == 2:
    quantidade_maca = quantidade_cliente("maçã")
    valor = calculo_valor(0.0, quantidade_maca)
    print(f"{quantidade_maca}Kg de morango por R${valor}")
else:
    quantidade_morango = quantidade_cliente("morango")
    quantidade_maca = quantidade_cliente("maçã")
    valor = calculo_valor(quantidade_morango, quantidade_maca)
    print(f"{quantidade_morango}Kg de morango e {quantidade_maca}Kg de maçã por R${valor}")


