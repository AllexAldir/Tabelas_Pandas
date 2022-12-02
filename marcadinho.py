import pandas as pd
from colorama import Fore
#desenvolvimento de tabela de um mercadinho 

#Login de acesso ao estoque:
senha = 2001

usuario = input(Fore.LIGHTRED_EX + "Digite o nome de usuário: " + Fore.RESET)
senha_ = int(input("Digite a senha de acesso: "))
while senha_ != senha:
    senha_ = int(input(Fore.GREEN + "ERRO Digite a senha novamente: " + Fore.RESET))

#Estrutura para o pandas

alimentos = []
valor = []
repetir = "Sim"

while repetir == "Sim":
    alimentos_ = input("Digite o nome do alimento aqui: ").capitalize()
    while alimentos_ in alimentos:
        alimentos_ = input("ERRO... alimento constado no banco de dados. Digite novamente: ").capitalize()
    alimentos.append(alimentos_)
    valor.append(float(input("Digite o valor desse item: ")))
    repetir = input("Deseja repetir a operação: 'sim' ou 'não': ").capitalize()

#Pandas:

dic_ = {"Alimentos":alimentos,"Valor":valor}

df_tabela = pd.DataFrame(dic_)

df_tabela = df_tabela.loc[:,"Valor Médio"] = 0   #Erro aqui

print(df_tabela)