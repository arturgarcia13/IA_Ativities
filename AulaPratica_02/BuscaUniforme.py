import heapq

def busca_custo_uniforme_exp(graph, start, goal):
    # Fila de prioridade: (custo_acumulado, nó_atual, caminho)
    fila = [(0, start, [start])]
    visitados = set()
    ordem_expansao = []

    while fila:
        custo, no, caminho = heapq.heappop(fila)
        
        if no in visitados:
            continue
        
        visitados.add(no)
        ordem_expansao.append(no)

        if no == goal:
            return ordem_expansao, caminho, custo
        
        for vizinho, peso in graph.get(no, []):
            if vizinho not in visitados:
                heapq.heappush(fila, (custo + peso, vizinho, caminho + [vizinho]))
    
    return None, None, None

def busca_custo_uniforme(inicio, objetivo):
    # Cria a fila de prioridade (heapq é a estrutura de fila de prioridade)
    fila = []
    
    # Adiciona o nó inicial com custo 0
    heapq.heappush(fila, (0, inicio, [inicio]))  # (custo acumulado, nó atual, caminho percorrido)
    
    # Conjunto para guardar nós visitados
    visitados = set()

    while fila:
        # Retira o nó com menor custo acumulado
        custo, no_atual, caminho = heapq.heappop(fila)

        print(f"Expansão do nó {no_atual} com custo {custo}")

        # Se o nó atual é o objetivo, acabou!
        if no_atual == objetivo:
            print(f"Caminho encontrado: {caminho} com custo total {custo}")
            return caminho, custo
        
        # Se o nó ainda não foi visitado
        if no_atual not in visitados:
            visitados.add(no_atual)

            # Para cada vizinho do nó atual
            for vizinho, custo_vizinho in graph.get(no_atual, []):
                if vizinho not in visitados:
                    # Adiciona o vizinho na fila com o custo acumulado
                    heapq.heappush(fila, (custo + custo_vizinho, vizinho, caminho + [vizinho]))
    
    # Se a fila acabar e não encontrar o objetivo
    print("Caminho não encontrado!")
    return None

# Chamando a função para buscar o caminho de 1 até 11
#busca_custo_uniforme(1, 11)
    
# Definindo o grafo
# Definindo o grafo como dicionário de listas
grafo = {
    1: [(2, 4), (3, 2)],
    2: [(4, 3), (5, 7)],
    3: [(5, 1), (6, 6)],
    4: [(7, 2)],
    5: [(7, 3)],
    6: [(8, 4)],
    7: [(9, 2)],
    8: [(9, 1)],
    9: [(10, 3)],
    10: [(11, 2)],
    11: []
}

graph = {
    1: [(2, 4), (3, 2)],
    2: [(4, 3), (5, 7)],
    3: [(5, 1), (6, 6)],
    4: [(7, 2)],
    5: [(7, 3)],
    6: [(8, 4)],
    7: [(9, 2)],
    8: [(9, 1)],
    9: [(10, 3)],
    10: [(11, 2)],
    11: []
}

# Rodar a busca
ordem_expansao, caminho, custo_total = busca_custo_uniforme_exp(graph, 1, 11)

# Mostrar o resultado
print(f"Ordem de expansão dos nós: {ordem_expansao}")
print(f"Caminho encontrado: {caminho}")
print(f"Custo total: {custo_total}")
