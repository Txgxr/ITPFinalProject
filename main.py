import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder

class StartScreen(Screen, FloatLayout):

    def __init__(self, **kwargs):
        
        super(StartScreen, self).__init__(**kwargs)
        self.splitsButton = Button(text="Splits", size_hint=(.2,.1), pos_hint={'center_x':.5, 'center_y':.5}, background_color=(0.2,0.2,1,0.8))
        self.add_widget(self.splitsButton)
        self.splitsButton.bind(on_press=self.toSplitsScreen)

        self.optionsButton = Button(text='Options', size_hint=(.2,.1), pos_hint={'center_x':.5, 'center_y':.38}, background_color=(0.2,0.2,1,0.8))
        self.add_widget(self.optionsButton)

        self.logo = Image(source='C:\github\intro to programming\ITPFinalProject\Resources\Images\mySplit_Logo.png',pos_hint={'center_x':.5,'center_y':.8})
        self.add_widget(self.logo)

    def toSplitsScreen(self, instance):
        sm.current='splits'
        return sm

class SplitsScreen(Screen, FloatLayout):
    
    def __init__(self, **kwargs):
        super(SplitsScreen, self).__init__(**kwargs)
        self.newSplitButton = Button(text='New Split', size_hint=(.2,.1), pos_hint={'x':.75, 'y':.75}, background_color=(0.2,0.2,1,0.8))
        self.add_widget(self.newSplitButton)

        self.backToMenuButton = Button(text='Back', size_hint=(.2,.1), pos_hint={'x':.05, 'y':.75}, background_color=(0.2,0.2,1,0.8))
        self.add_widget(self.backToMenuButton)
        self.backToMenuButton.bind(on_press=self.toStartScreen)

        self.logo = Image(source='C:\github\intro to programming\ITPFinalProject\Resources\Images\mySplit_Logo.png',pos_hint={'center_x':.5,'center_y':.8})
        self.add_widget(self.logo)

    def toStartScreen(self, instance):
        sm.current='start'
        return sm

       


class MySplit(App):

    def build(self):
        global sm
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(SplitsScreen(name='splits'))

        sm.current='start'

        return sm

if __name__ == '__main__':
    MySplit().run()