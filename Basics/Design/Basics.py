import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty



class BasicGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)


    def btn(self):
        print("Name:", self.name.text, "\nEmail:", self.email.text)
        self.name.text = ""
        self.email.text = ""




class BasicApp(App):
    def build(self):
        return BasicGrid()












if __name__== "__main__":
    BasicApp().run()