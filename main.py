import grafo
import time

g = grafo.Grafo()
# arquivo = input('Digite o arquivo de texto:')
# g.ler_arquivo(arquivo)
g.ler_arquivo('ex.txt')
inicio = time.time()
print(g.Bellman_Ford(0, 2))
fim = time.time()
print(fim - inicio)
# print(g.Dijkstra(0))
# print(grafo1.busca_largura(0, 5))
# print(grafo1.adjacentes_peso(0))
