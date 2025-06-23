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
            self._idMap[str(n)] = n
            for n2 in self._nodes:
                if (n,n2) not in self._edges and n!=n2:
                    self._edges.append((n,n2,{'weight': n.salaries + n2.salaries}))

        self._grafo.add_nodes_from(self._nodes)
        self._grafo.add_edges_from(self._edges)

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)


    def getdetails(self, nodoStr):
        nodo = self._idMap[nodoStr]
        print(nodo.ID)

        adiacenti = self._grafo.neighbors(nodo)
        lista_adiacenti = []

        for a in adiacenti:

            lista_adiacenti.append((str(a), self._grafo.get_edge_data(nodo,a)['weight']))

        sorted(lista_adiacenti,key=lambda x:x[1], reverse=True)
        return lista_adiacenti

    def cerca_cammino(self, partenza):

        nodo = self._idMap[partenza]
        print(nodo.ID)
        self._best_cammino = []
        self._best_peso = 0
        self._ricorsione([nodo], 0, {nodo}, 0)
        return self._best_cammino, self._best_peso

    def _ricorsione(self, cammino_parziale, peso_parziale, visited, peso_ultimo):
        ultimo = cammino_parziale[-1]

        # Caso finale: aggiorna se questo cammino è migliore
        if peso_parziale > self._best_peso:
            self._best_peso = peso_parziale
            self._best_cammino = list(cammino_parziale)

        for vicino in self._grafo.neighbors(ultimo):
            if vicino not in visited:
                peso = self._grafo[ultimo][vicino]['weight']
                if peso > peso_ultimo:
                    #print(str(vicino))
                    visited.add(vicino)
                    cammino_parziale.append(vicino)

                    self._ricorsione(cammino_parziale, peso_parziale + peso, visited, peso)

                    # Backtrack
                    visited.remove(vicino)
                    cammino_parziale.pop()

