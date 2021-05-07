# A program  to create a calculator with kivy
import kivy

# use  tis kivy version
from kivy.app import App

kivy.require ('1.9.0')

# to make multiple buttons to arranging

from kivy.uix.gridlayout import GridLayout

# for the size of window
from kivy.config import Config

# Setting size to resizable
Config.set ('graphics', 'resizable', 1)


# Creating Layout class
class CalcGridLayout (GridLayout):

    # Function called when equals is pressed
    def calculate(self, calculation):
        if calculation:
            try:

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
