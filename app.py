from flask import Flask, render_template, redirect, url_for, request, flash, session

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'minha_chave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///produtos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de Produto
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(200), nullable=False)

# Criando o banco de dados
with app.app_context():
    db.create_all()
    
# Simulação de uma base de usuários
usuarios = {
    'admin': {'senha': '123', 'role': 'admin'},
    'usuario': {'senha': '456', 'role': 'comum'}
}

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Verifica se o usuário existe e se a senha está correta
        if username in usuarios and usuarios[username]['senha'] == password:
            session['user'] = username
            session['role'] = usuarios[username]['role']  # Armazena o papel do usuário
            flash(f'Login realizado com sucesso! Bem-vindo, {username}', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Nome de usuário ou senha incorretos', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

# Rota para a página de dashboard (acessível a todos os usuários logados)
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', user=session['user'], role=session['role'])
    else:
        flash('Você precisa fazer login primeiro!', 'danger')
        return redirect(url_for('login'))

# Rota protegida apenas para admins
@app.route('/admin')
def admin():
    if 'user' in session and session.get('role') == 'admin':
        return render_template('admin.html', user=session['user'])
    else:
        flash('Acesso negado! Esta página é restrita para administradores.', 'danger')
        return redirect(url_for('dashboard'))

# Rota para logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('role', None)
    flash('Você saiu com sucesso!', 'success')
    return redirect(url_for('index'))

# Rota para visualizar todos os produtos (visível para todos os usuários logados)
@app.route('/produtos')
def produtos():
    if 'user' in session:
        todos_produtos = Produto.query.all()  # Obtém todos os produtos do banco de dados
        return render_template('produtos.html', produtos=todos_produtos, role=session['role'])
    else:
        flash('Você precisa fazer login primeiro!', 'danger')
        return redirect(url_for('login'))

# Rota para adicionar novo produto (apenas para admin)
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if 'user' in session and session['role'] == 'admin':
        if request.method == 'POST':
            nome = request.form['nome']
            preco = request.form['preco']
            descricao = request.form['descricao']
            novo_produto = Produto(nome=nome, preco=preco, descricao=descricao)
            db.session.add(novo_produto)
            db.session.commit()
            flash('Produto adicionado com sucesso!', 'success')
            return redirect(url_for('produtos'))
        return render_template('adicionar.html')
    else:
        flash('Acesso negado! Apenas administradores podem adicionar produtos.', 'danger')
        return redirect(url_for('produtos'))

# Rota para editar um produto existente (apenas para admin)
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if 'user' in session and session['role'] == 'admin':
        produto = Produto.query.get_or_404(id)
        if request.method == 'POST':
            produto.nome = request.form['nome']
            produto.preco = request.form['preco']
            produto.descricao = request.form['descricao']
            db.session.commit()
            flash('Produto atualizado com sucesso!', 'success')
            return redirect(url_for('produtos'))
        return render_template('editar.html', produto=produto)
    else:
        flash('Acesso negado! Apenas administradores podem editar produtos.', 'danger')
        return redirect(url_for('produtos'))

# Rota para deletar um produto (apenas para admin)
@app.route('/deletar/<int:id>')
def deletar(id):
    if 'user' in session and session['role'] == 'admin':
        produto = Produto.query.get_or_404(id)
        db.session.delete(produto)
        db.session.commit()
        flash('Produto deletado com sucesso!', 'success')
        return redirect(url_for('produtos'))
    else:
        flash('Acesso negado! Apenas administradores podem deletar produtos.', 'danger')
        return redirect(url_for('produtos'))
        
if __name__ == "__main__":
    app.run(debug=True)
