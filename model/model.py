import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._idMap = {}
        self._edges = []
        self._nodes = []
        self._grafo = nx.Graph()



    def getYears(self):
        return DAO.getYears()

    def getTeams(self, anno):
        self._nodes = DAO.getNodes(anno)
        return self._nodes


    def crea_grafo(self):
        for n in self._nodes:
            self._idMap[n.teamCode] = n
            for n2 in self._nodes:
                if (n,n2) not in self._edges:
                    self._edges.append((n,n2,{'weight': n.salaries + n2.salaries}))

        self._grafo.add_nodes_from(self._nodes)
        self._grafo.add_edges_from(self._edges)

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)


    def getdetails(self, nodoStr):
        valori = nodoStr.split("–")
        nodo = self._idMap[valori[0]]

        adiacenti = self._grafo.neighbors(nodo)
        lista_adiacenti = []

        for a in adiacenti:
            lista_adiacenti.append((str(a), self._grafo.get_edge_data(nodo,a)['weight']))

        sorted(lista_adiacenti,key=lambda x:x[1], reverse=True)
        return lista_adiacenti

