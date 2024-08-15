from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/novoaluno')
def cadastrar_aluno():
    return render_template('novoaluno.html')

@app.route('/diario')
def diario():
    return render_template('diriobordo.html')

@app.route('/logar',methods=['POST'])
def logar():
    ra = request.form['ra']
    if ra == '12345619':
        return render_template('diariobordo.html',ra=ra)
    else:
        return f'O ra está errado'
app.run(debug=True)





# o dontpad do mapeamento objeto relacional - ORM
# Modelo Relacional de Edgar Frank Cod com o paradigma de Orientação a Objetos python#







# Lista de Importação#


# Importa a função `sessionmaker`, que é usada para criar uma nova sessão para interagir com o banco de dados
from sqlalchemy.orm import sessionmaker

# Importa as funções `create_engine` para estabelecer uma conexão com o banco de dados e `MetaData` para trabalhar com metadados do banco de dados
from sqlalchemy import create_engine, MetaData

# Importa a função `automap_base`, que é usada para refletir um banco de dados existente em classes ORM automaticamente
from sqlalchemy.ext.automap import automap_base
from aluno import Aluno

#Conexão e Mapeamento#}


# Criando a configuração do banco de dados
# Configuração do Banco de Dados
# biblioteca para converter e resolver problema do @
import urllib.parse

# Qual o usuário do banco e a senha?

user = 'root'
password = urllib.parse.quote_plus('senai@123')

host = 'localhost'
database = 'projetodiario1'
connection_string = f'mysql+pymysql://{user}:{password}@{host}/{database}'

# Criar a engine e refletir o banco de dados existente
engine = create_engine(connection_string)
metadata = MetaData()
metadata.reflect(engine)

# Mapeamento automático das tabelas para classes Python
Base = automap_base(metadata=metadata)
Base.prepare()

# Acessando a tabela 'vitorias' mapeada
Aluno = Base.classes.aluno



# Criar a sessão do SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()