from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Tasks(BoxLayout):
    def __init__(self, tarefas, **kwargs): # keyword arguments dicionário
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.add_widget(Label(text=tarefa, font_size=30))

class MyApp(App):
    def build(self):
        return Tasks(['Trabalhar', 'Estudar', 'Comer', 'Lutar com um dragão', 'Dormir', 'Quebrar a janela do vizinho'], orientation='vertical')


if __name__ == "__main__":
    MyApp().run()
