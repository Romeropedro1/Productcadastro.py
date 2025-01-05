Cadastro de Produtos
Descrição
Este projeto é uma aplicação simples de Cadastro de Produtos desenvolvida em Python utilizando a biblioteca Tkinter para um em

Um aplicativo

Funcionalidades
Cadastrar Produto: Permite adicionar um novo produto com nome, descrição, valor e disponibilidade.
Listagem de Produtos: Exibe uma lista de produtos cadastrados, ordenada pelo valor do produto.
Deletar Produto: Permite excluir um produto selecionado da lista.
Limpar Campos: Apaga os campos do formulário para adicionar novos produtos.
Tecnologia
Python : Uma linguagem
Tkinter : Biblioteca utilizada para criação da interfa
ttk (Themed Tkinter) : SubbiblioTreeview (usada para listar os produtos).
Como Executar o Projeto
Pré-requisitos: Certifique-se de que você tenha o Python 3.x instalado em seu sistema.

Você pode verificar se o Python está instalado executando o seguinte comando no terminal ou prompt de comando:
bater

Copiar código
python --version
Se não estiver instalado, você pode obter a versão mais recente do Python no site oficial: https://www.python.org/downloads/

Instalação: Clone este repositório em seu diretório de trabalho.

bater

Copiar código
git clone https://github.com/Romeropedro1/Productcadastro.py.git
cd Productcadastro.py
Execução: Para rodar a aplicação, execute o arquivo Python Productcadastro.py.

bater

Copiar código
python Productcadastro.py
A interface gráfica será aberta, e você poderá começar a cadastrar, listar e excluir produtos.

Estrutura do Código
Funções principais:

adicionar_produto(): Adiciona um produto à lista e ordena os produtos por valor.
atualizar_listagem(): Atualiza a exibição da lista de produtos na interface gráfica.
limpar_campos(): Limpa os campos do formulário.
deletar_produto():D
criar_janela(): Configuração
Widgets importantes:

Treeview: Usado para exibir os produtos em formato tabular (nome e valor).
Entry: Campos de entrada para o nome, descrição e valor do produto.
Radiobutton: Permite escolher a disponibilidade do produto (sim ou não).
Button: Botões para adicionar, limpar e deletar produtos.
Como Usar
Adicionar Produto:

Preencha o nome, descrição, valor e disponibilidade do produto.
Clique em "Cadastrar Produto" para adicionar o produto à lista.
Listar Produtos:

A lista de produtos será exibida automaticamente, ordenada pelo valor do produto.
Deletar Produto:

Selecione um produto na lista.
Clique em "Deletar Produto" para removê-lo da lista.
Limpar Campos:

Clique em "Novo Produto" para limpar os campos e adicionar um novo produto.
Por exemplo
Adicionar Produto
Nome: "Cadeira"
Descrição: "Cadeira de escritório"
Valor: 150.00
Disponível: Sim
Após clicar em "Cadastrar Produto", o produto aparecerá na lista.

Listagem
A listagem de produtos exibirá o nome e valor de todos os produtos cadastrados. Os produtos serão ordenados pelo valor.

Deletar Produto
Selecione o produto na lista e clique em "Deletar Produto" para removê-lo.

Contribuição
Se você deseja contribuir para o projeto, fique à vontade para abrir um pull request com melhorias ou correções de bugs. Certifique-se de que suas mudanças não quebrem a funcionalidade existente e que tudo esteja bem documentado.

Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais informações.

