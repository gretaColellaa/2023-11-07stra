import flet as ft


class View(ft.UserControl):


    def __init__(self, page):
        self._page = page
        self._controller = None
        self.dd_year = None
        self.dd_team = None
        self.txt_squadre = None
        self.txt_result = None
        self.btn_crea_grafo = None
        self.btn_dettagli = None

    def load_interface(self):
        self._title = ft.Text("Campionato Formula1", color="blue", size=24)
        self._page.controls.append(self._title)

        # Dropdown anno
        self.dd_year = ft.Dropdown(label="Seleziona Anno", on_change=self._controller.handle_anno_selezionato)
        self._page.controls.append(self.dd_year)
        self._controller.fillDDyear()

        # Area per visualizzare le squadre (txtSquadre)
        self.txt_squadre = ft.ListView(expand=1, spacing=5, padding=10, auto_scroll=True, height=150)
        self._page.controls.append(ft.Text("Squadre nell'anno selezionato:"))
        self._page.controls.append(self.txt_squadre)

        # Dropdown per squadra da selezionare
        self.dd_team = ft.Dropdown(label="Seleziona Squadra")
        self._page.controls.append(self.dd_team)

        # Bottone per creare il grafo
        self.btn_crea_grafo = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handle_crea_grafo)
        self._page.controls.append(self.btn_crea_grafo)

        # Bottone per dettagli adiacenze
        self.btn_dettagli = ft.ElevatedButton(text="Dettagli", on_click=self._controller.handle_dettagli)
        self._page.controls.append(self.btn_dettagli)

        # Area risultati (txtResult)
        self.txt_result = ft.ListView(expand=1, spacing=5, padding=10, auto_scroll=True, height=200)
        self._page.controls.append(ft.Text("Risultati:"))
        self._page.controls.append(self.txt_result)

        self._page.update()

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

    def set_controller(self, controller):
        self._controller = controller

