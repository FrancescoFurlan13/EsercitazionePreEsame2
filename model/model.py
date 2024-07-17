from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self.essential_genes = []
        self.idMap = {}
        self.buildGraph()

    def buildGraph(self):
        self._graph.clear()

        essential_genes = DAO.getGenesE()
        interactions = DAO.getInteractions()

        # Aggiungi i nodi al grafo e popola idMap
        for gene in essential_genes:
            self._graph.add_node(gene["GeneID"], chromosome=gene["Chromosome"])
            self.idMap[gene["GeneID"]] = gene

        # Aggiungi gli archi al grafo con i pesi calcolati
        for interaction in interactions:
            gene1 = interaction["GeneID1"]
            gene2 = interaction["GeneID2"]
            if gene1 in self.idMap and gene2 in self.idMap:
                corr = abs(interaction["Expression_Corr"])
                if self.idMap[gene1]["Chromosome"] == self.idMap[gene2]["Chromosome"]:
                    weight = 2 * corr
                else:
                    weight = corr
                self._graph.add_edge(gene1, gene2, weight=weight)

        self.essential_genes = [gene["GeneID"] for gene in essential_genes]

    def get_adjacent_genes(self, gene):
        if gene not in self._graph:
            return []

        # Recupera le localizzazioni connesse e i dettagli dell'arco
        connected = list(self._graph[gene].items())
        connected_sorted = sorted(connected, key=lambda x: x[1]['weight'], reverse=True)
        return connected_sorted