# SoftRisk

SoftRisk é um sistema baseado em lógica fuzzy desenvolvido para avaliar o nível de risco de projetos de software. Utilizando 12 variáveis principais que influenciam o risco de um projeto, SoftRisk é capaz de lidar com incertezas e subjetividades, fornecendo análises confiáveis e visuais para apoiar a tomada de decisão em grandes empresas.

---

## 📝 O Projeto

SoftRisk foi criado como parte de uma tarefa intitulada **Projeto 5: Avaliação Fuzzy de Risco de Projetos de Software**, cujo objetivo é desenvolver um sistema baseado em regras fuzzy para calcular o nível de risco com base em variáveis como experiência da equipe, prazo, complexidade técnica, entre outras. 

As regras fuzzy e as variáveis foram modeladas utilizando o ChatGPT-4, que desempenhou um papel fundamental na definição das regras linguísticas e dos intervalos fuzzy. O sistema é totalmente funcional, com uma interface web estilizada utilizando **Tailwind CSS**, onde os usuários podem inserir os dados do projeto e visualizar o resultado calculado junto com um gráfico.

---

![](./data/Screenshot%202024-11-30%20232253.png)


![](./data/Screenshot%202024-11-30%20232343.png)

## 🚀 Funcionalidades

- **Avaliação fuzzy de riscos**: Análise baseada em 12 variáveis principais e suas relações.
- **Visualização gráfica**: Geração de gráficos interativos que exibem o nível de risco calculado.
- **Interface amigável**: Entrada de dados intuitiva e estilizada com Tailwind CSS.
- **Regras fuzzy realistas**: As regras foram geradas pelo ChatGPT-4 com base em cenários reais.

---

## 🛠️ Tecnologias Utilizadas

- **Python** (3.9 ou superior)
- **Flask** (Back-End)
- **Tailwind CSS** (Estilização)
- **Matplotlib** (Gráficos)
- **scikit-fuzzy** (Modelo fuzzy)

---

## 📋 Variáveis do Modelo

### **Variáveis de Entrada**

1. **Experiência da Equipe** (anos) [1, 10]  
   Baixa, Média, Alta

2. **Nível de Entrosamento** (escala subjetiva) [0, 10]  
   Baixo, Médio, Alto

3. **Rotatividade da Equipe** (% de substituições) [0, 100]  
   Baixa, Moderada, Alta

4. **Definição de Requisitos** (escala subjetiva) [0, 10]  
   Mal Definida, Parcialmente Definida, Bem Definida

5. **Mudanças nos Requisitos** (% de alterações significativas) [0, 100]  
   Baixas, Moderadas, Altas

6. **Tamanho do Projeto** (pontos de função) [0, 100]  
   Pequeno, Médio, Grande

7. **Prazo** (meses) [1, 36]  
   Curto, Moderado, Longo

8. **Comunicação** (escala subjetiva) [0, 10]  
   Ruim, Boa, Ótima

9. **Maturidade das Ferramentas** (escala subjetiva) [0, 10]  
   Imatura, Moderada, Alta

10. **Impacto do Ambiente Externo** (escala subjetiva) [0, 10]  
   Baixo, Moderado, Alto

11. **Orçamento Disponível** (USD) [5.000, 500.000]  
   Baixo, Adequado, Excedente

### **Variável de Saída**

12. **Nível de Risco do Projeto**  
   Baixo [0, 25], Moderado [25, 50], Alto [50, 75], Crítico [75, 100]

---

## 📜 Regras Fuzzy

As seguintes regras foram definidas para determinar o nível de risco:

1. **SE** Experiência é Baixa **E** Complexidade é Alta **ENTÃO** Risco é Alto.  
2. **SE** Entrosamento é Baixo **OU** Rotatividade é Alta **ENTÃO** Risco é Crítico.  
3. **SE** Prazo é Curto **E** Tamanho é Grande **ENTÃO** Risco é Crítico.  
4. **SE** Definição de Requisitos é Mal Definida **E** Mudanças nos Requisitos são Altas **ENTÃO** Risco é Crítico.  
5. **SE** Tamanho é Grande **E** Prazo é Curto **ENTÃO** Risco é Alto.  
6. **SE** Comunicação é Ruim **E** Impacto Externo é Alto **ENTÃO** Risco é Crítico.  
7. **SE** Comunicação é Ótima **E** Maturidade é Alta **ENTÃO** Risco é Baixo.  
8. **SE** Orçamento é Baixo **E** Prazo é Curto **ENTÃO** Risco é Crítico.  

---

## 🖥️ Como Rodar o Projeto

### **Pré-requisitos**
- Python 3.9 ou superior instalado.
- Gerenciador de pacotes `pip`.

### **Passos para Instalação**

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/soft-risk.git
cd soft-risk
```

2. Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o servidor Flask:

```bash
python app.py
```

5. Acesse no navegador:
```bash
http://127.0.0.1:5000
