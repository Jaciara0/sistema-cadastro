from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from tkinter import Tk, StringVar, ttk
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkcalendar import DateEntry

from view import atualizar_form, inserir_form, deletar_form, ver_item

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

# Variáveis globais
imagem_string = ""
l_imagem_exibicao = None

# Função para carregar imagem
def escolher_imagem():
    global imagem_string
    imagem_string = fd.askopenfilename()
    print(f"Imagem selecionada: {imagem_string}")

# Função inserir
def inserir():
    global imagem_string
    nome = e_nome.get()
    area = e_area.get()
    descricao = e_desc.get()
    marca = e_marca.get()
    data_aquisicao = e_data.get()
    valor = e_valor.get()
    serie = e_serie.get()
    
    lista_inserir = (nome, area, descricao, marca, data_aquisicao, valor, serie, imagem_string, 1)
    
    for i in lista_inserir:
        if i == "":
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return
        
    inserir_form(lista_inserir)
    messagebox.showinfo("Sucesso", "Item adicionado com sucesso!")
    
    # Limpando os campos
    e_nome.delete(0, END)
    e_area.delete(0, END)
    e_desc.delete(0, END)
    e_marca.delete(0, END)
    e_data.delete(0, END)
    e_valor.delete(0, END)
    e_serie.delete(0, END)
    imagem_string = ""
    
    # Atualizando a tabela
    mostrar()

# Função atualizar
def atualizar():
    try:
        treev_dados = tree.focus()
        if not treev_dados:
            messagebox.showwarning("Aviso", "Selecione um item para atualizar.")
            return
            
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        
        if not treev_lista:
            messagebox.showwarning("Aviso", "Selecione um item válido.")
            return
            
        # Limpando os campos
        e_nome.delete(0, END)
        e_area.delete(0, END)
        e_desc.delete(0, END)
        e_marca.delete(0, END)
        e_data.delete(0, END)
        e_valor.delete(0, END)
        e_serie.delete(0, END)
        
        # Preenchendo os campos com os dados selecionados
        id = int(treev_lista[0])
        e_nome.insert(END, treev_lista[1])
        e_area.insert(END, treev_lista[2])
        e_desc.insert(END, treev_lista[3])
        e_marca.insert(END, treev_lista[4])
        e_data.set_date(treev_lista[5])
        e_valor.insert(END, treev_lista[6])
        e_serie.insert(END, treev_lista[7])
        
        # Função interna para confirmar atualização
        def confirmar_atualizacao():
            global imagem_string
            nome = e_nome.get()
            area = e_area.get()
            descricao = e_desc.get()
            marca = e_marca.get()
            data_aquisicao = e_data.get()
            valor = e_valor.get()
            serie = e_serie.get()
            imagem = imagem_string or treev_lista[8] if len(treev_lista) > 8 else imagem_string
            
            lista_atualizar = (nome, area, descricao, marca, data_aquisicao, valor, serie, imagem, id)
            
            for i in lista_atualizar[:-1]:
                if i == "":
                    messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
                    return
                    
            atualizar_form(lista_atualizar)
            messagebox.showinfo("Sucesso", "Item atualizado com sucesso!")
            
            # Limpando os campos
            e_nome.delete(0, END)
            e_area.delete(0, END)
            e_desc.delete(0, END)
            e_marca.delete(0, END)
            e_data.delete(0, END)
            e_valor.delete(0, END)
            e_serie.delete(0, END)
            imagem_string = ""
            
            botao_confirmar.destroy()
            mostrar()
        
        # Botão confirmar atualização
        botao_confirmar = Button(
            frameMeio, 
            text="CONFIRMAR ATUALIZAÇÃO", 
            width=20,
            command=confirmar_atualizacao,
            bg=co3,
            fg="white",
            font=('ivy 8 bold')
        )
        botao_confirmar.place(x=330, y=130)
        
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao selecionar item: {str(e)}")

# Função deletar
def deletar():
    try:
        treev_dados = tree.focus()
        if not treev_dados:
            messagebox.showwarning("Aviso", "Selecione um item para deletar.")
            return
            
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        
        if not treev_lista:
            messagebox.showwarning("Aviso", "Selecione um item válido.")
            return
            
        valor = treev_lista[0]

        # Confirmação antes de deletar
        resposta = messagebox.askyesno("Confirmar", "Tem certeza que deseja deletar este item?")
        if resposta:
            deletar_form([valor])
            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')
            mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um item na tabela')
    except Exception as e:
        messagebox.showerror('Erro', f'Erro ao deletar item: {str(e)}')

# Função para ver imagem
def ver_imagem():
    global l_imagem_exibicao

    try:
        treev_dados = tree.focus()
        if not treev_dados:
            messagebox.showwarning("Aviso", "Selecione um item para ver a imagem.")
            return
            
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        
        if not treev_lista:
            messagebox.showwarning("Aviso", "Selecione um item válido.")
            return
            
        # CORREÇÃO: Passar o ID diretamente como inteiro
        id_item = int(treev_lista[0])
        iten = ver_item(id_item)
        
        if not iten or not iten[0][8]:
            messagebox.showinfo("Info", "Este item não possui imagem.")
            return
            
        imagem = iten[0][8]

        # Limpar imagem anterior se existir
        if l_imagem_exibicao:
            l_imagem_exibicao.destroy()

        # Abrindo a imagem
        try:
            imagem_aberta = Image.open(imagem)
            imagem_aberta = imagem_aberta.resize((170, 170))
            imagem_tk = ImageTk.PhotoImage(imagem_aberta)

            l_imagem_exibicao = Label(frameMeio, image=imagem_tk, bg=co4)
            l_imagem_exibicao.image = imagem_tk
            l_imagem_exibicao.place(x=700, y=10)
            
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir a imagem: {str(e)}")

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um item na tabela')
    except Exception as e:
        messagebox.showerror('Erro', f'Erro ao carregar imagem: {str(e)}')

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

