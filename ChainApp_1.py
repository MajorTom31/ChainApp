from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.core.window import Window

Window.size = (480, 853)

from kivy.config import Config
Config.set('kivy', 'keyboard_mode',
           'systemanddock')
class Container(GridLayout):
    pass

    # new_tile = ObjectProperty()
    # def create_tile(self):
    #     layout.add_widget(New Cahin)

class ChainApp(App):
    def build(self):
        return Container()

if __name__ == "__main__":
    ChainApp().run()