
import random
import os
import sys
import time
import webbrowser
import tkinter as tk
from tkinter import messagebox


def sortear():
    opcao = 5
    numSorteado = random.randint(1, opcao)
    #print("O número sorteado é: ", numSorteado)

    # try:
    #     escolha = int(input(f"Escolha um número entre 1 e {opcao}: "))
    #     if escolha < 1 or escolha > opcao:
    #         raise ValueError("Número fora de intervalo! ")
        
    # except ValueError as e:
    #     print(f"entrada inválida: {e} tente de novo!")
    #     sortear()

    def verificarEscolha(escolha):
        if escolha == numSorteado:
            print("Bye Bye word, seu pc será desligado!👻 ")
            messagebox.showerror("Perdeu", "o computado sera desigado")
            time.sleep(5)
            if sys.platform == "win32":
                os.system("shutdown /s /t 1")
            elif sys.platform == 'linux' or sys.platform == 'linux2':
                os.system("shutdown now")
            elif sys.platform == "dar32 win":
                os.system("shutdown -h now")

        else:
            print("Você está seguro, por enquanto! ")
            messagebox.showerror("ufa","voce esta seguro, por enquanto!")
            sortear()
    janela = tk.Toplevel()
    janela.title("Algoritmo de sorteio")
    tk.Label(janela, text="Escolha um número entre 1 e 6").pack(pady=10)

    for i in range(1,6):
        tk.Button(janela, text=str(i), command=lambda i=i: [janela.destroy(),
        verificarEscolha(i)]).pack(pady=5)

        def exibirRegras()
        regras = (
            "Regras do jogo: \n"
            "1. Escolha um numero entre 1 e 6. \n"
            "2. Se voce escolher o n sorteado, o Pc sera desligado! \n"
            "3. Se não for, o jogo continua. \n"
            "4. Boa sorte, vai precisar!"
        )
        messagebox.showerror("Regras", regras)

    def sair():
        root.destroy()


root = tk.Tk()
root.title("Jogo do evento aleatório")
tk.Label(root, text="Bem-vindo ao Jogo de Evento Aleatório!", font=("Arial", 20)).pack(pady=15)
tk.Button(root, text="Iniciar Jogo", width=20, command=sortear).pack(pady=10)
tk.Button(root, text="Ver regras", width=20, command=exibirRegras).pack(pady=10)
tk.Button(root, text="Sair", width=20, command=sair).pack(pady=10)

root.mainloop()