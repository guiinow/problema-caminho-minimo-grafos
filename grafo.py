from cmath import inf
from dis import dis
import math
from queue import PriorityQueue
from re import I


class Grafo:
    def __init__(self, num_vert=0, num_arestas=0, lista_adj=None, mat_adj=None, lista_arestas=None):
        self.num_vert = num_vert
        self.num_arestas = num_arestas
        if lista_adj is None:
            self.lista_adj = [[] for i in range(num_vert)]
        else:
            self.lista_adj = lista_adj
        if mat_adj is None:
            self.mat_adj = [[0 for j in range(num_vert)]
                            for i in range(num_vert)]
        else:
            self.mat_adj = mat_adj
        if lista_arestas is None:
            self.lista_arestas = [[] for i in range(num_vert)]
        else:
            self.lista_arestas = lista_arestas

    def add_aresta(self, u, v, w=1):
        """Adiciona aresta de u a v com peso w"""
        self.num_arestas += 1
        if u < self.num_vert and v < self.num_vert:
            self.lista_adj[u].append((v, w))
            self.mat_adj[u][v] = w
        else:
            print("Aresta invalida!")

    def ler_arquivo(self, nome_arq):
        """Le arquivo de grafo no formato dimacs"""
        try:
            arq = open(nome_arq)
            # Leitura do cabecalho
            str = arq.readline()
            str = str.split(" ")
            self.num_vert = int(str[0])
            cont_arestas = int(str[1])
            # Inicializacao das estruturas de dados
            self.lista_adj = [[] for i in range(self.num_vert)]
            self.mat_adj = [[0 for j in range(self.num_vert)]
                            for i in range(self.num_vert)]
            # Le cada aresta do arquivo
            for i in range(0, cont_arestas):
                str = arq.readline()
                str = str.split(" ")
                u = int(str[0])  # Vertice origem
                v = int(str[1])  # Vertice destino
                w = int(str[2])  # Peso da aresta
                self.add_aresta(u, v, w)
                self.lista_arestas.append((u, v, w))
        except IOError:
            print("Nao foi possivel encontrar ou ler o arquivo!")

    def busca_largura(self, s, target):
        """Retorna a ordem de descoberta dos vertices pela 
        busca em largura a partir de s"""

        desc = [0 for v in range(self.num_vert)]
        Q = [s]  # queue: fila de vertices para serem descobertos
        R = [s]  # reachable, lista de vertices descobertos
        desc[s] = 1  # posição dos vertices descobertos

        while Q:
            u = Q.pop(0)
            for (v, w) in self.lista_adj[u]:
                if desc[v] == 0:
                    Q.append(v)
                    R.append(v)
                    desc[v] = 1
                    if(desc[v] == target):
                        break
        return R

    # def Dijkstra(self, s):
    #     dist = [float('inf') for v in range(self.num_vert)]
    #     pred = [None for v in range(self.num_vert)]
    #     dist[s] = 0
    #     Q = self.num_vert
    #     while(Q != None):
    #         u = (for i in range[dist[i]]:
    #              u=None
    #              min_dist=math.inf
    #              for i in range Q:
    #              if(dist[i] < min_dist):
    #              u=min_dist=dist[i])
    #         Q = Q - {u}
    #         for v

    def Bellman_Ford(self, s=0):
        dist = [math.inf for v in range(self.num_vert)]
        pred = [None for v in range(self.num_vert)]
        dist[s] = 0
        for i in range(self.num_vert-1):
            trocou = False
            for u, v, w in self.lista_arestas:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
                    trocou = True
            if trocou == False:
                break
        return dist, pred
