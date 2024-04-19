from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.config import Config

Config.set('graphics', 'wight', '100')
Config.set('graphics', 'height', '1000')

class cardApp (App):
    def build(self):
        bl = BoxLayout(orientation='vertical', 
                       spacing = 10)
        btn1 = Button(text='First Card')
        btn2 = Button(text='Second Card')
        bl.add_widget(btn1)
        bl.add_widget(btn2)

        return bl

if __name__ == "__main__":
    cardApp().run()