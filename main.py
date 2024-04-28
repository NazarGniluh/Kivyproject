

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label





class MyApp(App):
    def build(self):
        line = BoxLayout(orientation='vertical')
        hello = Label(text='Heello world')
        line.add_widget(hello)

        hello2 = Label(text='Heello from in Ukraaine')
        line.add_widget(hello2)

        kno = Button()
        line.add_widget(kno)
        return line

MyApp().run()
