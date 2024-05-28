from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivy.core.window import Window
Window.size = (310, 580)

class LoginScreen(Screen):
    pass

class PrincipalScreen(Screen):
    pass

class CookieScreen(Screen):
    pass

class BrownieScreen(Screen):
    pass

class BolopoteScreen(Screen):
    pass

class App(MDApp):
     def build(self):
        Builder.load_file('teste.kv')
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(PrincipalScreen(name='principal'))
        sm.add_widget(CookieScreen(name='cookie'))
        sm.add_widget(BrownieScreen(name='brownie'))
        sm.add_widget(BolopoteScreen(name='bolopote'))
        return sm


if __name__ == '__main__':
    App().run()