from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager


class MyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        line = BoxLayout(orientation='vertical')
        line1 = BoxLayout(orientation='horizontal')
        line2 = BoxLayout(orientation='horizontal')
        hello = Label(text='Heello world')
        line.add_widget(hello)



        kno = Button(text="1")
        line.add_widget(kno)
        self.add_widget(line)


class SecondWibd(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        line = BoxLayout(orientation='vertical')

        kno = Button(text="SecondWibd", on_press=self.second())
        line.add_widget(kno)
        self.add_widget(line)

    def second(self, *args):
        self.manager.current = 'second'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MyScreen(name='main'))
        sm.add_widget(SecondWibd(name='second'))

        return sm