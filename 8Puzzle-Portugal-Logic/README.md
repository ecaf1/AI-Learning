# Soluções de Algoritmos de Busca - IA 2024.1

Este repositório contém soluções para três problemas clássicos de Inteligência Artificial:

1. [Jogo dos 8 Números (8-Puzzle)](#8-puzzle) - Implementação de três algoritmos de busca distintos
2. [Navegação em Mapa (Portugal)](#mapa-portugal) - Problema de roteamento entre cidades
3. [Provador de Teoremas](#provador-teoremas) - Sistema de prova automática em lógica proposicional

## 🎲 8-Puzzle <a name="8-puzzle"></a>

### O Problema

O jogo dos 8 números (8-puzzle) é um problema de busca onde temos:
- Um tabuleiro 3x3
- 8 peças numeradas e um espaço vazio
- Objetivo: atingir uma configuração específica movendo as peças

#### Estado Inicial (Situação 1):
```
1 7 2
8 4 5
6 _ 3
```

#### Estado Objetivo:
```
1 2 3
8 4 _
7 6 5
```


### Busca Gulosa (Greedy Search) 
Essa um estrategia que visa encontrar uma solução para nosso problema resolvendo subproblema de forma aparentimente otimas. Sendo assim definiremos a metrica heuristica para  para estimar a "distância".


1. Número de peças fora do lugar
2. Soma das distâncias Manhattan

```python
def calcular_heuristica(estado_atual, estado_objetivo, tipo="manhattan"):
    """
    Calcula o valor heurístico de um estado.
    
    Args:
        estado_atual: matriz 3x3 representando o estado atual
        estado_objetivo: matriz 3x3 representando o estado objetivo
        tipo: string indicando qual heurística usar ("manhattan" ou "pecas_fora")
    
    Returns:
        valor heurístico calculado
    """
    if tipo == "manhattan":
        return distancia_manhattan(estado_atual, estado_objetivo)
    else:
        return pecas_fora_lugar(estado_atual, estado_objetivo)
```

#### Implementação das Heurísticas

##### Heurística de Peças Fora do Lugar
```python
def pecas_fora_lugar(estado_atual, estado_objetivo):
    """
    Conta quantas peças estão fora de sua posição final.
    
    Exemplo:
    Estado Atual:     Estado Objetivo:
    1 2 3            1 2 3
    8 0 4            8 0 4
    7 6 5            7 5 6
                     
    Retorno: 2 (peças 5 e 6 estão fora do lugar)
    """
    count = 0
    for i in range(3):
        for j in range(3):
            # Não conta o espaço vazio (0)
            if estado_atual[i][j] != 0 and estado_atual[i][j] != estado_objetivo[i][j]:
                count += 1
    return count
```

#### Heurística da Distância Manhattan
```python
def distancia_manhattan(estado_atual, estado_objetivo):
    """
    Calcula a soma das distâncias Manhattan de cada peça até sua posição final.
    
    Exemplo:
    Estado Atual:     Estado Objetivo:
    1 2 3            1 2 3
    8 0 4            8 0 4
    7 6 5            7 5 6
    
    Peça 5: |2-1| + |2-1| = 2
    Peça 6: |2-2| + |1-2| = 1
    Total: 3
    """
    distancia = 0
    # Cria dicionário com posições objetivo
    pos_objetivo = {}
    for i in range(3):
        for j in range(3):
            if estado_objetivo[i][j] != 0:
                pos_objetivo[estado_objetivo[i][j]] = (i, j)
    
    # Calcula distância para cada peça
    for i in range(3):
        for j in range(3):
            if estado_atual[i][j] != 0:  # ignora espaço vazio
                pos_obj = pos_objetivo[estado_atual[i][j]]
                distancia += abs(i - pos_obj[0]) + abs(j - pos_obj[1])
                
    return distancia
```

#### Funções Auxiliares

```python
def encontrar_posicao(estado, valor):
    """
    Encontra a posição de um valor específico no tabuleiro.
    
    Args:
        estado: matriz 3x3 do tabuleiro
        valor: número a ser encontrado
    
    Returns:
        tupla (linha, coluna) com a posição
    """
    for i in range(3):
        for j in range(3):
            if estado[i][j] == valor:
                return (i, j)
    return None
```

#### Exemplo de Uso

```python
# Estado de exemplo
estado_inicial = [
    [1, 7, 2],
    [8, 4, 5],
    [6, 0, 3]
]

estado_objetivo = [
    [1, 2, 3],
    [8, 4, 0],
    [7, 6, 5]
]

# Calculando diferentes heurísticas
h1 = calcular_heuristica(estado_inicial, estado_objetivo, "pecas_fora")
h2 = calcular_heuristica(estado_inicial, estado_objetivo, "manhattan")

print(f"Peças fora do lugar: {h1}")
print(f"Distância Manhattan: {h2}")
```

#### Análise das Heurísticas

#####  Peças Fora do Lugar
- **Vantagens:**
  - Fácil de calcular
  - Intuitiva
- **Desvantagens:**
  - Menos informativa
  - Pode ser muito otimista

#####  Distância Manhattan
- **Vantagens:**
  - Mais informativa
  - Melhor estimativa da distância real
  - Admissível (nunca superestima)
- **Desvantagens:**
  - Mais complexa de calcular
  - Pode ainda ser otimista em alguns casos

#### Propriedades Importantes

#####  Admissibilidade
Ambas as heurísticas são admissíveis, pois:
- Nunca superestimam o custo real
- Garantem solução ótima quando usadas com A*

#####  Consistência
A distância Manhattan é consistente:
- h(n) ≤ c(n,n') + h(n')
- Onde c(n,n') é o custo do movimento
- E h(n') é a heurística do estado sucessor

#### Exemplo Detalhado

```python
estado_inicial = [
    [1, 7, 2],
    [8, 4, 5],
    [6, 0, 3]
]

estado_objetivo = [
    [1, 2, 3],
    [8, 4, 0],
    [7, 6, 5]
]

# Análise peça por peça (Manhattan)
"""
1: |0-0| + |0-0| = 0
7: |0-2| + |1-0| = 3
2: |0-0| + |2-1| = 1
8: |1-1| + |0-0| = 0
4: |1-1| + |1-1| = 0
5: |1-2| + |2-2| = 1
6: |2-2| + |0-1| = 3
3: |2-0| + |2-2| = 4

Total: 12
"""




```python
def busca_gulosa(estado_inicial, estado_objetivo):
    # Inicializa estruturas de controle
    fronteira = FilaPrioridade()    # Estados a serem explorados
    visitados = set()               # Estados já analisados
    
    # Calcula heurística inicial e adiciona primeiro estado
    h_inicial = calcular_heuristica(estado_inicial, estado_objetivo)
    fronteira.inserir(estado_inicial, h_inicial)
    
    while not fronteira.vazia():
        # Pega estado com menor valor heurístico
        atual = fronteira.remover()
        
        # Verifica se chegou ao objetivo
        if atual == estado_objetivo:
            return reconstruir_caminho(atual)
            
        # Marca como visitado
        visitados.add(atual)
        
        # Gera próximos estados possíveis
        for sucessor in gerar_sucessores(atual):
            if sucessor not in visitados:
                h_sucessor = calcular_heuristica(sucessor, estado_objetivo)
                fronteira.inserir(sucessor, h_sucessor)
```

**Características:**
- Utiliza apenas heurística para decisão
- Não considera custo do caminho
- Busca o estado que parece mais próximo do objetivo
- Rápido mas não garante solução ótima

###  Visão Geral do A* (A-Star)
O A* é um algoritmo de busca que combina:

- g(n): custo real do caminho até o nó atual
- h(n): estimativa heurística até o objetivo
- f(n) = g(n) + h(n): custo total estimado




# Algoritmo A* (A-Star) para o 8-Puzzle

## 1. Visão Geral do A*

O A* é um algoritmo de busca que combina:
- g(n): custo real do caminho até o nó atual
- h(n): estimativa heurística até o objetivo
- f(n) = g(n) + h(n): custo total estimado

## 2. Implementação Detalhada

### 2.1 Estruturas de Dados Base

```python
class Estado:
    def __init__(self, tabuleiro, pai=None, acao=None):
        self.tabuleiro = tabuleiro  # matriz 3x3
        self.pai = pai              # estado anterior
        self.acao = acao           # movimento que gerou este estado
        self.g = 0                 # custo do caminho até aqui
        self.h = 0                 # valor heurístico
        self.f = 0                 # f = g + h
    
    def calcular_f(self, estado_objetivo):
        """Calcula o valor total f(n) = g(n) + h(n)"""
        self.h = calcular_heuristica(self.tabuleiro, estado_objetivo)
        self.f = self.g + self.h
        return self.f
    
    def __lt__(self, outro):
        """Comparação para a fila de prioridade"""
        return self.f < outro.f
```

### Algoritmo A* Principal

```python
def a_estrela(estado_inicial, estado_objetivo):
    """
    Implementação do algoritmo A* para o 8-puzzle.
    
    Args:
        estado_inicial: Estado inicial do puzzle
        estado_objetivo: Estado objetivo a ser alcançado
    
    Returns:
        Lista de ações para chegar ao objetivo ou None se não houver solução
    """
    # Inicialização
    fronteira = PriorityQueue()  # estados a serem explorados
    visitados = set()            # estados já visitados
    
    # Prepara estado inicial
    inicio = Estado(estado_inicial)
    inicio.calcular_f(estado_objetivo)
    fronteira.put((inicio.f, inicio))
    
    # Hash dos estados visitados
    estado_para_hash = lambda x: str(x.tabuleiro)
    
    while not fronteira.empty():
        # Pega estado com menor f(n)
        _, atual = fronteira.get()
        hash_atual = estado_para_hash(atual)
        
        # Verifica se chegou ao objetivo
        if atual.tabuleiro == estado_objetivo:
            return reconstruir_caminho(atual)
            
        # Marca como visitado
        visitados.add(hash_atual)
        
        # Gera sucessores
        for sucessor in gerar_sucessores(atual):
            hash_sucessor = estado_para_hash(sucessor)
            
            if hash_sucessor in visitados:
                continue
                
            # Calcula novo custo g
            sucessor.g = atual.g + 1
            
            # Calcula f(n) = g(n) + h(n)
            sucessor.calcular_f(estado_objetivo)
            
            # Adiciona à fronteira
            fronteira.put((sucessor.f, sucessor))
    
    return None  # Não encontrou solução
```

##### Funções Auxiliares

```python
def gerar_sucessores(estado):
    """
    Gera todos os estados sucessores possíveis.
    """
    sucessores = []
    movimentos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # direita, baixo, esquerda, cima
    
    # Encontra posição do espaço vazio
    vazio_x, vazio_y = encontrar_vazio(estado.tabuleiro)
    
    # Tenta cada movimento possível
    for dx, dy in movimentos:
        novo_x, novo_y = vazio_x + dx, vazio_y + dy
        
        # Verifica se movimento é válido
        if 0 <= novo_x < 3 and 0 <= novo_y < 3:
            # Cria novo tabuleiro
            novo_tabuleiro = [linha[:] for linha in estado.tabuleiro]
            
            # Realiza movimento
            novo_tabuleiro[vazio_x][vazio_y] = novo_tabuleiro[novo_x][novo_y]
            novo_tabuleiro[novo_x][novo_y] = 0
            
            # Cria novo estado
            novo_estado = Estado(novo_tabuleiro, estado, f"Mover {novo_tabuleiro[vazio_x][vazio_y]}")
            sucessores.append(novo_estado)
            
    return sucessores

def reconstruir_caminho(estado):
    """
    Reconstrói o caminho da solução a partir do estado final.
    """
    caminho = []
    while estado.pai is not None:
        caminho.append(estado.acao)
        estado = estado.pai
    return list(reversed(caminho))
```

#### Exemplo Passo a Passo

```python
# Estado inicial e objetivo
inicial = [
    [1, 7, 2],
    [8, 4, 5],
    [6, 0, 3]
]

objetivo = [
    [1, 2, 3],
    [8, 4, 0],
    [7, 6, 5]
]

# Execução passo a passo
"""
Passo 1:
Estado: 1 7 2    f(n) = 0 + 12 = 12
       8 4 5     g(n) = 0 (início)
       6 0 3     h(n) = 12 (Manhattan)

Passo 2:
Estado: 1 7 2    f(n) = 1 + 11 = 12
       8 4 5     g(n) = 1 (um movimento)
       6 3 0     h(n) = 11 (Manhattan)

[continua...]
"""
```

#### Análise de Complexidade

#####  Tempo
- Pior caso: O(b^d)
  - b = fator de ramificação
  - d = profundidade da solução

##### Espaço
- O(b^d) estados armazenados

#### Por Que A* é Ótimo?

##### Garantia de Otimalidade
1. A* é ótimo quando h(n) é admissível
2. Nossa heurística Manhattan é admissível pois:
   - Nunca superestima a distância real
   - Cada peça precisa de pelo menos esses movimentos

```python
# Exemplo de admissibilidade
"""
Estado:     1 7 2
           8 4 5
           6 0 3

Para mover 7 para posição final:
- Heurística Manhattan = 3
- Custo real ≥ 3 (impossível em menos movimentos)
"""
```

##### Comparação com Busca Gulosa

```python
# Mesmo estado com diferentes algoritmos
estado = [
    [1, 7, 2],
    [8, 4, 5],
    [6, 0, 3]
]

# Busca Gulosa
"""
Decisão baseada apenas em h(n) = 12
Pode escolher caminho ruim no longo prazo
"""

# A*
"""
Decisão baseada em f(n) = g(n) + h(n)
g(n) impede escolhas ruins no longo prazo
"""
```

### Subida de Encosta (Hill Climbing)

O algoritmo de Subida de Encosta é uma técnica de otimização local que:
- Sempre move para o melhor estado vizinho
- Não mantém histórico de estados anteriores
- Funciona como um alpinista que sempre sobe pela inclinação mais íngreme


#### Estrutura Base
```python
class EstadoHillClimbing:
    def __init__(self, tabuleiro, movimento=None):
        self.tabuleiro = tabuleiro
        self.movimento = movimento
        self.valor_heuristico = None
    
    def avaliar(self, estado_objetivo):
        """
        Calcula e armazena o valor heurístico do estado.
        Usamos negativo pois queremos "subir" para minimizar a distância
        """
        if self.valor_heuristico is None:
            self.valor_heuristico = -calcular_manhattan(self.tabuleiro, estado_objetivo)
        return self.valor_heuristico
```

#### Algoritmo Principal
```python
def subida_encosta(estado_inicial, estado_objetivo, max_tentativas=100):
    """
    Implementa o algoritmo de subida de encosta para o 8-puzzle.
    
    Args:
        estado_inicial: Configuração inicial do tabuleiro
        estado_objetivo: Configuração objetivo
        max_tentativas: Número máximo de reinícios
    
    Returns:
        Lista de movimentos para solução ou None
    """
    melhor_solucao = None
    melhor_valor = float('-inf')
    
    for tentativa in range(max_tentativas):
        atual = EstadoHillClimbing(estado_inicial)
        movimentos = []
        
        while True:
            # Avalia estado atual
            valor_atual = atual.avaliar(estado_objetivo)
            
            # Gera todos os vizinhos possíveis
            vizinhos = gerar_vizinhos(atual.tabuleiro)
            if not vizinhos:
                break
                
            # Encontra o melhor vizinho
            melhor_vizinho = None
            melhor_valor_vizinho = float('-inf')
            
            for vizinho, movimento in vizinhos:
                estado_vizinho = EstadoHillClimbing(vizinho, movimento)
                valor_vizinho = estado_vizinho.avaliar(estado_objetivo)
                
                if valor_vizinho > melhor_valor_vizinho:
                    melhor_vizinho = estado_vizinho
                    melhor_valor_vizinho = valor_vizinho
            
            # Se não houver melhora, chegamos a um máximo local
            if melhor_valor_vizinho <= valor_atual:
                break
                
            # Move para o melhor vizinho
            atual = melhor_vizinho
            movimentos.append(atual.movimento)
            
            # Verifica se chegou ao objetivo
            if atual.tabuleiro == estado_objetivo:
                return movimentos
        
        # Atualiza melhor solução encontrada
        if atual.avaliar(estado_objetivo) > melhor_valor:
            melhor_solucao = movimentos
            melhor_valor = atual.avaliar(estado_objetivo)
    
    return melhor_solucao
```

#### Funções Auxiliares

```python
def gerar_vizinhos(tabuleiro):
    """
    Gera todos os estados vizinhos possíveis.
    
    Returns:
        Lista de tuplas (novo_tabuleiro, movimento)
    """
    vizinhos = []
    # Encontra posição do espaço vazio
    vazio_x, vazio_y = None, None
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                vazio_x, vazio_y = i, j
                break
    
    # Movimentos possíveis (cima, baixo, esquerda, direita)
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in movimentos:
        novo_x, novo_y = vazio_x + dx, vazio_y + dy
        
        if 0 <= novo_x < 3 and 0 <= novo_y < 3:
            # Cria novo tabuleiro
            novo_tab = [linha[:] for linha in tabuleiro]
            
            # Realiza movimento
            peca_movida = novo_tab[novo_x][novo_y]
            novo_tab[novo_x][novo_y] = 0
            novo_tab[vazio_x][vazio_y] = peca_movida
            
            movimento = f"Mover {peca_movida}"
            vizinhos.append((novo_tab, movimento))
    
    return vizinhos
```

### Exemplo de Execução Passo a Passo

```python
# Estado inicial e objetivo
inicial = [
    [1, 7, 2],
    [8, 4, 5],
    [6, 0, 3]
]

objetivo = [
    [1, 2, 3],
    [8, 4, 0],
    [7, 6, 5]
]

"""
Execução:

Passo 1:
Estado Atual:
1 7 2    Valor: -12 (Manhattan)
8 4 5    Vizinhos possíveis:
6 0 3    - Mover 3 (valor: -11)
         - Mover 5 (valor: -13)
         - Mover 6 (valor: -13)
         Escolhe: Mover 3

Passo 2:
1 7 2    Valor: -11
8 4 5    Vizinhos:
6 3 0    - Voltar (valor: -12)
         - Mover 5 (valor: -10)
         Escolhe: Mover 5

[continua...]
"""
```

### Tratamento de Máximos Locais

####  Implementação com Reinícios Aleatórios
```python
def subida_encosta_com_reinicio(estado_inicial, estado_objetivo, max_reinicio=10):
    """
    Implementa subida de encosta com reinícios aleatórios.
    """
    melhor_solucao = None
    melhor_valor = float('-inf')
    
    for _ in range(max_reinicio):
        # Embaralha estado inicial aleatoriamente
        estado_atual = embaralhar_estado(estado_inicial)
        solucao = subida_encosta(estado_atual, estado_objetivo)
        
        if solucao:
            valor = avaliar_solucao(solucao, estado_objetivo)
            if valor > melhor_valor:
                melhor_solucao = solucao
                melhor_valor = valor
    
    return melhor_solucao
```

### Análise de Desempenho

#### Complexidade
- Tempo: O(n) no melhor caso
- Espaço: O(1) - memória constante
- n = profundidade da solução

#### Vantagens e Desvantagens

###### Vantagens:
1. Memória constante
2. Implementação simples
3. Rápido quando funciona
4. Bom para problemas com poucos máximos locais

###### Desvantagens:
1. Pode ficar preso em máximos locais
2. Não garante solução ótima
3. Pode falhar em encontrar solução
4. Sensível ao estado inicial


### Conclusões

1. **Quando Usar:**
   - Problemas simples
   - Recursos muito limitados
   - Solução rápida necessária
   - Otimalidade não é crucial

2. **Quando Evitar:**
   - Problemas complexos
   - Necessidade de solução ótima
   - Muitos máximos locais
   - Alta precisão necessária

3. **Melhorias Possíveis:**
   - Implementar variações (estocástica, tabu)
   - Adicionar reinícios aleatórios
   - Ajustar parâmetros (temperatura, tamanho tabu)
   - Combinar com outras técnicas



## Problema do Caminho entre Cidades de Portugal

**Objetivo da Questão:** 
Encontrar o melhor caminho de Castelo Branco até Porto usando três diferentes algoritmos de busca.

**Dados do Problema:**
1. Estado Inicial: Castelo Branco
2. Estado Final (Objetivo): Porto
3. Dados fornecidos:
   - Mapa com conexões entre cidades
   - Tabela com distâncias em linha reta até Porto
   - Distâncias reais entre cidades conectadas

**Restrições:**
- Só é possível mover entre cidades que estão conectadas por estradas (linhas vermelhas no mapa)
- As distâncias consideradas são as mostradas no mapa em km
- A heurística utilizada é a distância em linha reta até Porto (da tabela)

**Algoritmos a serem aplicados:**
1. Busca Gulosa
2. A* (A Estrela)
3. Subida de Encosta (Hill Climbing)


### Distâncias em linha reta até Porto:

- **Aveiro**: 58 km
- **Beja**: 356 km
- **Braga**: 46 km
- **Bragança**: 172 km
- **Castelo Branco**: 177 km
- **Coimbra**: 108 km
- **Évora**: 294 km
- **Guarda**: 133 km
- **Leiria**: 157 km
- **Lisboa**: 274 km
- **Portalegre**: 231 km
- **Porto**: 0 km
- **Santarém**: 214 km
- **Setúbal**: 294 km
- **Viana do Castelo**: 62 km
- **Vila Real**: 76 km
- **Viseu**: 82 km

### Conexões entre cidades (com as distâncias):

- **Viana do Castelo** -- Porto: 70 km
- **Viana do Castelo** -- Braga: 50 km
- **Braga** -- Porto: 50 km
- **Braga** -- Vila Real: 100 km
- **Porto** -- Vila Real: 100 km
- **Porto** -- Aveiro: 70 km
- **Vila Real** -- Bragança: 140 km
- **Vila Real** -- Viseu: 100 km
- **Viseu** -- Guarda: 80 km
- **Viseu** -- Coimbra: 90 km
- **Aveiro** -- Coimbra: 60 km
- **Coimbra** -- Castelo Branco: 160 km
- **Coimbra** -- Leiria: 70 km
- **Castelo Branco** -- Guarda: 100 km
- **Castelo Branco** -- Portalegre: 80 km
- **Leiria** -- Santarém: 70 km
- **Santarém** -- Lisboa: 80 km
- **Lisboa** -- Setúbal: 50 km
- **Setúbal** -- Évora: 120 km
- **Évora** -- Beja: 80 km
- **Beja** -- Faro: 150 km

### Algoritmos

Para essa questão, vamos simular três algoritmos de busca:

1. **Busca em Largura (Breadth-First Search - BFS)**
2. **Busca de Custo Uniforme (Uniform Cost Search - UCS)**
3. **A*** (com função heurística da distância em linha reta até Porto)


## 1. Busca em Largura (BFS)

A busca em largura expande os nós camada por camada, sem priorizar caminhos mais curtos em relação à distância total.

### Passos:

1. **Início**: Castelo Branco (distância em linha reta: 177 km)
2. Expande para **Coimbra** (distância em linha reta: 108 km) e **Guarda** (distância em linha reta: 133 km).
3. Da cidade **Coimbra**, expande para **Aveiro** e **Leiria**.
4. Em **Aveiro** (mais próximo de Porto, distância em linha reta: 58 km), expande para **Porto**.
5. **Porto** alcançado!

### Caminho encontrado:
**Castelo Branco -> Coimbra -> Aveiro -> Porto**


## 2. Busca de Custo Uniforme (UCS)

A busca de custo uniforme expande o caminho de menor custo acumulado em cada iteração.

### Passos:

1. **Início**: Castelo Branco (177 km)
2. Da cidade **Castelo Branco**, expande para **Guarda** (distância acumulada: 100 km) e **Coimbra** (distância acumulada: 160 km).
3. Escolhe o nó de menor custo acumulado, **Guarda**.
4. Expande de **Guarda** para **Viseu**.
5. De **Viseu**, expande para **Coimbra** e **Vila Real**.
6. Escolhe o caminho com menor custo acumulado e continua até **Porto**.

### Caminho encontrado:
**Castelo Branco -> Guarda -> Viseu -> Porto**


## 3. A* (A Estrela)

O A* utiliza a função de avaliação \( f(n) = g(n) + h(n) \), onde \( g(n) \) é o custo acumulado até o nó atual e \( h(n) \) é a heurística da distância em linha reta até Porto.

### Passos:

1. **Início**: Castelo Branco (heurística: 177 km)
2. Da cidade **Castelo Branco**, expande para **Guarda** e **Coimbra**.
   - **Coimbra** é selecionado pela menor \( f(n) \).
3. Expande **Coimbra** para **Aveiro**.
   - **Aveiro** é selecionado pela menor \( f(n) \).
4. Expande **Aveiro** e encontra **Porto**.

### Caminho encontrado:
**Castelo Branco -> Coimbra -> Aveiro -> Porto**


Aqui está a apresentação da questão em um formato claro e organizado:


## Inferência com Busca Heurística

Dada a Base de Conhecimento (BC) composta pelas sentenças \( S1 \) a \( S9 \) e um conjunto de regras de inferência, demonstre que é possível provar \( H \) a partir da BC. Use uma abordagem de **busca heurística** (por exemplo, com o algoritmo A*), mostrando o passo a passo da derivação.

Para provar \( H \) usando uma abordagem de **busca heurística** com o **algoritmo A\*** em lógica proposicional, vamos estruturar a prova como um processo de busca onde cada estado representa uma derivação (ou passo lógico) a partir das sentenças já conhecidas.

Nossa Base de Conhecimento (BC) consiste nas sentenças \( S1 \) a \( S9 \), e vamos aplicar regras de inferência para verificar se conseguimos derivar \( H \).

### Informações Iniciais

#### Sentenças da Base de Conhecimento (BC):

1. \( S1: (A \land B) \rightarrow C \)
2. \( S2: A \rightarrow D \)
3. \( S3: (C \land D) \rightarrow E \)
4. \( S4: (B \land E \land F) \rightarrow G \)
5. \( S5: (A \land E) \rightarrow H \)
6. \( S6: (D \land E \land H) \rightarrow I \)
7. \( S7: A \) (fato)
8. \( S8: B \) (fato)
9. \( S9: F \) (fato)

Nosso objetivo é provar que **\( H \) pode ser derivado a partir da BC**, ou seja, \( \text{BC} \vdash H \).

#### Regras de Inferência:

Vamos usar as seguintes regras de inferência:

- **MP (Modus Ponens)**: \( P \rightarrow Q \) e \( P \) juntos produzem \( Q \).
- **Introdução do \(\land\)**: \( P \) e \( Q \) produzem \( P \land Q \).


### Estratégia com Algoritmo A*

1. **Estado Inicial**: \( S7: A \), \( S8: B \), \( S9: F \).
2. **Objetivo**: Derivar \( H \).

O algoritmo A* usará uma função de custo, onde a **heurística** será a contagem de sentenças faltantes para atingir \( H \).

### Passos de Derivação

1. **Estado 0**: Inicialmente temos \( A \), \( B \), e \( F \).

2. **Passo 1 (Aplicando \( S1 \) com MP)**:
   - De \( S1: (A \land B) \rightarrow C \) e \( A \land B \) (temos \( A \) e \( B \)), obtemos **\( C \)**.
   - **Novo Estado**: \( A \), \( B \), \( F \), \( C \).

3. **Passo 2 (Aplicando \( S2 \) com MP)**:
   - De \( S2: A \rightarrow D \) e \( A \), obtemos **\( D \)**.
   - **Novo Estado**: \( A \), \( B \), \( F \), \( C \), \( D \).

4. **Passo 3 (Aplicando \( S3 \) com MP)**:
   - De \( S3: (C \land D) \rightarrow E \) e \( C \land D \) (temos \( C \) e \( D \)), obtemos **\( E \)**.
   - **Novo Estado**: \( A \), \( B \), \( F \), \( C \), \( D \), \( E \).

5. **Passo 4 (Aplicando \( S5 \) com MP)**:
   - De \( S5: (A \land E) \rightarrow H \) e \( A \land E \) (temos \( A \) e \( E \)), obtemos **\( H \)**.
   - **Novo Estado**: \( A \), \( B \), \( F \), \( C \), \( D \), \( E \), \( H \).

### Conclusão

Assim, **\( H \)** foi derivado com sucesso a partir da base de conhecimento.

