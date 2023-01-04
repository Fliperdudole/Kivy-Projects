import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse,Color
from kivy.uix.button import Button

class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Color(1, 0, 0, .5, mode='rgba')
            self.circles = []

        self.erase_button = Button(text='Erase', size_hint=(.1, .1), pos_hint={'x': .9, 'y': .9})
        self.erase_button.bind(on_press=self.erase_drawing)
        self.add_widget(self.erase_button)

    def on_touch_move(self, touch):
        with self.canvas:
            Color(1, 1, 1, 1, mode='rgba')
            circle = Ellipse(pos=(touch.x - 5, touch.y), size=(10, 10))
            self.circles.append(circle)

    def erase_drawing(self, instance):
        self.canvas.clear()
        self.circles = []
        
        self.erase_button = Button(text='Erase', size_hint=(.1, .1), pos_hint={'x': .9, 'y': .9})
        self.erase_button.bind(on_press=self.erase_drawing)
        self.add_widget(self.erase_button)

class BasicApp(App):
    def build(self):
        return Touch()

if __name__ == "__main__":
    BasicApp().run()