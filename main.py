import os
from utils.middleware import HTTPMethodOverrideMiddleware as middleware
from flask import Flask, render_template, redirect, request

# Esta linha é para evitar bugs para localizar os caminhos
basedir = os.path.abspath(os.path.dirname(__file__))

# Nesta parte setamos o Flask como um objeto app e assim podemos configurar
app = Flask(
    __name__,
    static_folder=os.path.join(basedir, "static"),
    template_folder=os.path.join(basedir, "templates"),
)

# Aqui invocamos o utilitário que habilita os métodos PUT e DELETE no template Jinja
app.wsgi_app = middleware(app.wsgi_app)

###########################################################################
# Seção de rotas
###########################################################################

# Decorador o @ informa ao python que a função abaixo não é uma função comum
# ela está dentro do decorador, este decorador faz o flask chamar a função
# quando a rota for chamada no navegador
@app.route("/")
# Função que é chamada pelo decorador
def home():
    # Chama o arquivo index.jinja para criar a página
    return render_template("index.jinja")

@app.route("/patrimonio", methods=['GET', 'POST', 'PUT', 'DELETE'])
def patrimonios():
    if request.method == 'GET':
        return render_template("patrimonios.jinja")

@app.route("/patrimonio/form")
def form_patrimonios():
    return render_template("patrimonios_form.jinja")

@app.route("/setor")
def setores():
    return render_template("setores.jinja")




###########################################################################
# Fim da seção de rotas
###########################################################################



# Esta parte faz com que o código interno seja rodado apenas se o arquivo for rodado diretamente
# mas não seja rodado quando for importado em outro local
if __name__ == "__main__":
    
    # app.run faz com que o Flask seja iniciado o debug=True faz a execução ser mais verboso e assim
    # caso algum bug ocorra seja mais fácil localizar o erro
    app.run(debug=True)