import pandas as pd
# from datetime import date as d

repetir = "sim"
l_faturamento = []
l_meses = []
l_porcent = []

for i in range(0,12):
    l_meses.append(input("Digite o mês: ").capitalize())
    l_faturamento.append(float(input("digite o valor desse faturamento: ")))
    
for indice, nome in enumerate(l_meses):
    print(f"mês: {nome} e seu valor: {l_faturamento[indice]}")

#Fazendo a representação em porcentagem:

soma = sum(l_faturamento)
valor_medio = soma / len(l_faturamento)

for i in l_faturamento:
    porcent = (i / soma) * 100
    porcent = round(porcent,2)
    l_porcent.append(porcent)
    
dic_ = {"Meses":l_meses,"Faturamento_Por_Mes":l_faturamento,"Representação de Porcentagem por mês":l_porcent}

df_ = pd.DataFrame(dic_)

print(df_)