from kivy.app import App 
from kivy.lang import Builder
import requests

# Carrega a tela principal
GUI = Builder.load_file(r"screen.kv")

class MyApp(App):
    # Função padrão que retorna a tela do app
    def build(self):
        return GUI
    
    # Função de inicialização
    def on_start(self):
        m1, m2, m3 = 'USD', 'ETH', 'BTC'
        v1, v2, v3 = self.get_quotation(m1, m2, m3)
        # root é o aplicativo GUI
        # os ids retorna um hashmap contendo os ids e valores do arquivo kv 
        self.root.ids['moeda1'].text = v1
        self.root.ids['moeda2'].text = v2
        self.root.ids['moeda3'].text = v3

    def get_quotation(self, moeda1, moeda2, moeda3):
        cota1 = requests.get(f"https://economia.awesomeapi.com.br/last/{moeda1}-BRL").json()[f"{moeda1}BRL"]["bid"]
        cota2 = requests.get(f"https://economia.awesomeapi.com.br/last/{moeda2}-BRL").json()[f"{moeda2}BRL"]["bid"]
        cota3 = requests.get(f"https://economia.awesomeapi.com.br/last/{moeda3}-BRL").json()[f"{moeda3}BRL"]["bid"]
        return f"{moeda1}: {cota1}", f"{moeda2}: {cota2}", f"{moeda3}: {cota3}"



if __name__ == "__main__":
    app = MyApp().run()
