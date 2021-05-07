# Program to create a calculator

# Program to Show how to create a switch
# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require ('1.9.0')

# for making multiple bttons to arranging
# them we are using this
from kivy.uix.gridlayout import GridLayout

# for the size of window
from kivy.config import Config

# Setting size to resizable
Config.set ('graphics', 'resizable', 1)


## Config.set('graphics', 'width', '400')
## Config.set('graphics', 'height', '400')


# Creating Layout class
class CalcGridLayout (GridLayout):

    # Function called when equals is pressed
    def calculate(self, calculation):
        if calculation:
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                self.display.text = str (eval (calculation))
            except Exception:
                self.display.text = "Error"


# Creating App class
class CalculatorApp (App):

    def build(self):
        return CalcGridLayout ()


# creating object and running it
calcApp = CalculatorApp ()
calcApp.run ()
