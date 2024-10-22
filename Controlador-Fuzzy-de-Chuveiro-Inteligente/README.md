# Controlador Fuzzy de Chuveiro Inteligente

## Sobre o Projeto
Sistema de controle inteligente baseado em lógica fuzzy para regular automaticamente a temperatura do chuveiro. O projeto utiliza a biblioteca Scikit-Fuzzy para implementar um controlador Mamdani que ajusta a abertura da válvula com base na temperatura e fluxo de água.

## Funcionalidades
- Controle automático da temperatura do chuveiro
- Sistema de inferência fuzzy baseado em Mamdani
- Processamento de duas variáveis de entrada (temperatura e fluxo de água)
- Controle da abertura da válvula como saída

## Tecnologias Utilizadas
- Python
- Scikit-Fuzzy
- NumPy
- Matplotlib

## Estrutura do Sistema
O sistema implementa um controlador fuzzy completo com:
- Fuzzificação das entradas
- Base de regras com 6 regras de controle
- Sistema de inferência Mamdani
- Defuzzificação para determinar a abertura da válvula

## Como Executar
1. Instale as dependências necessárias:
```bash
pip install scikit-fuzzy numpy matplotlib
```