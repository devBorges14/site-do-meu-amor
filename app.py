from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

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

# Data que vocês começaram a namorar (exemplo)
data_inicio = datetime(2025, 7, 20, 0, 0, 0)

@app.route('/aceito')
def aceito():
    agora = datetime.now()
    delta = agora - data_inicio
    total_seconds = int(delta.total_seconds())
    # Passa total_seconds para o JS atualizar o cronômetro
    return render_template('aceito.html', total_seconds=total_seconds)

if __name__ == '__main__':
    app.run(debug=True)