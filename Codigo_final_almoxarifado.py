from tkinter import *
from tkinter import messagebox

dados_cliente = {}
mercadorias = {}

COR_FUNDO = "#013220"
COR_TEXTO = "white"
COR_BOTAO = "#006400"
COR_ERRO = "#8B0000"

root = Tk()
root.title("Sistema de Almoxarifado")
root.geometry("500x400")
root.configure(bg=COR_FUNDO)

def mostrar_tela(frame):
    frame.tkraise()

def criar_cadastro():
    usuario = entry_user_cadastro.get().strip()
    senha = entry_senha_cadastro.get().strip()
    resenha = entry_resenha_cadastro.get().strip()

    if usuario in dados_cliente:
        messagebox.showerror("Erro", "Esse usuário ja existe")
    elif senha != resenha:
        messagebox.showerror("Erro", "As senha não coincidem")
    else:
        dados_cliente[usuario] = {"senha": senha}
        messagebox.showinfo("Sucesso", "Usuario cadastrado com sucesso!")
        entry_user_cadastro.delete(0, END)
        entry_senha_cadastro.delete(0, END)
        entry_resenha_cadastro.delete(0, END)
        mostrar_tela(frame_login)

def login():
    usuario = entry_user_login.get().strip()
    senha = entry_senha_login.get().strip()
    if usuario in dados_cliente and dados_cliente[usuario]["senha"] == senha:
        messagebox.showerror("Sucesso", f"Bem-vindo, {usuario}!")
        mostrar_tela(frame_menu)
    else:
        messagebox.showerror("Erro", "Usuario ou senha incorretos")

def cadastrar_mercadoria():
    nome = entry_nome_mercadoria.get().strip()
    if nome in mercadorias:
        messagebox.showerror("Erro", "Essa mercadoria ja esta cadastrada.")

    else:
        try:
            qtd = int(entry_qtd_mercadoria.get())
            preço = float(entry_preço_mercadoria.get())
            mercadorias[nome] = {"quantidade": qtd, "preço": preço}
            messagebox.showinfo("Sucesso", f"Mercadoria '{nome}' cadastrada!")
        except ValueError:
            messagebox.showerror("Erro", "Digite valores válidos para quantidade e preço.")
    entry_nome_mercadoria.delete(0, END)
    entry_qtd_mercadoria.delete(0, END)
    entry_preço_mercadoria.delete(0, END)

def consultar_mercadorias():
    texto.delete(1.0, END)
    if not mercadorias:
        texto.insert(END, "Nenhuma mercadoria cadastrada. \n")
    else:
        for nome, info in mercadorias.items():
            texto.insert(END, f"{nome}: {info['quantidade']} unidades - R${info['preço']:.2f}\n")

#inserir
def inserir_mercadorias():
    nome = entry_nome_inserir.get().strip()
    try:
        qtd = int(entry_qtd_inserir.get())
        if nome not in mercadorias:
            messagebox.showerror("Erro", "Essa mercadoria não está cadastrada.")
        else:
            mercadorias[nome]["quantidade"] += qtd
            messagebox.showinfo("Sucesso", f"{qtd} unidades adicionadas a '{nome}'!")
            entry_nome_inserir.delete(0, END)
            entry_qtd_inserir.delete(0, END)
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido para a quantidade.")


for frame in range(5):
    Frame(root, bg=COR_FUNDO).grid(row=0, column=0, sticky='nsew')

frame_login = Frame(root, bg=COR_FUNDO)
frame_cadastro = Frame(root, bg=COR_FUNDO)
frame_menu = Frame(root, bg=COR_FUNDO)
frame_mercadorias = Frame(root, bg=COR_FUNDO)
frame_consulta = Frame(root, bg=COR_FUNDO)
frame_inserir = Frame(root, bg=COR_FUNDO)


#login
Label(frame_login, text="LOGIN", bg=COR_FUNDO, fg=COR_TEXTO, font=("Arial", 20, "bold")).pack(pady=20)
Label(frame_login, text="Usuario:", bg=COR_FUNDO, fg=COR_TEXTO).pack()
entry_user_login = Entry(frame_login)
entry_user_login.pack()
Label(frame_login, text="Senha:", bg=COR_FUNDO, fg=COR_TEXTO).pack()
entry_senha_login = Entry(frame_login, show="*")
entry_senha_login.pack(pady=5)
Button(frame_login, text="Entrar", bg=COR_BOTAO, fg=COR_TEXTO, command=login).pack(pady=5)
Button(frame_login, text="Cadastrar", bg=COR_BOTAO, fg=COR_TEXTO, command=lambda: mostrar_tela(frame_cadastro)).pack()

