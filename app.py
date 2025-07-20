from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# tela inicial
@app.route("/")
def homepage():
    return render_template("index.html")

# tela do pedido
@app.route("/pedido")
def PEDIDOpage():
    return render_template("pedido.html")

# tela aceito
@app.route("/aceito")
def ACEITOpage():
    return render_template("aceito.html")

if __name__ == '__main__':
    app.run(debug=True)