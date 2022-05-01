import grafo

grafo1 = grafo.Grafo()
grafo1.ler_arquivo("grafo_largura.txt")
print(grafo1.busca_largura(0))  