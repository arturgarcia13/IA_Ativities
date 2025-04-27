graph = {
    '0': [],
    '1': [],
    '2': ['0', '1'],
    '3': ['2', '6'],
    '4': ['3'],
    '5': ['7'],
    '6': ['4', '5', '7'],
    '7': []
}

# Tentativa depth-first search
def dfs(graph, start, visitados=None):
    if not visitados:
        visitados = set()
    print(start, end=' ')
    for vizinho in graph[start]:
        visitados.add(vizinho)
        if vizinho not in visitados:
            dfs(graph, vizinho, visitados)

# Algoritmo de Busca em Largura (BFS)
def bfs(graph, start):
    visited = set()
    queue = [start]
    print(f'queue inicial: {queue}')
    visited.add(start)
    print(f'visited inicial: {visited}')
    while queue:
        vertex = queue.pop(0)
        print(f'vertex: {vertex}', end='\n')
        print(f'graph: {graph[vertex]}')
        for neighbor in graph[vertex]:
            print(f'neighbor para {graph[vertex]}: {neighbor}')
            if neighbor not in visited:
                visited.add(neighbor)
                print(f'Adicionando {neighbor} em visited: {visited}')
                queue.append(neighbor)
                print(f'Adicionando {neighbor} em queue: {queue}')
                
print('Busca em Largura:')
bfs(graph, '6')

graph = {
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Zerind': {'Oradea': 71, 'Arad': 75},
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Sibiu': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

