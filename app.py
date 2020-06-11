from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Site de receitas médicas de Doutora Maria Fernanda"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}. Be Welcome!!!".format(name)

if __name__ == '__main__':
    app.run()

