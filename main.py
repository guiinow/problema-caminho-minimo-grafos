import grafo

grafo1 = grafo.Grafo()
grafo1.ler_arquivo("datasets/teste.txt")
# print(grafo1.Bellman_Ford(0))  
# print(grafo1.busca_largura(0, 5))  
print(grafo1.adjacentes_peso(0))