#cadastro
Label(frame_cadastro, text="Cadastro", bg=COR_FUNDO, fg=COR_TEXTO, font=("Arial", 20, "bold")).pack(pady=20)
Label(frame_cadastro, text="Usuario:", bg=COR_FUNDO, fg=COR_TEXTO).pack()
entry_user_cadastro = Entry(frame_cadastro)
entry_user_cadastro.pack()
Label(frame_cadastro, text="Senha:", bg=COR_FUNDO, fg=COR_TEXTO).pack()
entry_senha_cadastro = Entry(frame_cadastro, show="*")
entry_senha_cadastro.pack()
Label(frame_cadastro, text="Repita a senha:", bg=COR_FUNDO, fg=COR_TEXTO).pack()
entry_resenha_cadastro = Entry(frame_cadastro, show="*")
entry_resenha_cadastro.pack(pady=5)
Button(frame_cadastro, text="Cadastro", bg=COR_BOTAO, fg=COR_TEXTO, command=criar_cadastro).pack(pady=5)

#menu principal
Label(frame_menu, text="Menu Principal", bg=COR_FUNDO, fg=COR_TEXTO, font=("Arial", 20, "bold")).pack(pady=20)
Button(frame_menu, text="Consultar Mercadorias", bg=COR_BOTAO, fg=COR_TEXTO, width=25, command=lambda: [consultar_mercadorias(), mostrar_tela(frame_consulta)]).pack(pady=5)
Button(frame_menu, text="Cadastrar Mercadoria", bg=COR_BOTAO, fg=COR_TEXTO, width=25, command=lambda: mostrar_tela(frame_mercadorias)).pack(pady=5)
Button(frame_menu, text="Inserir Mercadorias", bg=COR_BOTAO, fg=COR_TEXTO, width=25, command=lambda: mostrar_tela(frame_inserir)).pack(pady=5)
Button(frame_menu, text="Sair", bg=COR_ERRO, fg=COR_TEXTO, width=25, command=lambda:mostrar_tela(frame_login)).pack(pady=5)

#cadastro de mercadorias
Label(frame_mercadorias, text="CADASTRAR MERCADORIA", bg=COR_FUNDO, fg=COR_TEXTO, font=("Arial", 16, "bold")).pack(pady=10)
Label(frame_mercadorias, text="Nome:", bg=COR_FUNDO, fg=COR_TEXTO).pack()
entry_nome_mercadoria = Entry(frame_mercadorias)
entry_nome_mercadoria.pack()
Label(frame_mercadorias, text="Quantidade:", bg=COR_FUNDO, fg=COR_TEXTO).pack()
entry_qtd_mercadoria = Entry(frame_mercadorias)
entry_qtd_mercadoria.pack()
Label(frame_mercadorias, text="Preço:", bg=COR_FUNDO, fg=COR_TEXTO).pack()
entry_preço_mercadoria = Entry(frame_mercadorias)
entry_preço_mercadoria.pack(pady=5)
Button(frame_mercadorias, text="Cadastrar", bg=COR_FUNDO, fg=COR_TEXTO, command=cadastrar_mercadoria).pack(pady=5)
Button(frame_mercadorias, text="Voltar", bg=COR_ERRO, fg=COR_TEXTO, command=lambda: mostrar_tela(frame_menu)).pack()

#inserir
Label(frame_inserir, text="INSERIR MERCADORIAS", bg=COR_FUNDO, fg=COR_TEXTO, font=("Arial", 16, "bold")).pack(pady=10)
Label(frame_inserir, text="Nome da mercadoria:", bg=COR_FUNDO, fg=COR_TEXTO).pack()
entry_nome_inserir = Entry(frame_inserir)
entry_nome_inserir.pack()
Label(frame_inserir, text="Quantidade a adicionar:", bg=COR_FUNDO, fg=COR_TEXTO).pack()
entry_qtd_inserir = Entry(frame_inserir)
entry_qtd_inserir.pack(pady=5)
Button(frame_inserir, text="Adicionar", bg=COR_BOTAO, fg=COR_TEXTO, command=inserir_mercadorias).pack(pady=5)
Button(frame_inserir, text="Voltar", bg=COR_ERRO, fg=COR_TEXTO, command=lambda: mostrar_tela(frame_menu)).pack()

#consulta
Label(frame_consulta, text="CONSULTAR MERCADORIAS", bg=COR_FUNDO, fg=COR_TEXTO, font=("Arial", 16, "bold")).pack(pady=10)
texto = Text(frame_consulta, width=50, height=10)
texto.pack()
Button(frame_consulta, text="Voltar", bg=COR_ERRO, fg=COR_TEXTO, command=lambda: mostrar_tela(frame_menu)).pack(pady=5)

#inicial
for frame in (frame_login, frame_cadastro, frame_menu, frame_mercadorias, frame_consulta, frame_inserir):
    frame.grid(row=0, column=0, sticky='nsew')

mostrar_tela(frame_login)
root.mainloop()