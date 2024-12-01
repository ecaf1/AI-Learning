import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# --- Definição das variáveis fuzzy ---
experiencia = ctrl.Antecedent(np.arange(1, 11, 1), "experiencia")
entrosamento = ctrl.Antecedent(np.arange(0, 11, 1), "entrosamento")
rotatividade = ctrl.Antecedent(np.arange(0, 101, 1), "rotatividade")
complexidade = ctrl.Antecedent(np.arange(0, 11, 1), "complexidade")
definicao_requisitos = ctrl.Antecedent(np.arange(0, 11, 1), "definicao_requisitos")
mudancas_requisitos = ctrl.Antecedent(np.arange(0, 101, 1), "mudancas_requisitos")
tamanho = ctrl.Antecedent(np.arange(0, 101, 1), "tamanho")
prazo = ctrl.Antecedent(np.arange(1, 37, 1), "prazo")
comunicacao = ctrl.Antecedent(np.arange(0, 11, 1), "comunicacao")
maturidade = ctrl.Antecedent(np.arange(0, 11, 1), "maturidade")
impacto_externo = ctrl.Antecedent(np.arange(0, 11, 1), "impacto_externo")
orcamento = ctrl.Antecedent(np.arange(5000, 500001, 5000), "orcamento")  # Intervalo ajustado

risco = ctrl.Consequent(np.arange(0, 101, 1), "risco")

# --- Funções de pertinência ---
experiencia.automf(names=["baixa", "media", "alta"])
entrosamento.automf(names=["baixo", "medio", "alto"])
rotatividade.automf(names=["baixa", "media", "alta"])
complexidade.automf(names=["baixa", "media", "alta"])
definicao_requisitos.automf(names=["mal_definida", "parcialmente_definida", "bem_definida"])
mudancas_requisitos.automf(names=["baixas", "moderadas", "altas"])
tamanho.automf(names=["pequeno", "medio", "grande"])
prazo.automf(names=["curto", "moderado", "longo"])
comunicacao.automf(names=["ruim", "adequada", "otima"])
maturidade.automf(names=["baixa", "media", "alta"])
impacto_externo.automf(names=["baixo", "moderado", "alto"])
orcamento.automf(names=["baixo", "adequado", "excedente"])

risco["baixo"] = fuzz.trapmf(risco.universe, [0, 0, 25, 50])
risco["moderado"] = fuzz.trimf(risco.universe, [25, 50, 75])
risco["alto"] = fuzz.trapmf(risco.universe, [50, 75, 90, 100])
risco["critico"] = fuzz.trapmf(risco.universe, [75, 90, 100, 100])

# --- Regras fuzzy ---
rule1 = ctrl.Rule(experiencia["baixa"] & complexidade["alta"], risco["alto"])
rule2 = ctrl.Rule(entrosamento["baixo"] | rotatividade["alta"], risco["critico"])
rule3 = ctrl.Rule(prazo["curto"] & tamanho["grande"], risco["critico"])
rule4 = ctrl.Rule(definicao_requisitos["mal_definida"] & mudancas_requisitos["altas"], risco["critico"])
rule5 = ctrl.Rule(tamanho["grande"] & prazo["curto"], risco["alto"])
rule6 = ctrl.Rule(comunicacao["ruim"] & impacto_externo["alto"], risco["critico"])
rule7 = ctrl.Rule(comunicacao["otima"] & maturidade["alta"], risco["baixo"])
rule8 = ctrl.Rule(orcamento["baixo"] & prazo["curto"], risco["critico"])

# --- Controle fuzzy ---
risk_control = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8])
risk_simulation = ctrl.ControlSystemSimulation(risk_control)

# --- Função de simulação ---
def simulate(inputs):
    try:
        for key, value in inputs.items():
            risk_simulation.input[key] = value  # Insere os valores de entrada

        risk_simulation.compute()  # Executa o sistema fuzzy
        return round(risk_simulation.output["risco"], 2)  # Retorna o resultado arredondado
    except KeyError as e:
        raise ValueError(f"Variável desconhecida: {e}")

# --- Teste ---
inputs = {
    "experiencia": 5,
    "entrosamento": 7,
    "rotatividade": 30,
    "complexidade": 8,
    "definicao_requisitos": 6,
    "mudancas_requisitos": 40,
    "tamanho": 50,
    "prazo": 12,
    "comunicacao": 8,
    "maturidade": 6,
    "impacto_externo": 3,
    "orcamento": 150000,  # Novo valor ajustado para o intervalo expandido
}

# Simulação e resultado
nivel_de_risco = simulate(inputs)
print(f"Nível de Risco Calculado: {nivel_de_risco}%")
