# %%

import random
from secrets import choice

def setup_porta():
    portas = {i:"Não ha nada aqui!" for i in range(1,4)}
    premio = random.choice([1,2,3])
    portas[premio] = "Vencedor!"
    return portas, premio

def update_portas(portas, premio, escolha):
    portas_livres = [i for i in portas.keys() if i not in (premio, escolha) ]
    porta_aberta = random.choice(portas_livres)
    return porta_aberta

def input_porta( choices=[1,2,3] ):
    escolha = 0
    while escolha not in choices:
        try:
            escolha = int(input(f'Entre com a porta selecionada {choices}: '))
        except ValueError as err:
            pass
    return escolha

def main():
    portas, premio = setup_porta()
    escolha = input_porta()
    porta_aberta = update_portas(portas, premio, escolha)

    novas_escolhas = [i for i in portas.keys() if i not in (porta_aberta,)]

    print(f"Na porta {porta_aberta} não há nada. Deseja trocar de porta?")
    escolha = input_porta(novas_escolhas)
    print(portas[escolha])

if __name__ == "__main__":
    main()