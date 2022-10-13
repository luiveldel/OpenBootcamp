"""
En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener
una lista de elementos seleccionables, también debe de tener
un label con el texto que queráis.
"""

import tkinter

window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

label = tkinter.Label(window, text='Elige a tu amigo!')
label.pack()

pokemon_list = ['Bulbasur', 'Charmander', 'Squirtel']
pokemon_items = tkinter.StringVar(value=pokemon_list)
list_box = tkinter.Listbox(window, height=3, listvariable=pokemon_items)
list_box.pack()

window.mainloop()
