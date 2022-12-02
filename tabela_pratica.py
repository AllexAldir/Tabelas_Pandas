import pandas as pd
from colorama import Fore
import time
dic_itens = {}
produto = []
quant = []
valor = []
repetir = "sim"

while repetir == "sim":
    produto.append(input("Digite aqui o item: ").lower())
    quant.append(int(input("Digite aqui a quantidade: ")))
    valor.append(float(input("Digite aqui o valor do item: ")))
    repetir = input("Deseja repetir a operação? 'sim' ou 'não': ").lower()

dic_itens = {"Produto": produto, "Quantidade": quant, "Valor": valor}

# print(dic_itens)

df_tabela = pd.DataFrame(dic_itens)
# print(df_tabela)

df_tabela["Valor Total"] = df_tabela["Quantidade"] * df_tabela["Valor"] #Pegando o valor total:
print(df_tabela)
time.sleep(2)
despesas_pao = (df_tabela.loc[df_tabela["Produto"] == "pão",["Produto","Quantidade","Valor","Valor Total"]])
print(despesas_pao)
# df_tabela = df_tabela.drop(df_tabela.loc[df_tabela["Produto"] == "frango"], axis = 0)
# print(df_tabela)
