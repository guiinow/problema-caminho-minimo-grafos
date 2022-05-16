from distutils.command.sdist import sdist
import grafo
import time

g = grafo.Grafo()

arquivo = input('Digite o arquivo de texto:')
g.ler_arquivo(arquivo)

origem = int(input("Informe a origem: "))
destino = int(input("Informe o destino: "))

if(g.ler_arquivo(arquivo) == 0):
    BLinicio = time.time()
    g.busca_largura_caminhos(origem, destino)
    BLfim = time.time()
    BLtime = BLfim-BLinicio
    print('Tempo: %.5fs' % (BLtime))
elif(g.ler_arquivo(arquivo) == 1):
    Dinicio = time.time()
    g.Dijkstra(origem, destino)
    Dfim = time.time()
    Dtime = Dfim-Dinicio
    print('Tempo: %.5fs' % (Dtime))
elif(g.ler_arquivo(arquivo) == 2):
    BFinicio = time.time()
    g.Bellman_Ford(origem, destino)
    BFfim = time.time()
    BFtime = BFfim - BFinicio
    print('Tempo: %.5fs' % (BFtime))
