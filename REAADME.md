
```md
# Flask CRUD Application with Bootstrap

Este é um projeto simples de aplicação web em **Flask** que implementa um sistema **CRUD (Criar, Ler, Atualizar, Deletar)** para o gerenciamento de produtos. O projeto também inclui um sistema de autenticação e autorização, onde apenas administradores podem adicionar, editar e remover produtos. Para o frontend, utilizamos **Bootstrap** para tornar o design responsivo e elegante.

## Funcionalidades

- **Autenticação**: Sistema de login com dois tipos de usuários - Admin e Usuário Comum.
- **Autorização**: Apenas administradores podem realizar operações de criar, editar e deletar produtos.
- **CRUD de Produtos**:
  - Criar um novo produto (apenas admin).
  - Listar todos os produtos (visível para todos os usuários logados).
  - Editar um produto (apenas admin).
  - Deletar um produto (apenas admin).
- **Banco de Dados**: Uso do **SQLite** para armazenar os dados dos produtos.

## Tecnologias Utilizadas

- **Python 3.x**
- **Flask**
- **SQLite** (via SQLAlchemy)
- **Bootstrap 5**
- **HTML/CSS**

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd nome-do-repositorio
   ```

3. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate  # Windows
   ```

4. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

5. Execute o aplicativo:

   ```bash
   python app.py
   ```

6. Abra o navegador e acesse `http://127.0.0.1:5000/` para visualizar o projeto.

## Estrutura do Projeto

```
├── app.py               # Arquivo principal do Flask
├── templates/           # Diretório dos templates HTML
│   ├── base.html        # Template base com o layout padrão
│   ├── login.html       # Página de login
│   ├── produtos.html    # Página para listar produtos
│   ├── adicionar.html   # Formulário para adicionar produto
│   ├── editar.html      # Formulário para editar produto
├── static/
│   ├── css/             # Arquivos de estilo CSS
│   └── js/              # Arquivos JavaScript
├── produtos.db          # Arquivo do banco de dados SQLite
├── requirements.txt     # Dependências do projeto
└── README.md            # Arquivo de documentação do projeto
```

## Uso

- Acesse a aplicação em `http://127.0.0.1:5000/`.
- Faça login como administrador para adicionar, editar ou deletar produtos.
- Usuários comuns podem visualizar os produtos listados.

## Licença

Este projeto está licenciado sob a licença [MIT](https://choosealicense.com/licenses/mit/).

---

Sinta-se à vontade para contribuir com o projeto ou sugerir melhorias!
```
