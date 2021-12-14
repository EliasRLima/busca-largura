#importando pacote para estrutura de dados
from collections import defaultdict


class Grafo:

    def __init__(self):
        self.grafo = defaultdict(list)

    def inserirVertice(self, index, nodo):
        self.grafo[index].append(nodo)

    def realizarBuscaLargura(self, raiz):
        lista = []
        lista.append(raiz)
        visitado = ([False] * (len(self.grafo)))
        visitado[raiz] = True
        while lista:
            raiz = lista.pop(0)
            print(raiz, " ")
            for idx in self.grafo[raiz]:
                if visitado[idx] != True:
                    lista.append(idx)
                    visitado[idx] = True


#testando
# exemplo de grafo:
#         0----1 
#         |    | \
#         2----3--4 
#
#
# criando exemplo:
grf = Grafo()
grf.inserirVertice(0, 1) 
grf.inserirVertice(0, 2) 
grf.inserirVertice(1, 0) 
grf.inserirVertice(1, 3)
grf.inserirVertice(1, 4)
grf.inserirVertice(2, 0)
grf.inserirVertice(2, 3)
grf.inserirVertice(3, 1)
grf.inserirVertice(3, 2)
grf.inserirVertice(3, 4)
grf.inserirVertice(4, 1)   
grf.inserirVertice(4, 3)    

print ("Segue a busca de largura começando pelo vertice 0: ")
grf.realizarBuscaLargura(0) 