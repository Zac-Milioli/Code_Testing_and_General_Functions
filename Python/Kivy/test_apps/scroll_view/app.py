from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class Tasks(ScrollView):
    def __init__(self, tasks, **kwargs):
        super().__init__(**kwargs)
        for _ in range(5,tasks):
            self.ids.box.add_widget(Label(text='Role a tela', font_size=_, size_hint_y=None, height=200))
        self.ids.box.add_widget(Label(text="Me faz um pix chave zacmilioli@gmail.com", font_size=50, size_hint_y=None, height=200))

class MyApp(App):
    def build(self):
        return Tasks(250)

MyApp().run()
