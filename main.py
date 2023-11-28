# Project:      Lab3
# Author:       Nicole Ruiz-Bueno
# Date:         02/01/2023
# File:         main.py
# Description:  This lab is an introduction to input using Kivy text input,
#               Python variables and operators
# Input:        This program has 2 numerical inputs, 'Rate' and 'Hours'
# Output:       Display the product of the 2 numbers using a Calculate button.
# Processing:   The Calculate Button releases the event function.
#               Declare input variables Pay Rate and Hours Worked to hold integer input from the text input boxes.
#               Cast both Rate and Hours as a float.
#               If: ‘Hours’ > 40,
#               Gross Pay = ((rate * 1.5) * (hours - 40)) + (rate * 40)
#               Else: Gross Pay = Pay Rate * Hours Worked
#               Convert result to string and format 2 decimal places.
#               Display in the Gross Pay label.
#
#               The Exit button releases the event function.
#               Stop the application.

# import the Kivy library components
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget

# designate our .kv design file
# we are using gui.kv for the Graphical user Interface
Builder.load_file('gui.kv')


# A Widget is the base building block of GUI interfaces in Kivy.
# It provides a Canvas that can be used to draw on screen.
# It receives user events and reacts to them.
# MyLayout is the root window of the application
class MyLayout(Widget):
    pass


# Lab3 is the name of the Python application that will be using Kivy
class Lab3(App):
    # set the title of the window frame
    title = 'Lab 3 by Ruiz-Bueno'

    # the build method is called when the application starts
    def build(self):
        print("build called")
        # when app starts, return main root window in the kivy gui file
        return MyLayout()

    # calculate button release event handler
    # this function is called by the Kivy event loop when a user presses the Add button
    def calculate_button(self):
        # get data from text inputs
        # self means this or the current object
        # root is the root window or MyLayout
        # ids is the id's of the widgets contained in the root window
        # payRate is the id of the payRate text input box
        # hoursWorked is the id of the hoursWorked text input box
        # print the input for debugging
        print(f'calculate_button payRate: {self.root.ids.rate.text}, hoursWorked: {self.root.ids.hours.text}')

        # declare float variables rate and hours
        # use float since either can contain a decimal point
        # get both input strings from textInputs and cast to float variables
        rate = float(self.root.ids.rate.text)
        hours = float(self.root.ids.hours.text)

        # multiply the rate * hours together and assign the result to the variable grossPay
        if hours > 40:
            grossPay = ((rate * 1.5) * (hours - 40)) + (rate * 40)
        else:
            grossPay = rate * hours

        # convert grossPay to string and display in the grossPay label's text property
        self.root.ids.grossPay.text = str(grossPay)
        # format grossPay to string with 2 decimal places and display in Label's text
        # self.root.ids.grossPay.text = '${:.2f}'.format(grossPay)
        self.root.ids.grossPay.text = f'${grossPay:.2f}'

    # exit button release event handler
    # this function is called by the Kivy event loop when a user presses the Multiply button
    def exit_button(self):
        # call the stop function in the app
        self.stop()


# If this Python file is called as the main starting point of the application
# start the Python/Kivy app running.
if __name__ == '__main__':
    Lab3().run()
