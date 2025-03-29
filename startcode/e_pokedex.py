import tkinter
window = tkinter.Tk()
window.title("pokédex")
window.geometry("300x200")
tkinter.Entry(window)







# Knop aanmaken
button = tkinter.Button(window, text="haal pokedex info op", command=haal_pokedex_info_op)
button.pack()














window.mainloop()