import tkinter as tk
from tkinter import ttk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        
        # Pantalla de resultados
        self.pantalla = tk.Entry(master, width=30, justify="right")
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # Botones
        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row = 1
        col = 0
        for boton in botones:
            comando = lambda x=boton: self.click(x)
            ttk.Button(master, text=boton, command=comando).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Botón de limpiar
        ttk.Button(master, text="C", command=self.limpiar).grid(row=row, column=col, padx=5, pady=5)
    
    def click(self, key):
        if key == '=':
            try:
                resultado = eval(self.pantalla.get())
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, str(resultado))
            except:
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, "Error")
        else:
            self.pantalla.insert(tk.END, key)
    
    def limpiar(self):
        self.pantalla.delete(0, tk.END)

root = tk.Tk()
calculadora = Calculadora(root)
root.mainloop()
