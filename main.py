import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image

class StartScreen(FloatLayout):

    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        self.splitsButton = Button(text="Splits", size_hint=(.2,.1), pos_hint={'center_x':.5, 'center_y':.5}, background_color=(0.2,0.2,1,0.8))
        self.add_widget(self.splitsButton)

        self.optionsButton = Button(text='Options', size_hint=(.2,.1), pos_hint={'center_x':.5, 'center_y':.38})
        self.add_widget(self.optionsButton)

        self.logo = Image(source='C:\github\intro to programming\ITPFinalProject\Resources\Images\mySplit_Logo.png',pos_hint={'center_x':.5,'center_y':.8})
        self.add_widget(self.logo)
class MyApp(App):

    def build(self):
        return StartScreen()

if __name__ == '__main__':
    MyApp().run()