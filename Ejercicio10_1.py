"""
En este ejercicio tenéis que crear una lista de RadioButton
que muestre la opción que se ha seleccionado
y que contenga un botón de reinicio para que deje todo como al principio.
Al principio no tiene que haber una opción seleccionada.

"""
import sys
import tkinter
from tkinter import ttk  # Ttk aplica cierto estilo

window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)


def pop_window():
    window = tkinter.Tk()

    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)

    selected = tkinter.StringVar()
    r1 = ttk.Radiobutton(window, text='Yes', value='1', variable=selected)
    r2 = ttk.Radiobutton(window, text='No', value='2', variable=selected)
    r3 = ttk.Radiobutton(window, text='Maybe', value='3', variable=selected)

    r1.grid(column=0, row=1, pady=5, padx=5)
    r2.grid(column=0, row=2, pady=5, padx=5)
    r3.grid(column=0, row=3, pady=5, padx=5)

    button = tkinter.Button(window, text='Reboot')
    button.grid(column=1, row=4, sticky=tkinter.E, padx=5, pady=5)
    button.bind('<Button-1>', reboot)


def reboot(event):
    window.destroy()
    pop_window()

def election():
    reboot()
    pop_window()


selected = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text='Yes', value='1', variable=selected, command=election)
r2 = ttk.Radiobutton(window, text='No', value='2', variable=selected, command=election)
r3 = ttk.Radiobutton(window, text='Maybe', value='3', variable=selected, command=election)

# Positioning
r1.grid(column=0, row=1, pady=5, padx=5)
r2.grid(column=0, row=2, pady=5, padx=5)
r3.grid(column=0, row=3, pady=5, padx=5)

# Button
button = tkinter.Button(window, text='Reboot')
button.grid(column=1, row=4, sticky=tkinter.E, padx=5, pady=5)
button.bind('<Button-1>', reboot)

window.mainloop()
