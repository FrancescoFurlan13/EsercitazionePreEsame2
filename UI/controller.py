import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._model.buildGraph()

        # Aggiorna la View con i dettagli del grafo
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Nodi del grafo: {len(self._model._graph.nodes())}"))
        self._view.txt_result.controls.append(ft.Text(f"Archi del grafo: {len(self._model._graph.edges())}"))

        for g in  self._model.essential_genes:
            self._view.ddGene.options.append(ft.dropdown.Option(g))
        self._view.update_page()



    def handle_Geni(self, e):
        gene = self._view.ddGene.value
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Gene selezionato: {gene}"))

        adjacent_genes = self._model.get_adjacent_genes(gene)
        for adj_gene, edge_data in adjacent_genes:
            weight = edge_data['weight']
            self._view.txt_result.controls.append(ft.Text(f"Gene: {adj_gene}, Peso: {weight}"))

        self._view.update_page()

    def handle_search(self, e):
        pass