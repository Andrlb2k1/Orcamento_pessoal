# Importando Tkinter
from tkinter import *
from tkinter import Tk, ttk

# Importando Pillow
from PIL import Image, ImageTk

# Importando barra de progresso
from tkinter.ttk import Progressbar

# Importando Mathplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# Cores
co0 = "#2e2d2b"  # preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

# Criando janela
janela = Tk()
janela.title()
janela.geometry('900x650')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# Criando frames para divisão da tela
frameCima = Frame(janela, width=1043, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=361, bg=co1, pady=20, relief="raised")
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief="flat")
frameBaixo.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

# Trabalhando no frame de cima
# Acessando a imagem
app_img = Image.open('log.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=" Orçamento pessoal", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

# Porcentagem -----------------------------------------------------------
def porcentagem():
	l_nome = Label(frameMeio, text="Porcentagem da receita gasta", height=1, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
	l_nome.place(x=7, y=5)

	style = ttk.Style()
	style.theme_use('default')
	style.configure("black.Horizontal.TProgressbar", background='#daed6b')
	style.configure("TProgressbar", thickness=25)

	bar = Progressbar(frameMeio, length=180, style="black.Horizontal.TProgressbar")
	bar.place(x=10, y=35)
	bar['value'] = 50

	valor = 50

	l_porcentagem = Label(frameMeio, text="{:,.2f}%".format(valor), anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
	l_porcentagem.place(x=200, y=35)

porcentagem()
janela.mainloop()