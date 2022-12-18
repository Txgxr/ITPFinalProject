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
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown

Builder.load_string("""
<EditIconButton>:
    canvas:
        Rectangle:
            source:self.editIcon
            pos: self.center_x-20, self.center_y-20
            size: 40,40

<TrashIconButton>:
    canvas:
        Rectangle:
            source:self.trashIcon
            pos: self.center_x-20, self.center_y-20
            size: 40,40

<SmallTrashIconButton>:
    canvas:
        Rectangle:
            source:self.trashIcon
            pos: self.center_x-12.5, self.center_y-12.5
            size: 25,25

<PlusIconButton>:
    canvas:
        Rectangle:
            source:self.plusIcon
            pos: self.center_x-15, self.center_y-15
            size: 30,30

<LoadIconButton>:
    canvas:
        Rectangle:
            source:self.loadIcon
            pos: self.center_x-15, self.center_y-15
            size: 30,30

<CheckIconButton>:
    canvas:
        Rectangle:
            source: self.checkIcon
            pos: self.center_x-12.5, self.center_y-12.5
            size: 25,25
""")

splitCount = 1
exCount = 0
prog_dir = os.path.dirname(__file__)
img_path = "Resources\Images\\"
split_path = "Resources\Splits\\"
img_file_path = os.path.join(prog_dir, img_path)
split_file_path = os.path.join(prog_dir, split_path)
print(img_file_path)

editSplitName = 'split'
exCount = 1

if not os.path.exists(split_file_path):
    os.umask(0)
    os.mkdir(split_file_path, 0o777)
    os.chmod(split_file_path, 0o777)

class EditIconButton(Button):
    editIcon = StringProperty(f'{img_file_path}pencil_icon.png')

class TrashIconButton(Button):
    trashIcon = StringProperty(f'{img_file_path}trash_icon.png')

class PlusIconButton(Button):
    plusIcon = StringProperty(f'{img_file_path}plus_icon.png')

class LoadIconButton(Button):
    loadIcon = StringProperty(f'{img_file_path}load_icon.png')

class CheckIconButton(Button):
    checkIcon = StringProperty(f'{img_file_path}check_icon.png')

class SmallTrashIconButton(Button):
    trashIcon = StringProperty(f'{img_file_path}trash_icon.png')

class StartScreen(Screen, FloatLayout):

    def __init__(self, **kwargs):
        
        super(StartScreen, self).__init__(**kwargs)
        # Create Splits Button
        self.splitsButton = Button(text="Splits", size_hint=(.2,.1), pos_hint={'center_x':.5, 'center_y':.5}, background_color=(0.294,0,1,0.509))
        self.add_widget(self.splitsButton)
        self.splitsButton.bind(on_release=self.toSplitsScreen)
        # Create Options Button
        self.optionsButton = Button(text='Options', size_hint=(.2,.1), pos_hint={'center_x':.5, 'center_y':.38}, background_color=(0.294,0,1,0.509))
        self.add_widget(self.optionsButton)
        self.optionsButton.bind(on_release=self.toOptionsScreen)
        # Create Exit Button
        self.exitButton = Button(text="Exit", size_hint=(.2,.1), pos_hint={'center_x':.5, 'center_y':.26}, background_color=(0.294,0,1,0.509))
        self.add_widget(self.exitButton)
        self.exitButton.bind(on_release=lambda x:self.exitPopup())
        # Create Logo
        self.logo = Image(source=f'{img_file_path}mySplit_Logo.png',pos_hint={'center_x':.5,'center_y':.8})
        self.add_widget(self.logo)

    def toSplitsScreen(self, instance):
        sm.current = "splits"
        print(splitCount)
        return sm

    def toOptionsScreen(self, instance):
        sm.current = "options"
        return sm

    def exitPopup(self):
        splitNameBox = FloatLayout()

        cancelExitButton = Button(text='Cancel', size_hint=(None, None), size=(90,60), pos_hint={'center_x':.25, 'center_y':.2})
        exitButton = Button(text='Exit', size_hint=(None, None), size=(90, 60), pos_hint={'center_x':.75, 'center_y':.2})
        exitConfirmLabel = Label(text="Are you sure you want to Exit?", size_hint=(None, None), size=(150, 50), pos_hint={'center_x':.5, 'center_y':.7})

        splitNameBox.add_widget(cancelExitButton)
        splitNameBox.add_widget(exitButton)
        splitNameBox.add_widget(exitConfirmLabel)

        exitConfirmPopup = Popup(title='Exit MySplit',content=splitNameBox, size_hint=(None, None), size=(300,250), auto_dismiss=False, background_color=(0.294,0,1,1))
        cancelExitButton.bind(on_release=exitConfirmPopup.dismiss)
        exitButton.bind(on_release=lambda x:MySplit().stop())

        exitConfirmPopup.open()







