# Função para o cálculo de grandezes elétricas
def formula(tensao=0.0, resistencia=0.0, corrente=0.0):
    if tensao == 0:
        tensao = resistencia * corrente
        print(f"A Tensão é de {tensao}V")
    elif resistencia == 0:
        resistencia = tensao / corrente
        print(f"A Resistência é de {resistencia}Ω")
    elif corrente == 0:
        corrente = tensao / resistencia
        print(f"A Corrente é de {corrente}A")

# Criar menu do usuário
# Usar a função "print"


print("**************************************")
print("CÁCULO DE GRANDEZAS ELÉTRICAS")
print("**************************************")
print("1. Tensão (em Volt)")
print("2. Resistência (em Ohm)")
print("3. Corrente (em Ampére)")
print("**************************************")

# Receber input do usuário com a grandeza a ser calculada
# Usar a função "input"
selecao_user = input("Qual grandeza deseja calcular?\n")

# Transforma o input do usuário em um inteiro
# Usar a função "int"
selecao = int(selecao_user)

# Valida a seleção do usuário
if selecao < 1 or selecao > 3:
    print("Opção inválida")

# Compara o input do usuário com as opções listadas e oferece um feedback da seleção
# Usar if e elif para estabelecer as condições de comparação
# Após a seleção o usuário deve informar as outras duas variáveis para o cálculo
if selecao == 1:
    print("Você selecionou Tensão")
    R = float(input("Informe o valor da Resistência (em Ohm)\n"))
    i = float(input("Informe o valor da Corrente (em Ampére)\n"))
    formula(0.0, R, i)
elif selecao == 2:
    print("Você selecionou Resistência")
    U = float(input("Informe o valor da Tensão (em Volt)\n"))
    i = float(input("Informe o valor da Corrente (em Ampére)\n"))
    formula(U, 0.0, i)
elif selecao == 3:
    print("Você selecionou Corrente")
    U = float(input("Informe o valor da Tensão (em Volt)\n"))
    R = float(input("Informe o valor da Resistência (em Ohm)\n"))
    formula(U, R, 0.0)
