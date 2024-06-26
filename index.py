import networkx as nx
import matplotlib.pyplot as plt
import json

# Ler a matriz de adjacência do arquivo matriz.json
with open('matriz.json', 'r') as file:
    adj_matrix = json.load(file)

# Criar o grafo
G = nx.Graph()

# Adicionar as arestas ao grafo
for i in range(len(adj_matrix)):
    for j in range(len(adj_matrix[i])):
        if adj_matrix[i][j] != 0:
            G.add_edge(i, j, weight=adj_matrix[i][j])

# Obter a árvore geradora mínima do grafo
MST = nx.minimum_spanning_tree(G)

# Obter o subgrafo gerador completo de peso mínimo
CGMST = MST.copy()
edges_to_remove = []
for u, v in CGMST.edges():
    if CGMST.degree(u) == 1 or CGMST.degree(v) == 1:
        edges_to_remove.append((u, v))
CGMST.remove_edges_from(edges_to_remove)

# Definir os labels dos nós
node_labels = {0: "v1", 1: "v2", 2: "v3", 3: "v4", 4: "v5", 5: "v6"}

# Atualizar os labels dos nós no grafo
nx.set_node_attributes(G, node_labels, "label")

pos = {
     0: (0.0, 1.0),
     1: (0.9, 0.3),
     2: (0.59, -0.81),
     3: (0.0, -1.1),
     4: (-0.5, -0.8),
     5: (-0.9, 0.3)
}

# Plotar o grafo principal com as coordenadas lidas do arquivo coord.json
plt.figure(figsize=(16, 6))

# Plotar o grafo principal
plt.subplot(131)
nx.draw(G, pos, with_labels=True, labels=node_labels, node_size=500, node_color='lightblue', edge_color='gray', width=2, font_size=10, font_weight='bold', alpha=0.8)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')
plt.title("Grafo Principal")
plt.axis('off')

# Plotar a árvore geradora mínima
plt.subplot(132)
nx.draw(MST, pos, with_labels=True, labels=node_labels, node_size=500, node_color='lightblue', edge_color='gray', width=2, font_size=10, font_weight='bold', alpha=0.8)
labels = nx.get_edge_attributes(MST, 'weight')
nx.draw_networkx_edge_labels(MST, pos, edge_labels=labels, font_color='red')
plt.title("Árvore Geradora Mínima")
plt.axis('off')

# Plotar o subgrafo gerador completo de peso mínimo
plt.subplot(133)
nx.draw(CGMST, pos, with_labels=True, labels=node_labels, node_size=500, node_color='lightblue', edge_color='gray', width=2, font_size=10, font_weight='bold', alpha=0.8)
labels = nx.get_edge_attributes(CGMST, 'weight')
nx.draw_networkx_edge_labels(CGMST, pos, edge_labels=labels, font_color='red')
plt.title("Subgrafo Gerador Completo de Peso Mínimo")
plt.axis('off')

plt.tight_layout()
plt.show()
