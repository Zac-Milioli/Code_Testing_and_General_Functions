from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class TaskList(Screen):
    def __init__(self, tasks=[], **kwargs):
        super(TaskList, self).__init__(**kwargs)
        for i in tasks:
            self.ids.box.add_widget(Tarefa(text=i))
    
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Tarefa(text=texto))
        self.ids.texto.text = ''

class Tarefa(BoxLayout):
    def __init__(self, text='', **kwargs):
        super(Tarefa, self).__init__(**kwargs)
        self.ids.label.text = text

class MeuApp(App):
    def build(self):
        return Gerenciador()

MeuApp().run()
