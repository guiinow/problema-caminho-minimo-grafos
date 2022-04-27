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

    def busca_largura(self, s):

        """Retorna a ordem de descoberta dos vertices pela 
        busca em largura a partir de s"""

        desc = [0 for v in range(self.num_vert)]
        Q = [s]
        R = [s]
        desc[s] = 1

        while Q:
            u = Q.pop(0)
        for (v, w) in self.lista_adj[u]:
            if desc[v] == 0:
                Q.append(v)
                R.append(v)
                desc[v] = 1
        return R
    
    