class SplitsScreen(Screen, FloatLayout):
    
    
    def __init__(self, **kwargs):
        global splitCount
        super(SplitsScreen, self).__init__(**kwargs)
        self.newSplitButton = Button(text='New Split', size_hint=(.2,.1), pos_hint={'x':.75, 'y':.75}, background_color=(0.294,0,1,0.509))
        self.add_widget(self.newSplitButton)
        self.newSplitButton.bind(on_release=self.splitNamePopup)

        self.backToMenuButton = Button(text='Back', size_hint=(.2,.1), pos_hint={'x':.05, 'y':.75}, background_color=(0.294,0,1,0.509))
        self.add_widget(self.backToMenuButton)
        self.backToMenuButton.bind(on_release=self.toStartScreen)

        self.logo = Image(source=f'{img_file_path}splits_logo.png',pos_hint={'center_x':.5,'center_y':.8})
        self.add_widget(self.logo)

    
        self.splitEntries = os.listdir('C:\github\intro to programming\ITPFinalProject\Resources\Splits')

        i=0 
        for split in self.splitEntries:
            self.generateSplits(os.path.splitext(self.splitEntries[i])[0])
            print(os.path.splitext(self.splitEntries[i])[0])
            i += 1

        # for split in self.splitEntries:
        #     splitButton = Button(text=f'{os.path.splitext(split)[0]}', pos_hint={'center_x':.5,'center_y':.75-(.1*(splitCount)*1.5)}, size_hint=(None, None), size=(450, 80), font_size=25, background_color=(0.294,0,1,0.509))
        #     editButton = EditIconButton(pos_hint={'center_x':.15, 'center_y':.75-(.1*(splitCount)*1.5)}, size_hint=(None, None), size=(80,80), background_color=(0.294,0,1,0.509))
        #     trashButton = TrashIconButton(pos_hint={'center_x':.85, 'center_y':.75-(.1*(splitCount)*1.5)}, size_hint=(None, None), size=(80,80), background_color=(0.294,0,1,0.509))

        #     self.add_widget(splitButton)
        #     self.add_widget(editButton)
        #     self.add_widget(trashButton)

        #     splitCount += 1

    def generateSplits(self, splitName):
        global splitCount
        if not os.path.exists(f'{split_file_path}{splitName}') and splitCount < 5:
            # splitNameFile = open(f'{split_file_path}{splitName}.txt', 'w')

            splitButton = Button(text=f'{splitName}', pos_hint={'center_x':.5,'center_y':.75-(.1*splitCount*1.5)}, size_hint=(None, None), size=(450, 80), font_size=25, background_color=(0.294,0,1,0.509))
            self.add_widget(splitButton)
            editIconButton = EditIconButton(pos_hint={'center_x':.15, 'center_y':.75-(.1*splitCount*1.5)}, size_hint=(None, None), size=(80,80), background_color=(0.294,0,1,0.509))
            self.add_widget(editIconButton)
            trashIconButton = TrashIconButton(pos_hint={'center_x':.85, 'center_y':.75-(.1*splitCount*1.5)}, size_hint=(None, None), size=(80,80), background_color=(0.294,0,1,0.509))
            self.add_widget(trashIconButton)

            trashIconButton.bind(on_release=lambda x:self.remove_widget(splitButton))
            trashIconButton.bind(on_release=lambda y:self.remove_widget(trashIconButton))
            trashIconButton.bind(on_release=lambda z:self.remove_widget(editIconButton))
            trashIconButton.bind(on_release=lambda a:self.minusSplitCount())
            trashIconButton.bind(on_release=lambda x:os.remove(f'{split_file_path}{splitName}.txt'))
            trashIconButton.bind(on_release=lambda b:print(splitCount))

            editIconButton.bind(on_release=lambda x:self.toEditScreen(splitName))


            # splitNameFile.close()
            splitCount += 1
    
    def toEditScreen(self, splitName):
        global editSplitName
        sm.current='edit'
        editSplitName = splitName   
        print(editSplitName)     

    def minusSplitCount(self):
        global splitCount
        splitCount -= 1


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

        splitNamePopup = Popup(title='Creating New Split',content=splitNameBox, size_hint=(None, None), size=(300,250), auto_dismiss=False, background_color=(0.294,0,1,1))
        closeSplitPopupButton.bind(on_release=splitNamePopup.dismiss)
        splitPopupEnterButton.bind(on_release=lambda x:self.createSplit(splitPopupTextInput.text))
        splitPopupEnterButton.bind(on_release=splitNamePopup.dismiss)

        splitNamePopup.open()
        

    # def editSplitPopup(self, splitName):
    #     global exCount
    #     editSplitBox = FloatLayout()
    #     exCount = 0
    #     exList = []
        
    #     with open(f"C:\github\intro to programming\ITPFinalProject\Resources\Splits\{splitName}.txt") as sN:
    #         exCount = len(sN.readlines())
    #     print(exCount)

    #     editSplitTextInput = TextInput(text='', size_hint=(None, None), size=(200,60), pos_hint={'center_x':.35, 'center_y':.55}, font_size=25, halign='left')
    #     cancelSplitEditButton = Button(text='Cancel', size_hint=(None, None), size=(90, 60), pos_hint={'center_x':.3, 'center_y':.1})
    #     saveSplitEditButton = Button(text='Save', size_hint=(None, None), size=(90, 60), pos_hint={'center_x':.7, 'center_y':.1})
    #     editSplitLabel = Label(text=f"Editing Split '{splitName}'", size_hint=(None, None), size=(150, 50), pos_hint={'center_x':.5, 'center_y':.9}, font_size=25)
    #     addExButton = plusIconButton(pos_hint={'center_x':.9, 'center_y':.9}, size_hint=(None,None), size=(50,50), background_color=(0.294,0,1,1))

    #     # editSplitBox.add_widget(editSplitTextInput)
    #     editSplitBox.add_widget(cancelSplitEditButton)
    #     editSplitBox.add_widget(saveSplitEditButton)
    #     editSplitBox.add_widget(editSplitLabel)
    #     editSplitBox.add_widget(addExButton)

    #     editSplitPopup = Popup(title='Edit Split', content=editSplitBox, size_hint=(None,None), size=(400,500), auto_dismiss=False, background_color=(0.294,0.1,1,1))
    #     cancelSplitEditButton.bind(on_release=editSplitPopup.dismiss)
    #     saveSplitEditButton.bind(on_release=editSplitPopup.dismiss)
    #     addExButton.bind(on_release=lambda x:editSplitBox.add_widget(TextInput(text='', size_hint=(None, None), size=(200,45), pos_hint={'center_x':.35, 'center_y':.9-(.1*exCount*1.25)}, font_size=25, halign='center', on_text_validate=)))
    #     addExButton.bind(on_release=lambda x:self.addExCount())


    #     editSplitPopup.open()
    #     return editSplitPopup
    
    def addExCount(self):
        global exCount
        exCount += 1
        print(exCount)



            

    def createSplit(self, splitName):
        global splitCount
        if not os.path.exists(f'{split_file_path}{splitName}.txt') and splitCount < 5:
            # Create a new file with the split name
            splitNameFile = open(f'{split_file_path}{splitName}.txt', 'w')

            # Add layout widgets
            splitButton = Button(text=f'{splitName}', pos_hint={'center_x':.5,'center_y':.75-(.1*splitCount*1.5)},
                                 size_hint=(None, None), size=(450, 80), font_size=25, background_color=(0.294,0,1,0.509))
            self.add_widget(splitButton)
            editIconButton = EditIconButton(pos_hint={'center_x':.15, 'center_y':.75-(.1*splitCount*1.5)}, 
                                            size_hint=(None, None), size=(80,80), background_color=(0.294,0,1,0.509))
            self.add_widget(editIconButton)
            trashIconButton = TrashIconButton(pos_hint={'center_x':.85, 'center_y':.75-(.1*splitCount*1.5)},
                                             size_hint=(None, None), size=(80,80), background_color=(0.294,0,1,0.509))
            self.add_widget(trashIconButton)

            # Bind Delete and Edit Buttons
            trashIconButton.bind(on_release=lambda x:self.remove_widget(splitButton))
            trashIconButton.bind(on_release=lambda y:self.remove_widget(trashIconButton))
            trashIconButton.bind(on_release=lambda z:self.remove_widget(editIconButton))
            trashIconButton.bind(on_release=lambda a:self.minusSplitCount())
            trashIconButton.bind(on_release=lambda x:os.remove(f'{split_file_path}{splitName}.txt'))
            trashIconButton.bind(on_release=lambda b:print(splitCount))

            editIconButton.bind(on_release=lambda x:self.toEditScreen(splitName))
        

            # Close split file
            splitNameFile.close()
            # Increase splitCount by 1
            splitCount += 1
                    


