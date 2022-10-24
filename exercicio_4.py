from tabulate import tabulate

def carrega_arquivo():
    arquivo = open("usuarios.txt", "r")

    dict_usuario = {}

    for linha in arquivo:
        linha = linha.strip()
        colunas = linha.split('\t')
        dict_usuario[colunas[0]] = colunas[1]

    arquivo.close()
    return dict_usuario

def converte_bytes(valor_byte):
    valor_megabyte = float(valor_byte) * (9.537*(10**-7))
    return round(valor_megabyte, 2)

def porcentagem_uso(valor, total):
    porcentagem = (float(valor) * 100) / float(total)
    return round(porcentagem, 2)

def sort_uso(e):
    return e[3]

def construir_tabela(lista, total, medio):
    print("ACME Inc.\tUso do espaço em disco pelos usuários\n")
    print(tabulate(lista, headers=["ID", "Usuário", "Espaço utilizado (MB)", "% do uso"], tablefmt="github"))
    print(f"Espaço total ocupado: {total} MB\nEspaço médio ocupado: {medio} MB")

# Tratar os dados da tabela

tabela_usuario = carrega_arquivo()

total_espaco = 0

for usuario in tabela_usuario:
    total_espaco = total_espaco + float(tabela_usuario[usuario])

total_espaco = converte_bytes(total_espaco)

lista_usuario = []

nr_usuario = 1

for usuario in tabela_usuario:
    usuario_mbyte = converte_bytes(tabela_usuario[usuario])
    porcentagem_usuario = porcentagem_uso(usuario_mbyte, total_espaco)
    temp_lista = [nr_usuario, usuario, usuario_mbyte, porcentagem_usuario]
    lista_usuario.append(temp_lista)
    nr_usuario = nr_usuario + 1

espaco_medio = round((total_espaco / (nr_usuario - 1)), 2)

# Montar a tabela

print("Bem vindo ao Controle de Cotas de Disco - ACME Inc.")
input_usuario = int(input("Ordenar os usuários pelo percentual de espaço ocupado?\n(1) Sim\n(2) Não\n"))

if input_usuario < 1 or input_usuario > 2:
    raise Exception("Opção inválida")

if input_usuario == 1:
    lista_usuario.sort(reverse=True, key=sort_uso)
    construir_tabela(lista_usuario, total_espaco, espaco_medio)
else:
    construir_tabela(lista_usuario, total_espaco, espaco_medio)