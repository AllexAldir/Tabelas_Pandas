import pandas as pd

repetir = "sim"
l_salario = []
l_nome = []
l_anos = []
new_sal = []
juros = []

while repetir == "sim":
    l_nome.append(input("Digite aqui o seu nome: ").capitalize())
    l_salario.append(float(input("Digite aqui o salário do trabalhador: ")))
    l_anos.append(int(input("Digite aqui a quantidade de anos que o trabalhador está nessa empresa: ")))
    repetir = input("Deseja repetir a operação? 'sim' ou 'não': ").lower()

#Agora reajustar o salário de cada trabalhador:

for ano,sal in zip(l_anos,l_salario):
    if ano >= 1 and ano <=3:
        new = (sal * 0.1) + sal
        juros.append("10%")
        new_sal.append(new)

    if ano >3 and ano <=5:
        new = (sal * 0.13) + sal
        juros.append("13%")
        new_sal.append(new)

    if ano > 5 and ano <= 8:
        new = (sal * 0.15) + sal
        juros.append("15%")
        new_sal.append(new)

    if ano > 8 and ano <= 10:
        new = (sal * 0.18) + sal
        juros.append("18%")
        new_sal.append(new)

    if ano > 10:
        new = (sal * 0.2) + sal
        juros.append("20%")
        new_sal.append(new)

dic_ = {"Nome Funcionario":l_nome,"Salário Antigo":l_salario,"Juros":juros,"Novo Salário":new_sal}

df_tabela = pd.DataFrame(dic_)

print(df_tabela)

indice_s = l_salario.index(max(l_salario))
nome_s = l_nome[indice_s]

print(f"""
Relatorio:

Maior salário s/reajuste: {max(l_salario)} com o nome de: {nome_s}

Maior salário c/reajuste: {max(new_sal)} logicamente de: {nome_s}

""")
