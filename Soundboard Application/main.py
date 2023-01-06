import os
import random
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color,Rectangle

class MyLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Set the color to white
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class SoundApp(App):
    def build(self):
        # Get the base path of the application
        base_path = os.path.dirname(__file__)

        # Create a relative path to the sound file
        self.sound_file_path = os.path.join(base_path, 'Sounds')

        # Create a button to play the sound file
        image= Image(source= os.path.join(base_path, 'Images', 'Button.png'))

        play_button = Button(text='Play Sound', background_color=[0,0,0,0])
        play_button.bind(on_release=self.play_sound)
        play_button.size_hint = (0.44, .75)
        play_button.pos_hint = {'center_x': 0.50, 'center_y': 0.50}

         # Create a layout to contain the buttons
        layout = MyLayout()
        layout.add_widget(play_button)
        layout.add_widget(image, index=0)
        
        return layout

    def play_sound(self, instance):
        # Get a list of all the files in the sound file directory
        sound_files = os.listdir(self.sound_file_path)

        # Choose a random sound file from the list
        sound_file = random.choice(sound_files)

        # Create the full path to the sound file
        sound_file_path = os.path.join(self.sound_file_path, sound_file)

        # Load the sound file
        sound = SoundLoader.load(sound_file_path)

        # Play the sound file
        sound.play()



if __name__ == '__main__':
    SoundApp().run()
