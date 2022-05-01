from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from scrap import scrap20
import asyncio



class Container(GridLayout):
    def scrap_text(self):
        scrapper = scrap20()
        dollar = asyncio.run(scrapper.rubl_dollar())
        euro = asyncio.run(scrapper.rubl_euro())

        self.dollar.text = str(dollar) + "₽"
        
        self.euro.text = str(euro) + "₽"



class DollarApp(App):


    def build(self):

        self.title = 'B E Z D A R N O S T !'
        return Container()


app = DollarApp()
if __name__ == "__main__":
    app.run()