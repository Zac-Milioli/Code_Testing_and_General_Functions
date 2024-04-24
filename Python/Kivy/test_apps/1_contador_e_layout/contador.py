from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class TestClass(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        button = Button(text="Botãozinho", font_size=30, on_release=self.incrementar, on_press=self.apertado)
        self.label = Label(text='0', font_size=30)
        box.add_widget(button)
        box.add_widget(self.label)

        box2 = BoxLayout(orientation='horizontal')
        button2 = Button(text="Segundo")
        label2 = Label(text="Segundo Texto qualquer")
        box2.add_widget(button2)
        box2.add_widget(label2)

        box.add_widget(box2)
        return box
    
    def incrementar(self, button):
        self.label.text = str(int(self.label.text)+1)
        button.text = "Botãozinho"

    def apertado(self, button):
        button.text = "Apertando"


if __name__ == "__main__":
    TestClass().run()