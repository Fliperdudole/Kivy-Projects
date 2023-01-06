import os
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button

class SoundApp(App):
    def build(self):
        # Get the base path of the application
        base_path = os.path.dirname(__file__)

        # Create a relative path to the sound file
        self.sound_file_path = os.path.join(base_path, 'Sounds', 'lover.mp3')

        # Create a button to play the sound file
        play_button = Button(text='Play Sound')
        play_button.bind(on_release=self.play_sound)
        
        return play_button

    def play_sound(self, instance):
        # Load the sound file if it hasn't been loaded yet
        if not hasattr(self, 'sound'):
            self.sound = SoundLoader.load(self.sound_file_path)
        
        # Play the sound file
        self.sound.play()

if __name__ == '__main__':
    SoundApp().run()
