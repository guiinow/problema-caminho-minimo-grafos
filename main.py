import grafo
import time

g = grafo.Grafo()

# arquivo = input('Digite o arquivo de texto:')
# g.ler_arquivo(arquivo)

g.ler_arquivo('toy.txt')

if(g.ler_arquivo == 1):
    print('Busca Largura')
elif(g.ler_arquivo == 2):
    print('Dijkstra')
elif(g.ler_arquivo == 3):
    print('Bellman Ford')

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

print('Busca Largura')
BLinicio = time.time()
print(g.busca_largura_caminhos(0, 3))
BLfim = time.time()
BLtime = BLfim-BLinicio
print('BLTempo: %.5fs' % (BLtime))
