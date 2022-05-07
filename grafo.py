from queue import PriorityQueue

class Grafo:
    def __init__(self, num_vert = 0, num_arestas = 0, lista_adj = None, mat_adj = None):
        self.num_vert = num_vert
        self.num_arestas = num_arestas
        if lista_adj is None:
            self.lista_adj = [[] for i in range(num_vert)]
        else:
            self.lista_adj = lista_adj
        if mat_adj is None:
            self.mat_adj = [[0 for j in range(num_vert)] for i in range(num_vert)]
        else:
            self.mat_adj = mat_adj

    def add_aresta(self, u, v, w = 1):
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
            #Leitura do cabecalho
            str = arq.readline()
            str = str.split(" ")
            self.num_vert = int(str[0])
            cont_arestas = int(str[1])
            #Inicializacao das estruturas de dados
            self.lista_adj = [[] for i in range(self.num_vert)]
            self.mat_adj = [[0 for j in range(self.num_vert)] for i in range(self.num_vert)] 
            #Le cada aresta do arquivo
            for i in range(0,cont_arestas):
                str = arq.readline()
                str = str.split(" ")
                u = int(str[0]) #Vertice origem
                v = int(str[1]) #Vertice destino
                w = int(str[2]) #Peso da aresta
                self.add_aresta(u, v, w)
        except IOError:
            print("Nao foi possivel encontrar ou ler o arquivo!")

    def busca_largura(self, s, target):
        """Retorna a ordem de descoberta dos vertices pela 
        busca em largura a partir de s"""

        desc = [0 for v in range(self.num_vert)]
        Q = [s] #queue: fila de vertices para serem descobertos
        R = [s] # reachable, lista de vertices descobertos
        desc[s] = 1 # posição dos vertices descobertos

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

    #     dist = { v:float('inf') for v in range(self.num_vert)}
    #     pred = {None for i in range(self.num_vert)}

    #     dist[s] = 0
    #     queue = self.num_vert

    
    #     a = PriorityQueue()

    #     a.put((0, s))
    
    #     while not a.empty():
    #         (distancia, vertice_atual) = a.get()
    #         self.vertices_visitados.append(vertice_atual)
    
    #         for vizinho in range(self.num_vert):
    #             if self.num_arestas[vertice_atual][vizinho] != -1:
    #                 distancia = self.num_arestas[vertice_atual][vizinho]
    #                 if vizinho not in self.vertices_visitados:
    #                     custo = dist[vizinho]
    #                     novo_custo = dist[vertice_atual] + distancia
    #                     if novo_custo < custo:
    #                         a.put((novo_custo, vizinho))
    #                         dist[vizinho] = novo_custo
    #     return dist

    def Bellman_Ford(self,s):

        dist = {v:float('inf') for v in range(self.num_vert)}
        pred = {None for v in range(self.num_vert)}

        dist[s] = 0
        for i in range(0, self.num_vert-1):
            trocou = False
            for u, v, w in self.num_arestas:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
                    trocou = True
            if trocou == False:
                break

            #descobrir, nas linhas 105 e 106 como achar o peso
    
    def adjacentes_peso(self, u):
        """Retorna a lista dos vertices adjacentes a u no formato (v, w)"""
        return self.lista_adj[u-1]


