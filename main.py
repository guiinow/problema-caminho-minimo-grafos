import grafo
import time

g = grafo.Grafo()

# arquivo = input('Digite o arquivo de texto:')
# g.ler_arquivo(arquivo)

g.ler_arquivo('toy.txt')
print("peso")
g.peso

# if(g.peso<0):
#     print('')

# fazer um if para testar os pesos do grafo, se houverem grafos com peso negativo: usar Bellman_Ford, caso contrário ultilizar Dijkstra

print("-----------")

print('Bellman Ford:')
BFinicio = time.time()
print(g.Bellman_Ford(0, 3))
BFfim = time.time()
BFtime = BFfim - BFinicio
print('BFTempo: %.5fs' % (BFtime))

print("-----------")

print('Dijkstra')
Dinicio = time.time()
g.Dijkstra(0, 3)
Dfim = time.time()
Dtime = Dfim-Dinicio
print('DTempo: %.5fs' % (Dtime))

print("-----------")


print(g.busca_largura(0))