# Botão para carregar imagem do item
l_imagem = Label(frameMeio, text="Imagem do item", height=1, anchor=NW, font=('Segoe UI', 10, 'bold'), bg=co4, fg=co0)
l_imagem.place(x=10, y=220)

botao_carregar = Button(
    frameMeio, 
    compound=CENTER, 
    anchor=CENTER, 
    text="CARREGAR", 
    width=30, 
    overrelief=RIDGE,  
    font=('ivy 8'), 
    bg=co2, 
    fg=co5,
    command=escolher_imagem
)
botao_carregar.place(x=130, y=221)

# Botão Adicionar
img_add = Image.open('add.png').resize((20, 20))
img_add = ImageTk.PhotoImage(img_add)

botao_inserir = Button(
    frameMeio, 
    image=img_add, 
    compound=LEFT, 
    anchor=NW, 
    text="   ADICIONAR", 
    width=95, 
    overrelief=RIDGE,  
    font=('ivy 8'), 
    bg=co2, 
    fg=co5,
    command=inserir
)
botao_inserir.place(x=330, y=10)

# Botão Atualizar
img_update = Image.open('update.png').resize((20, 20))
img_update = ImageTk.PhotoImage(img_update)

botao_atualizar = Button(
    frameMeio, 
    image=img_update, 
    compound=LEFT, 
    anchor=NW, 
    text="   ATUALIZAR", 
    width=95, 
    overrelief=RIDGE,  
    font=('ivy 8'), 
    bg=co2, 
    fg=co5,
    command=atualizar
)
botao_atualizar.place(x=330, y=50)

# Botão Deletar
img_delete = Image.open('delete.png').resize((20, 20))
img_delete = ImageTk.PhotoImage(img_delete)

botao_deletar = Button(
    frameMeio, 
    image=img_delete, 
    compound=LEFT, 
    anchor=NW, 
    text="   DELETAR", 
    width=95, 
    overrelief=RIDGE,  
    font=('ivy 8'), 
    bg=co2, 
    fg=co5,
    command=deletar
)
botao_deletar.place(x=330, y=90)

# Botão Ver Imagem
img_item = Image.open('item.png').resize((20, 20))
img_item = ImageTk.PhotoImage(img_item)

botao_ver = Button(
    frameMeio, 
    image=img_item, 
    compound=LEFT, 
    anchor=NW, 
    text="   VER IMAGEM", 
    width=95, 
    overrelief=RIDGE,  
    font=('ivy 8'), 
    bg=co2, 
    fg=co5,
    command=ver_imagem
)
botao_ver.place(x=330, y=221)

# Labels para Total e Quantidade
l_total = Label(
    frameMeio, 
    width=14, 
    height=2, 
    anchor=CENTER, 
    font=('Ivy 17 bold'), 
    bg=co2, 
    fg=co5, 
    relief=FLAT
)
l_total.place(x=450, y=17)

l_valor_total = Label(
    frameMeio, 
    text='  Valor Total de todos os itens  ', 
    anchor=NW, 
    font=('Ivy 10 bold'), 
    bg=co2, 
    fg=co5
)
l_valor_total.place(x=450, y=12)

l_qtd = Label(
    frameMeio, 
    width=10, 
    height=2, 
    anchor=CENTER, 
    font=('Ivy 25 bold'), 
    bg=co2, 
    fg=co5, 
    relief=FLAT
)
l_qtd.place(x=450, y=90)

l_qtd_itens = Label(
    frameMeio, 
    text='Quantidade total de itens', 
    anchor=NW, 
    font=('Ivy 10 bold'), 
    bg=co2, 
    fg=co5
)
l_qtd_itens.place(x=460, y=92)

# Função para mostrar os dados na tabela
def mostrar():
    # Limpar tabela existente
    for item in tree.get_children():
        tree.delete(item)
    
    # Lista de itens
    lista_itens = []  
    
    # Inserindo os dados na tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)
        
    # Cálculo do total e quantidade de itens
    try:
        quantidade = [float(item[6]) for item in lista_itens if item[6]]
        Total_valor = sum(quantidade)
        Total_itens = len(lista_itens)
        
        # Atualizando os labels de total e quantidade
        l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
        l_qtd['text'] = Total_itens
    except:
        l_total['text'] = 'R$ 0,00'
        l_qtd['text'] = '0'

# Configurando a Treeview
tabela_head = ['#Item', 'Nome', 'Área', 'Descrição', 'Marca/Modelo', 'Data de Aquisição', 'Valor (R$)', 'Nº Série']

tree = ttk.Treeview(
    frameDireita, 
    selectmode="extended", 
    columns=tabela_head, 
    show="headings"
)

# Scrollbars
vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)
tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

# Posicionando a Treeview e as scrollbars
tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')
frameDireita.grid_rowconfigure(0, weight=12)
frameDireita.grid_columnconfigure(0, weight=1)

# Configuração das colunas
hd = ["center"] * len(tabela_head)
h = [40, 150, 100, 160, 130, 100, 100, 100]

for n, col in enumerate(tabela_head):
    tree.heading(col, text=col.title(), anchor=CENTER)
    tree.column(col, width=h[n], anchor=hd[n])

# Chamada da função para mostrar dados
mostrar()

# Execução da janela
janela.mainloop()