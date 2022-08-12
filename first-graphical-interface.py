from tkinter import *

def pegar_informações_pessoais():


    resultado = "Apertou o botão pq é besta hahaha"

    texto_informaçoes_pessoais["text"] = resultado

janela = Tk()
janela.title('Informações pessoais')

texto_orientaçao = Label(janela, text="Formulário pessoal")
texto_orientaçao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Responder", command=pegar_informações_pessoais)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_informaçoes_pessoais = Label(janela, text="")
texto_informaçoes_pessoais.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()