import grafo

g = grafo.Grafo()
g.ler_arquivo("ex.txt")
print(g.Bellman_Ford(0))
# print(grafo1.busca_largura(0, 5))
# print(grafo1.adjacentes_peso(0))
