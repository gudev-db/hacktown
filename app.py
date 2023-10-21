import tkinter as tk
from funcs import load_pto_tur2_data, preprocess_pto_tur2, pto_tur2_histogram_avaliacoes
window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()



load_pto_tur2_data()
preprocess_pto_tur2()
pto_tur2_histogram_avaliacoes()
window.mainloop()