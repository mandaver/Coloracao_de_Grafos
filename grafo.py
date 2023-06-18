import networkx as nx
import matplotlib.pyplot as plt

def colorir_grafo(grafo):
    color_map = {}  # Dicionário para armazenar as cores atribuídas a cada vértice
    
    # Itera sobre os vértices do grafo
    for vertice in grafo.nodes:
        vizinhos_cores = set()  # Conjunto para armazenar as cores dos vizinhos do vértice
        
        # Obtém as cores dos vizinhos do vértice atual
        for vizinho in grafo.neighbors(vertice):
            if vizinho in color_map:
                vizinhos_cores.add(color_map[vizinho])
        
        # Encontra a cor disponível para o vértice
        for cor in range(len(grafo.nodes)):
            if cor not in vizinhos_cores:
                color_map[vertice] = cor
                break
    
    return color_map

# Cria um grafo simples para exemplo
grafo = nx.Graph()
grafo.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])

# Chama a função para colorir o grafo
cores = colorir_grafo(grafo)

# Desenha o grafo com as cores atribuídas aos vértices
pos = nx.spring_layout(grafo)  # Define a posição dos nós no desenho
nx.draw(grafo, pos, with_labels=True, node_color=[cores[v] for v in grafo.nodes], node_size=500, font_size=12, font_color='black')

# Exibe o grafo
plt.show()
