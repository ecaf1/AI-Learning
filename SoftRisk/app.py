import matplotlib.pyplot as plt
import io
import base64
from flask import Flask, render_template, request
from simulation import simulate, risk_simulation, risco

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Coleta as variáveis do formulário
        inputs = {
            "experiencia": int(request.form.get("experiencia")),
            "entrosamento": int(request.form.get("entrosamento")),
            "rotatividade": int(request.form.get("rotatividade")),
            "complexidade": int(request.form.get("complexidade")),
            "definicao_requisitos": int(request.form.get("definicao_requisitos")),
            "mudancas_requisitos": int(request.form.get("mudancas_requisitos")),
            "tamanho": int(request.form.get("tamanho")),
            "prazo": int(request.form.get("prazo")),
            "comunicacao": int(request.form.get("comunicacao")),
            "maturidade": int(request.form.get("maturidade")),
            "impacto_externo": int(request.form.get("impacto_externo")),
            "orcamento": int(request.form.get("orcamento")),
        }

        # Executa a simulação
        nivel_de_risco = simulate(inputs)

        # Gera o gráfico do resultado
        plt.figure()
        risco.view(sim=risk_simulation)  # Gera o gráfico do skfuzzy
        img = io.BytesIO()
        plt.savefig(img, format="png")
        img.seek(0)
        graph_url = base64.b64encode(img.getvalue()).decode("utf-8")
        plt.close()

        # Renderiza o resultado
        return render_template("result.html", nivel_de_risco=nivel_de_risco, graph_url=graph_url)

    # Renderiza a página inicial com o formulário
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
