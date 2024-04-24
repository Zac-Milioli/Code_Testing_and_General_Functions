from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

class Tasks(ScrollView):
    def __init__(self, tasks, **kwargs):
        super().__init__(**kwargs)
        for i in tasks:
            self.ids.box.add_widget(Tarefa(text=i))

class Tarefa(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

class MyApp(App):
    def build(self):
        return Tasks(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

MyApp().run()
