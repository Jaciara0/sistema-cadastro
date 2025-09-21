from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from tkinter import Tk, StringVar, ttk
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkcalendar import DateEntry


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

# Criando os campos de entrada
# Campo: Nome do Item
l_nome = Label(frameMeio, text="Nome do Item", height=1, anchor=NW, font=('Segoe UI', 10, 'bold'), bg=co4, fg=co0)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width=30, justify='left', relief='solid')
e_nome.place(x=130, y=11)

# Campo: Área do Item
l_area = Label(frameMeio, text="Área do Item", height=1, anchor=NW, font=('Segoe UI', 10, 'bold'), bg=co4, fg=co0)
l_area.place(x=10, y=40)
e_area = Entry(frameMeio, width=30, justify='left', relief='solid')
e_area.place(x=130, y=41)

# Campo: Descrição do Item
l_desc = Label(frameMeio, text="Descrição do Item", height=1, anchor=NW, font=('Segoe UI', 10, 'bold'), bg=co4, fg=co0)
l_desc.place(x=10, y=70)
e_desc = Entry(frameMeio, width=30, justify='left', relief='solid')
e_desc.place(x=130, y=71)

# Campo: Marca/Modelo do Item
l_marca = Label(frameMeio, text="Marca/Modelo", height=1, anchor=NW, font=('Segoe UI', 10, 'bold'), bg=co4, fg=co0)
l_marca.place(x=10, y=100)
e_marca = Entry(frameMeio, width=30, justify='left', relief='solid')
e_marca.place(x=130, y=101)

# Campo: Data de Aquisição
l_data = Label(frameMeio, text="Data de Aquisição", height=1, anchor=NW, font=('Segoe UI', 10, 'bold'), bg=co4, fg=co0)
l_data.place(x=10, y=130)
e_data = DateEntry(
    frameMeio,
    width=12,
    background='darkblue',
    foreground='white',
    borderwidth=2,
    date_pattern='dd/mm/yyyy',
    font=('Segoe UI', 10)
)
e_data.place(x=130, y=131)

# Campo: Valor do Item
l_valor = Label(frameMeio, text="Valor do Item", height=1, anchor=NW, font=('Segoe UI', 10, 'bold'), bg=co4, fg=co0)
l_valor.place(x=10, y=160)
e_valor = Entry(frameMeio, width=30, justify='left', relief='solid')
e_valor.place(x=130, y=161)

# Campo: Número de Série
l_serie = Label(frameMeio, text="Número de Série", height=1, anchor=NW, font=('Segoe UI', 10, 'bold'), bg=co4, fg=co0)
l_serie.place(x=10, y=190)
e_serie = Entry(frameMeio, width=30, justify='left', relief='solid')
e_serie.place(x=130, y=191)

janela.mainloop()

# Criando botões do CRUD
# Botão para carregar imagem do item
l_carregar = Label(frameMeio, text="Imagem do Item", height=1, anchor=NW, font=('Segoe UI', 10, 'bold'), bg=co4, fg=co0)
l_carregar.place(x=10, y=220)

botao_carregar = Button(
    frameMeio, 
    compound=CENTER,
    anchor=CENTER,
    text="Carregar Imagem",
    width=30,
    overrelief=RIDGE,
    font=('Segoe UI', 10, 'bold'),
    bg=co2,
    fg=co4
)
botao_carregar.place(x=130, y=221)

# Botão para adicionar item
img_add = Image.open("add.png").resize((20, 20))
img_add = ImageTk.PhotoImage(img_add)

botao_inserir = Button(
    frameMeio,
    image=img_add,
    compound=LEFT,
    anchor=NW,
    text='     Adicionar Item',
    width=95,
    overrelief=RIDGE,
    font=('Segoe UI', 10, 'bold'),
    bg=co2,
    fg=co4
    
)
botao_inserir.place(x=330, y=10)

# Botão para atualizar item
img_update = Image.open("update.png").resize((20, 20))
img_update = ImageTk.PhotoImage(img_update)

botao_atualizar = Button(
    frameMeio,
    image=img_update,
    compound=LEFT,
    anchor=NW,
    text='     Atualizar Item',
    width=95,
    overrelief=RIDGE,
    font=('Segoe UI', 10, 'bold'),
    bg=co2,
    fg=co4
)
botao_atualizar.place(x=330, y=50)

# Botão para deletar item
img_delete = Image.open("delete.png").resize((20, 20))
img_delete = ImageTk.PhotoImage(img_delete)
botao_deletar = Button(
    frameMeio,
    image=img_delete,
    compound=LEFT,
    anchor=NW,
    text='     Deletar Item',
    width=95,
    overrelief=RIDGE,
    font=('Segoe UI', 10, 'bold'),
    bg=co2,
    fg=co4
)
botao_deletar.place(x=330, y=90)

# Botão ver item
img_item = Image.open("item.png").resize((20, 20))
img_item = ImageTk.PhotoImage(img_item)

botao_ver = Button(
    frameMeio,
    image=img_item,
    compound=LEFT,
    anchor=NW,
    text='     Ver Item',
    width=95,
    overrelief=RIDGE,
    font=('Segoe UI', 10, 'bold'),
    bg=co2,
    fg=co4
)
botao_ver.place(x=330, y=221)

# Labels para total e quantidade de itens
l_total = Label(
    frameMeio,
    width=14, 
    height=2, 
    anchor=CENTER,
    font=('Segoe UI', 12, 'bold'),
    bg=co1,
    fg=co4,
    relief=FLAT,
)
l_total.place(x=450, y=17)

l_valor_total = Label(
    frameMeio,
    text='  Valor Total de todos os itens  ', 
    width=14, 
    height=2, 
    anchor=NW,
    font=('Segoe UI', 12, 'bold'),
    bg=co1,
    fg=co4,
    relief=FLAT,
)
l_valor_total.place(x=450, y=12)

l_qtd = Label(
    frameMeio, 
    width=10, 
    height=2, 
    anchor=CENTER, 
    font=('Ivy 25 bold'), 
    bg=co7, 
    fg=co1, 
    relief=FLAT
)
l_qtd.place(x=450, y=90)

l_qtd_itens = Label(
    frameMeio, 
    text='Quantidade total de itens', 
    anchor=NW, 
    font=('Ivy 10 bold'), 
    bg=co7, 
    fg=co1
)
l_qtd_itens.place(x=460, y=92)


