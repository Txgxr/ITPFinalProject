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
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import os

if not os.path.exists('C:\github\intro to programming\ITPFinalProject\Resources\Splits'):
    os.umask(0)
    os.mkdir('C:\github\intro to programming\ITPFinalProject\Resources\Splits', 0o777)
    os.chmod('C:\github\intro to programming\ITPFinalProject\Resources\Splits', 0o777)

class Split():
    def __init__(self, splitName):
        self.splitName = splitName

class StartScreen(Screen, FloatLayout):

    def __init__(self, **kwargs):
        
        super(StartScreen, self).__init__(**kwargs)
        self.splitsButton = Button(text="Splits", size_hint=(.2,.1), pos_hint={'center_x':.5, 'center_y':.5}, background_color=(0.2,0.2,1,0.8))
        self.add_widget(self.splitsButton)
        self.splitsButton.bind(on_press=self.toSplitsScreen)

        self.optionsButton = Button(text='Options', size_hint=(.2,.1), pos_hint={'center_x':.5, 'center_y':.38}, background_color=(0.2,0.2,1,0.8))
        self.add_widget(self.optionsButton)
        self.optionsButton.bind(on_press=self.toOptionsScreen)

        self.exitButton = Button(text="Exit", size_hint=(.2,.1), pos_hint={'center_x':.5, 'center_y':.26}, background_color=(0.2,0.2,1,0.8))
        self.add_widget(self.exitButton)
        self.exitButton.bind(on_press=MySplit().stop)

        self.logo = Image(source='C:\github\intro to programming\ITPFinalProject\Resources\Images\mySplit_Logo.png',pos_hint={'center_x':.5,'center_y':.8})
        self.add_widget(self.logo)

    def toSplitsScreen(self, instance):
        sm.current = "splits"
        return sm

    def toOptionsScreen(self, instance):
        sm.current = "options"
        return sm

class Split():
    def __init__(self, name, exCount, position, **kwargs):
        self.name = name
        self.exCount = exCount
        self.position = position




class SplitsScreen(Screen, FloatLayout):
    
    def __init__(self, **kwargs):
        super(SplitsScreen, self).__init__(**kwargs)
        self.newSplitButton = Button(text='New Split', size_hint=(.2,.1), pos_hint={'x':.75, 'y':.75}, background_color=(0.2,0.2,1,0.8))
        self.add_widget(self.newSplitButton)
        self.newSplitButton.bind(on_press=self.splitNamePopup)

        self.backToMenuButton = Button(text='Back', size_hint=(.2,.1), pos_hint={'x':.05, 'y':.75}, background_color=(0.2,0.2,1,0.8))
        self.add_widget(self.backToMenuButton)
        self.backToMenuButton.bind(on_press=self.toStartScreen)

        self.logo = Image(source='C:\github\intro to programming\ITPFinalProject\Resources\Images\mySplit_Logo.png',pos_hint={'center_x':.5,'center_y':.8})
        self.add_widget(self.logo)

        self.splitCount = 1
        self.splitEntries = os.listdir('C:\github\intro to programming\ITPFinalProject\Resources\Splits')

        for split in self.splitEntries:
            self.splitCount += 1
            self.add_widget(Button(text=f'{os.path.splitext(split)[0]}', pos_hint={'center_x':.5,'center_y':.1*self.splitCount*1.5}, size_hint=(None, None), size=(450, 80), font_size=25, background_color=(0.1,0.1,1,0.5)))
            print(os.path.splitext(split)[0])
            print(self.splitCount)
        # self.splits = os.listdir('C:\github\intro to programming\ITPFinalProject\Resources\Splits')
        # self.splitCount = 1
        # for split in self.splits:
        #     self.add_widget(self.add_widget(Button(text=f'{split}', pos_hint={'center_x':.5,'center_y':.1}, size_hint=(None, None), size=(450, 80), font_size=25, background_color=(0.1,0.1,1,0.5))))
        #     self.splitCount += 1

    def toStartScreen(self, instance):
        sm.current='start'
        return sm
    
    def splitNamePopup(self, instance):
        splitNameBox = FloatLayout()

        splitPopupTextInput = TextInput(text='', size_hint=(None,None), size=(200,50), pos_hint={'center_x':.5, 'center_y':.6}, multiline=False, font_size=25, halign='center', )
        closeSplitPopupButton = Button(text='Close', size_hint=(None, None), size=(90,60), pos_hint={'center_x':.25, 'center_y':.2})
        splitPopupEnterButton = Button(text='Enter', size_hint=(None, None), size=(90, 60), pos_hint={'center_x':.75, 'center_y':.2})
        splitPopupNameLabel = Label(text="Enter Split Name", size_hint=(None, None), size=(150, 50), pos_hint={'center_x':.5, 'center_y':.8})

        splitNameBox.add_widget(splitPopupEnterButton)
        splitNameBox.add_widget(splitPopupTextInput)
        splitNameBox.add_widget(splitPopupNameLabel)
        splitNameBox.add_widget(closeSplitPopupButton)

        splitNamePopup = Popup(title='Creating New Split',content=splitNameBox, size_hint=(None, None), size=(300,250), auto_dismiss=False, background_color=(0.2,0.2,1,1))
        closeSplitPopupButton.bind(on_press=splitNamePopup.dismiss)
        splitPopupEnterButton.bind(on_press=lambda x:self.createSplit(splitPopupTextInput.text))
        splitPopupEnterButton.bind(on_press=splitNamePopup.dismiss)

        splitNamePopup.open()

    def createSplit(self, splitName):
        if not os.path.exists(f'C:\github\intro to programming\ITPFinalProject\Resources\Splits\{splitName}.txt') and self.splitCount < 5:
            splitNameFile = open(f'C:\github\intro to programming\ITPFinalProject\Resources\Splits\{splitName}.txt', 'w')
            self.add_widget(Button(text=f'{splitName}', pos_hint={'center_x':.5,'center_y':.1*self.splitCount*1.5}, size_hint=(None, None), size=(450, 80), font_size=25, background_color=(0.1,0.1,1,0.5)))
            splitNameFile.close()
            self.splitCount += 1
            lambda x:self.checkSplitFiles()
        


class OptionsScreen(Screen, FloatLayout):

    def __init__(self, **kwargs):
        super(OptionsScreen, self).__init__(**kwargs)
        self.optionsLogo = Image(source='C:\github\intro to programming\ITPFinalProject\Resources\Images\options_logo.png',pos_hint={'center_x':.5,'center_y':.8})
        self.add_widget(self.optionsLogo)

        self.backToMenuButton = Button(text='Back', size_hint=(.2,.1), pos_hint={'x':.05, 'y':.75}, background_color=(0.2,0.2,1,0.8))
        self.add_widget(self.backToMenuButton)
        self.backToMenuButton.bind(on_press=self.toStartScreen)

    def toStartScreen(self, instance):
        sm.current='start'
        return sm

      


class MySplit(App):

    def build(self):
        global sm
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(SplitsScreen(name='splits'))
        sm.add_widget(OptionsScreen(name='options'))


        sm.current='start'

        return sm

if __name__ == '__main__':
    MySplit().run()
    