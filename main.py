import os
from utils.middleware import HTTPMethodOverrideMiddleware as middleware
from flask import Flask, render_template, redirect, request, url_for
import bd

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
    patrimonio = bd.Patrimonio()
    if request.method == 'POST':
        nome = request.form['nome']
        n_patrimonio = int(request.form['patrimonio'])
        id_setor = int(request.form['id_setor'])
        patrimonio.create(nome, n_patrimonio, id_setor)
        return redirect(url_for("patrimonios"))
    elif request.method == 'PUT':
        id = int(request.form['id'])
        nome = request.form['nome']
        n_patrimonio = int(request.form['patrimonio'])
        id_setor = int(request.form['id_setor'])
        patrimonio.update(id, nome, n_patrimonio, id_setor)
        return redirect(url_for("patrimonios"))
    elif request.method == "DELETE":
        id = int(request.form['id'])
        patrimonio.delete(id)
        return redirect(url_for("patrimonios"))
    else:
        setor = bd.Setor()
        patrimonios = patrimonio.read()
        setores = setor.read()
        return render_template("patrimonios.jinja", patrimonios=patrimonios, setores=setores)
    

@app.route("/patrimonio/form")
def form_patrimonios():
    id = request.args.get("id")
    if id:
        patrimonio = bd.Patrimonio.read(id)
        patrimonio = patrimonio[0]
    else:
        patrimonio = False
    setor = bd.Setor()
    setores = setor.read()
    return render_template("patrimonios_form.jinja", setores=setores, patrimonio=patrimonio)

#####################################################################################################

@app.route("/setor", methods=['GET', 'POST', 'PUT', 'DELETE'])
def setores():
    setor = bd.Setor()
    if request.method == 'POST':
        nome = request.form['nome']
        setor.create(nome)
        return redirect(url_for("setores"))
    elif request.method == 'PUT':
        id = int(request.form['id'])
        nome = request.form['nome']
        setor.update(id, nome)
        return redirect(url_for("setores"))
    elif request.method == "DELETE":
        id = int(request.form['id'])
        setor.delete(id)
        return redirect(url_for("setores"))
    else:
        setores = setor.read()
        return render_template("setores.jinja", setores=setores)

@app.route("/setor/form")
def form_setores():
    id = request.args.get('id')
    if id:
        setores = bd.Setor.read(id)
        setores = setores[0]
    else:
        setores = False
    return render_template("setores_form.jinja", setores=setores)




###########################################################################
# Fim da seção de rotas
###########################################################################



# Esta parte faz com que o código interno seja rodado apenas se o arquivo for rodado diretamente
# mas não seja rodado quando for importado em outro local
if __name__ == "__main__":
    
    # app.run faz com que o Flask seja iniciado o debug=True faz a execução ser mais verboso e assim
    # caso algum bug ocorra seja mais fácil localizar o erro
    app.run(debug=True)