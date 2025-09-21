from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from tkinter import Tk, StringVar, ttk
from tkinter import filedialog as fd
from PIL import Image, ImageTk


co0 = "#355C7D"  # Azul profundo
co1 = "#725A7A"  # Roxo suave
co2 = "#C56C86"  # Rosa antigo
co3 = "#FF7582"  # Coral vibrante
co4 = "#F5F7FA"  # Branco gelo
co5 = "#2E2D2B"  # Preto neutro
co6 = "#E9EDF5"  # Cinza claro
co7 = "#403D3D"  # Cinza escuro
co8 = "#D9E4EC"  # Azul acinzentado
co9 = "#F1FAEE"  # Fundo alternativo

# Janela principal

janela = Tk()
janela.title("Sistema de Inventário")
janela.geometry("900x600")
janela.configure(background=co4)
janela.resizable(width=FALSE, height=FALSE)


# Estilo visual

style = ttk.Style(janela)
style.theme_use("clam")

style.configure("TLabel", background=co4, foreground=co0, font=("Segoe UI", 12))
style.configure("TButton", background=co2, foreground="white", font=("Segoe UI", 10, "bold"))
style.map("TButton", background=[("active", co3)])


# Frame superior (cabeçalho)

frameCima = Frame(janela, bg=co0, height=80)
frameCima.pack(fill=X)

# Ícone e título
app_img = Image.open("icone_lista.png")
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(
    frameCima,
    image=app_img,
    text=" Inventário Doméstico",
    compound=LEFT,
    font=('Segoe UI', 20, 'bold'),
    bg=co0,
    fg=co4,
    padx=10,
    pady=10
)
app_logo.pack(anchor=NW)

# Linha decorativa
linha = Frame(frameCima, bg=co2, height=2)
linha.pack(fill=X, padx=10, pady=(0, 5))


# Frame do meio (conteúdo principal)

frameMeio = Frame(janela, bg=co4, height=350, padx=20, pady=20)
frameMeio.pack(fill=X)


# Frame inferior (rodapé)

frameDireita = Frame(janela, bg=co0, height=170, padx=20, pady=10)
frameDireita.pack(fill=BOTH, expand=True)

# Executando a janela

janela.mainloop()




