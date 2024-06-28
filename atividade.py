#Código produzido por: Rafael Barbosa da Silva
#Linguagem: PYTHON
#Objetivo: Criar um sistema simples e objetivo de cadrastro de produtos seguindo as especificações pré definidas no formulário
#Linkedin: https://www.linkedin.com/in/rafael-barbosa-671649293/
#Email: rafaelbrbsilva@gmail.com






import tkinter as tk
from tkinter import ttk, messagebox

#Lista global para produtos
produtos = []

#Função para adicionar produtos
def adicionar_produto(nome, descricao, valor, disponivel):
    try:
        valor = float(valor)
        produto = {
            'nome': nome,
            'descricao': descricao,
            'valor': valor,
            'disponivel': disponivel
        }
        produtos.append(produto) #Adiciona produto na lista
        produtos.sort(key=lambda x: x['valor']) #Ordena a lista pelo valor
        nome_var.set("") #Limpa o campo de nome
        descricao_var.set("") #Limpa o campo de descrição
        valor_var.set("") #Limpa o campo de valor
        disponivel_var.set("Sim") #Define o campo de disponível como "Sim"
        listar_produtos() #Atualiza a listagem de produtos
        exibir_listagem() #Chama a função para exibir a listagem pós cadrastro
    except ValueError:
        messagebox.showerror("Erro!", "Valor do produto deve ser numérico.")

#Função para listar produtos
def listar_produtos():
    for item in tree.get_children():
        tree.delete(item) #Limpa a listagem atual
    
    for produto in produtos:
        tree.insert('', 'end', values=(produto['nome'], f"R${produto['valor']:.2f}"))

#Função para exibir formulário
def exibir_formulario():
    frame_listagem.pack_forget() #Esconde o frame da listagem
    frame_formulario.pack() #Mostra o frame do formulário

#Função para exibir a lista
def exibir_listagem():
    frame_formulario.pack_forget() #Esconde o frame do formulário
    frame_listagem.pack() #Mostra o frame da listagem
    listar_produtos() #Atualiza a listagem de produtos

root = tk.Tk()
root.title("Cadastro e Listagem de Produtos")

frame_formulario = tk.Frame(root)
frame_formulario.pack()

nome_var = tk.StringVar()
descricao_var = tk.StringVar()
valor_var = tk.StringVar()
disponivel_var = tk.StringVar(value="Sim")

tk.Label(frame_formulario, text="Nome do produto:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(frame_formulario, textvariable=nome_var).grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame_formulario, text="Descrição do produto:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(frame_formulario, textvariable=descricao_var).grid(row=1, column=1, padx=10, pady=10)

tk.Label(frame_formulario, text="Valor do produto:").grid(row=2, column=0, padx=10, pady=10)
tk.Entry(frame_formulario, textvariable=valor_var).grid(row=2, column=1, padx=10, pady=10)

tk.Label(frame_formulario, text="Disponível para venda:").grid(row=3, column=0, padx=10, pady=10)
ttk.Combobox(frame_formulario, textvariable=disponivel_var, values=["Sim", "Não"]).grid(row=3, column=1, padx=10, pady=10)

tk.Button(frame_formulario, text="Cadastrar", command=lambda: adicionar_produto(
    nome_var.get(), descricao_var.get(), valor_var.get(), disponivel_var.get())).grid(row=4, column=0, columnspan=2, pady=10)

tk.Button(frame_formulario, text="Ver Listagem", command=exibir_listagem).grid(row=5, column=0, columnspan=2, pady=10)

frame_listagem = tk.Frame(root)

tree = ttk.Treeview(frame_listagem, columns=("nome", "valor"), show='headings')
tree.heading("nome", text="Nome")
tree.heading("valor", text="Valor")

tree.pack()

tk.Button(frame_listagem, text="Novo Produto", command=exibir_formulario).pack(pady=10)

exibir_formulario()
root.mainloop()
