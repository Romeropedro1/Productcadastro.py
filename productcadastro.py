import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Lista para armazenar os produtos
produtos = []

# Função para adicionar um novo produto
def adicionar_produto():
    nome = entry_nome.get()
    descricao = entry_descricao.get()
    try:
        valor = float(entry_valor.get())
    except ValueError:
        messagebox.showerror("Erro", "O valor do produto deve ser um número.")
        return
    disponivel = var_disponivel.get()

    if nome and descricao and valor:
        produto = {
            'nome': nome,
            'descricao': descricao,
            'valor': valor,
            'disponivel': disponivel
        }
        produtos.append(produto)
        produtos.sort(key=lambda x: x['valor'])  # Ordena os produtos pelo valor
        atualizar_listagem()
        limpar_campos()
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")

# Função para atualizar a listagem de produtos
def atualizar_listagem():
    # Limpar a listagem existente
    for item in treeview.get_children():
        treeview.delete(item)
    
    # Adicionar os produtos na listagem
    for produto in produtos:
        treeview.insert('', 'end', values=(produto['nome'], f"R$ {produto['valor']:.2f}"))

# Função para limpar os campos do formulário
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_descricao.delete(0, tk.END)
    entry_valor.delete(0, tk.END)
    var_disponivel.set('sim')

# Função para deletar o produto selecionado
def deletar_produto():
    selected_item = treeview.selection()
    if selected_item:
        # Obter o nome do produto selecionado
        nome_produto = treeview.item(selected_item)['values'][0]
        produto_para_deletar = None
        
        # Encontrar o produto na lista de produtos
        for produto in produtos:
            if produto['nome'] == nome_produto:
                produto_para_deletar = produto
                break
        
        # Se encontrado, deletar da lista de produtos
        if produto_para_deletar:
            produtos.remove(produto_para_deletar)
            atualizar_listagem()
        else:
            messagebox.showerror("Erro", "Produto não encontrado para deletar.")
    else:
        messagebox.showerror("Erro", "Selecione um produto para deletar.")

# Função para criar a janela de cadastro
def criar_janela():
    janela = tk.Tk()
    janela.title("Cadastro de Produtos")

    # Campos do formulário
    tk.Label(janela, text="Nome do Produto:").grid(row=0, column=0)
    global entry_nome
    entry_nome = tk.Entry(janela)
    entry_nome.grid(row=0, column=1)

    tk.Label(janela, text="Descrição do Produto:").grid(row=1, column=0)
    global entry_descricao
    entry_descricao = tk.Entry(janela)
    entry_descricao.grid(row=1, column=1)

    tk.Label(janela, text="Valor do Produto:").grid(row=2, column=0)
    global entry_valor
    entry_valor = tk.Entry(janela)
    entry_valor.grid(row=2, column=1)

    tk.Label(janela, text="Disponível para venda:").grid(row=3, column=0)
    global var_disponivel
    var_disponivel = tk.StringVar(value='sim')
    tk.Radiobutton(janela, text="Sim", variable=var_disponivel, value='sim').grid(row=3, column=1, sticky='w')
    tk.Radiobutton(janela, text="Não", variable=var_disponivel, value='não').grid(row=3, column=1, sticky='e')

    # Botão para adicionar o produto
    btn_adicionar = tk.Button(janela, text="Cadastrar Produto", command=adicionar_produto)
    btn_adicionar.grid(row=4, column=0, columnspan=2)

    # Listagem de produtos
    global treeview
    treeview = ttk.Treeview(janela, columns=("Nome", "Valor"), show="headings")
    treeview.heading("Nome", text="Nome")
    treeview.heading("Valor", text="Valor")
    treeview.grid(row=5, column=0, columnspan=2)

    # Botão para cadastrar novo produto
    btn_novo_produto = tk.Button(janela, text="Novo Produto", command=limpar_campos)
    btn_novo_produto.grid(row=6, column=0, columnspan=2)

    # Botão para deletar o produto selecionado
    btn_deletar_produto = tk.Button(janela, text="Deletar Produto", command=deletar_produto)
    btn_deletar_produto.grid(row=7, column=0, columnspan=2)

    janela.mainloop()

# Criar a janela de cadastro ao executar o código
criar_janela()


