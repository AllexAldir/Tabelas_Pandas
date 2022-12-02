import pandas as pd
from datetime import date
#Vendas aparelhos

repetir = "sim"

produtos = []
valores = []

while repetir == "sim":
    produto = input("Digite o nome do aparelho: ").capitalize()
    while produto in produtos:
        produto = input("Produto encontrado no nosso banco de dados. Digite o nome de outro celular: ").capitalize()
    produtos.append(produto)
    valores.append(float(input("Digite o valor dele R$: ")))
    # valores.sort() #deixando em ordem
    repetir = input("Deseja repetir a operação? 'sim' ou 'não': ").lower()

for i in range(len(valores)):
    print(f"Número do produto: {i}, Produto: {produtos[i]}, Valor: {valores[i]}")


dic_ = {"Produtos":produtos,"Valores":valores}

df_tabela = pd.DataFrame(dic_)

print(df_tabela)

