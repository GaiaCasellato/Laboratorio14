import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = DAO.getAnni()
        self._listShape = DAO.getForme()

    def fillDD(self):
        for anno in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(anno))
        self._view.update_page()

    def fillShape(self):
        for shape in self._listShape:
            self._view.ddshape.options.append(ft.dropdown.Option(shape))
        self._view.update_page()
    def handle_graph(self, e):
        self._view.txt_result.clean()
        self._model.buildGraph(self._view.ddshape.value, self._view.ddyear.value)

        self._view.txt_result.controls.append(ft.Text(
            f"Numero di vertici: {self._model.get_num_of_nodes()} Numero di archi: {self._model.get_num_of_edges()}"))
        for i in self._model._grafo.nodes:
            self._view.txt_result.controls.append(ft.Text(f"Nodo {i.id}, somma pesi su archi = {self._model.sommaPesi(self._view.ddshape.value, self._view.ddyear.value,i)} "))
        self._view.update_page()
    def handle_path(self, e):
        pass