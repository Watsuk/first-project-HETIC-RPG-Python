from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


class Menu_screen(Screen):
    pass


class Info_screen(Screen):
    '''def showtext(self):
        with open("test.txt","r") as f:
            return(f.read())'''
    pass


class Game_screen(Screen):
    pass


class Manager(ScreenManager):
    pass


kv = Builder.load_file('kivy.kv')


class Menu(App):
    def build(self):
        return kv


if __name__ == '__main__':
    Menu().run()

