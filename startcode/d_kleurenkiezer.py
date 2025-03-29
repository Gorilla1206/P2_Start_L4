import tkinter
window = tkinter.Tk()
window.title("kleuren kiezer")
window.geometry("300x200")
from tkinter import colorchooser
def verander_kleur():
    kleur = colorchooser.askcolor()[1]
    if kleur:
        button.config(bg=kleur)


# Knop aanmaken
button = tkinter.Button(window, text="verander kleur", command=verander_kleur)
button.pack()
window.mainloop()





