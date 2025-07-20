from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# tela inicial
@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/pedido", methods=["GET", "POST"])
def pedido():
    if request.method == "POST":
        if "sim" in request.form:
            return redirect(url_for("aceito"))  # Rota que mostra o pedido aceito
        elif "nao" in request.form:
            return render_template("pedido.html", erro="Não vale dizer não 😢 Tenta de novo...")

    return render_template("pedido.html", erro=None)


# tela aceito
@app.route("/aceito")
def aceito():
    return render_template("aceito.html")

if __name__ == '__main__':
    app.run(debug=True)