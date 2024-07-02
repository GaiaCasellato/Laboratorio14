import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self.stati = DAO.getState()

    def buildGraph(self, shape, year):
        self._grafo.clear()
        self._nodes = self.stati
        self._edges = []
        self._grafo.add_nodes_from(self._nodes)
        for i in self._nodes:
            for j in self._nodes:
                if i != j:
                    if len(DAO.getArco(i.id,j.id)) > 0 :
                        self._grafo.add_edge(i, j, weight= DAO.getPeso(shape,year,i.id,j.id))

    def sommaPesi(self, shape, year, stato):
            vicini = self._grafo.neighbors(stato)
            sommaPeso = 0
            for i in vicini:
                sommaPeso += DAO.getPeso(shape, year, stato.id, i.id)[0]
            return sommaPeso


    def get_num_of_nodes(self):
        return self._grafo.number_of_nodes()

    def get_num_of_edges(self):
        return self._grafo.number_of_edges()