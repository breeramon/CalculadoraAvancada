from tkinter import *
from tkinter import ttk
import math

root =Tk()
root.title("Calculadora")
root.geometry("+500+80")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure('mainframe.TFrame', background="#DBDBDB")


mainframe = ttk.Frame(root, style='mainframe.TFrame')
mainframe.grid(column=0, row=0, sticky=NSEW)
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)

estilos_label1 = ttk.Style()
estilos_label1.configure('label1.TLabel', font=("Arial", 15), ANCHOR="e")

estilos_label2 = ttk.Style()
estilos_label2.configure('label2.TLabel', font=("Arial", 40), ANCHOR="e")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)

entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style='label1.TLabel')
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=NSEW)

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style='label2.TLabel')
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=NSEW)

#estilos para os botões
estilos_botao_numeros = ttk.Style()
estilos_botao_numeros.configure('Botao_numeros.TButton', font=("Arial", 22), width=5, background="#FFFFFF", relief="flat")
estilos_botao_numeros.map('Botao_numeros.TButton', background=[('active', '#B9B9B9')])

estilos_botao_apagar = ttk.Style()
estilos_botao_apagar.configure('Botao_apagar.TButton', font=("Arial", 22), width=5, background="#CECECE", relief="flat")
estilos_botao_apagar.map('Botao_apagar.TButton', foreground=[('active', '#FF0000')], background=[('active', '#858585')])

estilos_botao_restantes = ttk.Style()
estilos_botao_restantes.configure('Botao_restantes.TButton', font=("Arial", 22), width=5, background="#CECECE", relief="flat")
estilos_botao_restantes.map('Botao_restantes.TButton', backgroud=[('active', '#858585')])

botao0 = ttk.Button(mainframe, text="0", style="Botao_numeros.TButton")
botao1 = ttk.Button(mainframe, text="1", style="Botao_numeros.TButton")
botao2 = ttk.Button(mainframe, text="2", style="Botao_numeros.TButton")
botao3 = ttk.Button(mainframe, text="3", style="Botao_numeros.TButton")
botao4 = ttk.Button(mainframe, text="4", style="Botao_numeros.TButton")
botao5 = ttk.Button(mainframe, text="5", style="Botao_numeros.TButton")
botao6 = ttk.Button(mainframe, text="6", style="Botao_numeros.TButton")
botao7 = ttk.Button(mainframe, text="7", style="Botao_numeros.TButton")
botao8 = ttk.Button(mainframe, text="8", style="Botao_numeros.TButton")
botao9 = ttk.Button(mainframe, text="9", style="Botao_numeros.TButton")

botao_apagar = ttk.Button(mainframe, text=chr(9003), style="Botao_apagar.TButton")
botao_apagar_tudo = ttk.Button(mainframe, text="C", style="Botao_apagar.TButton")
botao_parentesis1 = ttk.Button(mainframe, text="(", style="Botao_restantes.TButton")
botao_parentesis2 = ttk.Button(mainframe, text=")", style="Botao_restantes.TButton")
botao_ponto = ttk.Button(mainframe, text=".", style="Botao_restantes.TButton")

botao_divisao = ttk.Button(mainframe, text=chr(247), style="Botao_restantes.TButton")
botao_multiplicacao = ttk.Button(mainframe, text="X", style="Botao_restantes.TButton")
botao_subtracao = ttk.Button(mainframe, text="-", style="Botao_restantes.TButton")
botao_soma = ttk.Button(mainframe, text="+", style="Botao_restantes.TButton")

botao_igual = ttk.Button(mainframe, text="=", style="Botao_restantes.TButton")
botao_raiz_quadrada = ttk.Button(mainframe, text="√", style="Botao_restantes.TButton")

#colocando os botões na tela
botao_parentesis1.grid(column=0, row=2, sticky=NSEW)
botao_parentesis2.grid(column=1, row=2, sticky=NSEW)
botao_apagar_tudo.grid(column=2, row=2, sticky=NSEW)
botao_apagar.grid(column=3, row=2, sticky=NSEW)

botao7.grid(column=0, row=3, sticky=NSEW)
botao8.grid(column=1, row=3, sticky=NSEW)
botao9.grid(column=2, row=3, sticky=NSEW)
botao_divisao.grid(column=3, row=3, sticky=NSEW)

botao4.grid(column=0, row=4, sticky=NSEW)
botao5.grid(column=1, row=4, sticky=NSEW)
botao6.grid(column=2, row=4, sticky=NSEW)
botao_multiplicacao.grid(column=3, row=4, sticky=NSEW)

botao1.grid(column=0, row=5, sticky=NSEW)
botao2.grid(column=1, row=5, sticky=NSEW)
botao3.grid(column=2, row=5, sticky=NSEW)
botao_soma.grid(column=3, row=5, sticky=NSEW)

botao0.grid(column=0, row=6, columnspan=2, sticky=NSEW) #sticky serve para esticar o botão(widget) para completar os espaços vazios
botao_ponto.grid(column=2, row=6, sticky=NSEW)
botao_subtracao.grid(column=3, row=6, sticky=NSEW)

botao_igual.grid(column=0, row=7, columnspan=3, sticky=NSEW)
botao_raiz_quadrada.grid(column=3, row=7, sticky=NSEW)

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

root,mainloop()