class OptionsScreen(Screen, FloatLayout):

    def __init__(self, **kwargs):
        super(OptionsScreen, self).__init__(**kwargs)
        self.optionsLogo = Image(source=f'{img_file_path}options_logo.png',
                                pos_hint={'center_x':.5,'center_y':.8})
        self.add_widget(self.optionsLogo)

        self.backToMenuButton = Button(text='Back', size_hint=(.2,.1), pos_hint={'x':.05, 'y':.75}, 
                                        background_color=(0.294,0,1,0.509))
        self.add_widget(self.backToMenuButton)
        self.backToMenuButton.bind(on_release=self.toStartScreen)

    def toStartScreen(self, instance):
        sm.current='start'
        return sm

class EditScreen(Screen, FloatLayout):

    def __init__(self, **kwargs):
        global editSplitName, exCount
        super(EditScreen, self).__init__(**kwargs)
        
        self.exLoaded = False

        self.editLogo = Image(source=f'{img_file_path}edit_logo.png', pos_hint={'center_x':.5, 'center_y':.9})
        self.add_widget(self.editLogo)

        self.cancelButton = Button(text='Cancel', size_hint=(.2,.1), pos_hint={'x':.05, 'center_y':.8}, background_color=(0.294,0,1,0.509))
        self.add_widget(self.cancelButton)
        self.cancelButton.bind(on_release=lambda x:self.toSplitsScreen())

        self.addExButton = PlusIconButton(pos_hint={'center_x':.85, 'center_y':.8}, size_hint=(None,None), size=(60,60), background_color=(0.294,0,1,0.509))
        self.add_widget(self.addExButton)
        self.addExButton.bind(on_release=lambda x:self.addEx())

        self.loadButton = LoadIconButton(pos_hint={'center_x':.75, 'center_y':.8}, size_hint=(None,None), size=(60,60), background_color=(0.294,0,1,0.509))
        self.add_widget(self.loadButton)
        self.loadButton.bind(on_release=lambda x: self.generateEx())

        
    
    def generateEx(self):
        global secondSplitName
        if self.exLoaded == False:
            self.editLabel = Label(text=f"Editing Split '{editSplitName}'", size_hint=(None,None), font_size=24, pos_hint={'center_x':.5, 'center_y':.8}, halign='center', color=(0.5,0.1,1,0.8))
            self.add_widget(self.editLabel)
            self.exLoaded = True

    def addEx(self):
        global exCount, split_file_path, editSplitName
        if exCount < 7:
            exCount += 1

            self.exNameTextInput = TextInput(size_hint=(None,None), size=(250,40), pos_hint={'center_x':.25, 'center_y':.85-(.1*exCount)}, font_size=22, multiline='false')
            self.add_widget(self.exNameTextInput)

            self.exSetsTextInput = TextInput(size_hint=(None,None), size=(40,40), pos_hint={'center_x':.5, 'center_y':.85-(.1*exCount)}, font_size=22, multiline='false')
            self.add_widget(self.exSetsTextInput)

            self.setsRepsTimesLabel = Label(text='x', font_size=30, pos_hint={'center_x':.55, 'center_y':.855-(.1*exCount)})
            self.add_widget(self.setsRepsTimesLabel)

            self.exRepsTextInput = TextInput(size_hint=(None,None), size=(40,40), pos_hint={'center_x':.6, 'center_y':.85-(.1*exCount)}, font_size=22, multiline='false')
            self.add_widget(self.exRepsTextInput)

            self.weightTextInput = TextInput(size_hint=(None,None), size=(60,40), pos_hint={'center_x':.72, 'center_y':.85-(.1*exCount)}, font_size=22, multiline='false')
            self.add_widget(self.weightTextInput)

            self.exLbsLabel = Label(text='lbs.', font_size=30, pos_hint={'center_x':.8, 'center_y':.85-(.1*exCount)})
            self.add_widget(self.exLbsLabel)

            self.saveExButton = CheckIconButton(size_hint=(None,None), size=(40,40), pos_hint={'center_x':.87, 'center_y':.85-(.1*exCount)}, background_color=(0.294,0,1,0.504))
            self.add_widget(self.saveExButton)

            self.delExButton = SmallTrashIconButton(size_hint=(None,None), size=(40,40), pos_hint={'center_x':.935, 'center_y':.85-(.1*exCount)}, background_color=(0.294,0,1,0.504))
            self.add_widget(self.delExButton)

            self.saveExButton.bind(on_release=lambda x:self.writeToFile(f'{self.exNameTextInput.text}:{self.exSetsTextInput.text}:{self.exRepsTextInput.text}:{self.weightTextInput.text}'))

            
    def writeToFile(self, text):
        splitFile = open(f'{split_file_path}{editSplitName}.txt', 'a+')
        splitData = splitFile.read()
        print(splitData + text)
        splitFile.write(splitData + text)
        splitFile.close()


    def toSplitsScreen(self):
        sm.current = 'splits'
        return sm
        

class MySplit(App):

    def build(self):
        global sm, editSplitName
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(SplitsScreen(name='splits'))
        sm.add_widget(OptionsScreen(name='options'))
        sm.add_widget(EditScreen(name='edit'))

        sm.current='start'

        return sm

if __name__ == '__main__':
    MySplit().run()

    