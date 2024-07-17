import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None

        # graphical elements
        self._title = None
        self.txt_name = None

        self.btnGeniAd = None
        self._btnGraph = None
        self.btn_search = None

        self.txt_result = None

        self.ddGene = None

        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Lab14-Simulazione esame gene_small", color="blue", size=24)
        self._page.controls.append(self._title)


        self._btnGraph= ft.ElevatedButton(text="Crea grafo", on_click=self._controller.handle_graph, width=600)
        row1 = ft.Row([self._btnGraph],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self._page.update()

        #ROW with some controls
        # text field for the name
        self.ddGene = ft.Dropdown(label="Genes", width=300)
        self.btnGeniAd = ft.ElevatedButton(text="Geni Adiacenti", on_click=self._controller.handle_Geni)

        row2 = ft.Row([self.ddGene, self.btnGeniAd],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()




    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
