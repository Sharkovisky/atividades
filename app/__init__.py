from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/home')
def home():
    title = "Atividades Complementares"
    lista = ['Semana da Ciência e Tecnologia','Oficina Git e GitHub', 'Semana Acadêmica de ADS']
    return render_template('index.html', titulo=title, eventos=lista)
