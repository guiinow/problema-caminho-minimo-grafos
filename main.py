import grafo
import time

g = grafo.Grafo()

# arquivo = input('Digite o arquivo de texto:')
# g.ler_arquivo(arquivo)

g.ler_arquivo('toy.txt')

inicio = time.time()

print(g.Bellman_Ford(0, 2))

fim = time.time()
BFtime = fim - inicio
print('Tempo: %.5fs' % (BFtime))
# inicio = time.time()
# print(g.Dijkstra(0))
# fim = time.time()
t = 3

caminho = [0 for v in range(t)]

for i in range(t):
    caminho[i] = (g.busca_largura(0)[i])

print(caminho)

print('total: ')
print(g.busca_largura(0))
# print(g.busca_largura(0)[-2])

print('Dijkstra')
print(g.Dijkstra(0))
