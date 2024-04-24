from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class Gerenciador(ScreenManager):
    pass

class TaskList(Screen):
    def __init__(self, tasks=[], **kwargs):
        super().__init__(**kwargs)
        for i in tasks:
            self.ids.box.add_widget(Tarefa(text=i))
    
    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Tarefa(text=texto))
        self.ids.texto.text = ''

class Tarefa(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

class MyApp(App):
    def build(self):
        return Gerenciador()

MyApp().run()
