import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._idMap = {}
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._year = None

    def handle_anno_selezionato(self, e):
        self._year = int(self._view.dd_year.value)
        teams = self._model.getTeams(self._year)
        self._view.txt_squadre.controls.append(ft.Text(f"Squadre presenti nell'anno {self._year}: {len(teams)}"))

        for a in teams:

            self._view.dd_team.options.append(ft.dropdown.Option(str(a)))
            self._view.txt_squadre.controls.append(ft.Text(f"{str(a)}"))
        self._view.update_page()

    def handle_crea_grafo(self, e):
        self._model.crea_grafo()
        self._view.txt_result.controls.append(ft.Text(f"il grafo ha {self._model.getNumNodes()} nodi"
                                                      f" e {self._model.getNumEdges()} archi"))
        self._view.update_page()

    def handle_dettagli(self, e):
        if self._view.dd_team.value is not None:
            lista = self._model.getdetails(self._view.dd_team.value)

            for a, peso in lista:
                self._view.txt_result.controls.append(ft.Text(f"{a}   -   {peso}"))
            self._view.update_page()
        else:
            self._view.create_alert("selezionare un team")


    def handle_path(self, e):
        if self._view.dd_team.value is not None:
            self._view.txt_result.clean()
            path, peso = self._model.cerca_cammino(self._view.dd_team.value)
            self._view.txt_result.controls.append(ft.Text(f"cammino di peso : {peso} "))
            for nodo in path:
                print(nodo)
                self._view.txt_result.controls.append(ft.Text(f"{nodo} "))
            self._view.update_page()
        else:
            self._view.create_alert("selezionare un team")



    def fillDDyear(self):
        anni = self._model.getYears()
        for a in anni :
            self._view.dd_year.options.append(ft.dropdown.Option(a))