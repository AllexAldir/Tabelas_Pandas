import pandas as pd

carros = ["Cronos","Pulse","Mobi"]
valores = [57.000,70.000,40.000]
cont_cronos = 0
cont_pulse = 0
cont_mobi = 0


def cont_carro(ca):
    global cont_cronos, cont_mobi, cont_pulse

    if ca == "Cronos":
        cont_cronos += 1
        return cont_cronos

    if ca == "Mobi":
        cont_mobi += 1
        return cont_mobi

    if ca == "Pulse":
        cont_pulse += 1
        return cont_pulse

repetir = "sim"

while repetir == "sim":
    ca = input("Qual carro cliente quer: ").capitalize()
    while ca not in carros:
        ca = input("Modelo não identificado tente novamente: ").capitalize()
    indice = carros.index(ca)
    print(f"Carro: {ca} valor de: {valores[indice]} R$")
    cont_carro(ca)
    repetir = input("Deseja repetir a operação? 'sim' ou 'não': ").lower()

# tabela com pandas

di_c = {"Carros":carros,"Preços":valores,"Número de pedidos":[cont_cronos,cont_pulse,cont_mobi]}

df_tabela = pd.DataFrame(di_c)

df_tabela["Valores totais"] = df_tabela["Preços"] * df_tabela["Número de pedidos"]
print(df_tabela)