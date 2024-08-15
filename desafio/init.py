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