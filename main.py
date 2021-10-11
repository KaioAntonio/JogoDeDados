import random
from tkinter import *

class jogarDados(object):

    def __init__(self, mestre):
        quadro = Frame(mestre)
        quadro.pack()

        self.label = Label(mestre, font= ("times",200))
        botao = Button(mestre, text = "Jogue os dados", command = self.rolar)
        botao.place(x=200,y=0)

    def rolar(self):
        simbolos =["\u2680", "\u2681", "\u2682","\u2683","\u2684","\u2685","\u2686"]
        self.label.config(text=f"{random.choice(simbolos)}{random.choice(simbolos)}")
        self.label.pack()

if __name__ == "__main__":
    inicio = Tk()
    inicio.title("Jogar os dados")
    inicio.geometry("500x300")
    jogarDados(inicio)
    inicio.mainloop()
