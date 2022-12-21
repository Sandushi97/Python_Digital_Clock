# Importing the relevant libraries
from tkinter import Label, Tk
import datetime
import time
# Defining the size and the title of the application
app_window = Tk()
app_window.title('Digital Clock')
app_window.geometry("1090x400")
app_window.resizable(1, 1)
#app_window.eval('tk::PlaceWindow . center')

# font of the window and its color
text_font = ("Times New Roman", 68, "italic bold")
background = "black"
foreground = "red"
border_width = 100

# combining all the elements to defining the label of the clock application
label = Label(app_window, font=text_font, bg=background,
              fg=foreground, bd=border_width)
label.grid(row=0, column=1)


def digital_clock():
    time_live = datetime.datetime.now().strftime("%A:%d-%b-%Y \n %H:%M:%S %p")
    label.config(text=time_live)
    label.after(200, digital_clock)


digital_clock()
app_window.mainloop()
