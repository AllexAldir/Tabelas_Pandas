import pandas as pd
import numpy as np
# exemplo de biblioteca

livros = ["João e maria","Pinoquio","Hobbit"]
cont1 = 0
cont2 = 0
cont3 = 0
repetir = "sim"


def conta_l(livro):
    global cont1, cont2, cont3

    if livro == "João e maria":
            cont1 += 1
    if livro == "Pinoquio":
            cont2 += 1
    if livro == "Hobbit":
            cont3 += 1
    return cont1, cont2, cont3

print("nome dos livros: ")
for i in livros:
    print(i)

while repetir == "sim":
    livro = input("Digite aqui o nome do livro o qual você deseja escolher: ").capitalize()
    while livro not in livros:
        livro = input("Livro não encontrado tente novamente: ").capitalize()
        print(livro)
    conta_l(livro)
    print(
        f"Até o momento o resultado é: 'João e Maria' com {cont1}, 'Pinoquio' com {cont2} e Hobbit com {cont3}")
    repetir = input("Deseja repetir 'sim' ou 'não': ").lower()    

dic_tab = {"Livros":livros,"Quantidades":[cont1,cont2,cont3]}

df_tab = pd.DataFrame(dic_tab)
print(df_tab.describe()) #Status
