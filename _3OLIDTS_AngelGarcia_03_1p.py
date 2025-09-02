import tkinter as tk
from tkinter import messagebox

def Calcular_temps():
    # Contar cuántos campos tienen valor
    campos_llenos = sum(bool(entry.get()) for entry in [tbcelsius, tbFahrenheit, tbKelvin])

    if campos_llenos == 0:
        messagebox.showwarning(title="Advertencia", message="Ingrese un valor en uno de los campos.")
        return
    elif campos_llenos > 1:
        messagebox.showwarning(title="Advertencia", message="Ingrese el valor SOLO en un campo.")
        return

    try:
        if tbcelsius.get():
            Ce = float(tbcelsius.get())
            Fa = (Ce * 9/5) + 32
            Ke = Ce + 273.15
            tbFahrenheit.delete(0, tk.END)
            tbFahrenheit.insert(0, f"{Fa:.2f}")
            tbKelvin.delete(0, tk.END)
            tbKelvin.insert(0, f"{Ke:.2f}")

        elif tbFahrenheit.get():
            Fa = float(tbFahrenheit.get())
            Ce = (Fa - 32) * 5/9
            Ke = Ce + 273.15
            tbcelsius.delete(0, tk.END)
            tbcelsius.insert(0, f"{Ce:.2f}")
            tbKelvin.delete(0, tk.END)
            tbKelvin.insert(0, f"{Ke:.2f}")

        elif tbKelvin.get():
            Ke = float(tbKelvin.get())
            Ce = Ke - 273.15
            Fa = (Ce * 9/5) + 32
            tbcelsius.delete(0, tk.END)
            tbcelsius.insert(0, f"{Ce:.2f}")
            tbFahrenheit.delete(0, tk.END)
            tbFahrenheit.insert(0, f"{Fa:.2f}")

    except ValueError:
        messagebox.showerror(title="Error", message="Ingrese un valor numérico válido.")

def Limpiar():
    for entry in [tbcelsius, tbFahrenheit, tbKelvin]:
        entry.delete(0, tk.END)
    messagebox.showinfo(title="Limpiar", message="Se han borrado los valores.")

# Ventana principal
ventana = tk.Tk()
ventana.title("Conversor Básico de Temperatura")

# Labels
tk.Label(ventana, text="Celsius").grid(row=0, column=0, padx=10, pady=10)
tk.Label(ventana, text="Fahrenheit").grid(row=1, column=0, padx=10, pady=10)
tk.Label(ventana, text="Kelvin").grid(row=2, column=0, padx=10, pady=10)

# Entradas
tbcelsius = tk.Entry(ventana)
tbFahrenheit = tk.Entry(ventana)
tbKelvin = tk.Entry(ventana)
tbcelsius.grid(row=0, column=1, padx=10, pady=10)
tbFahrenheit.grid(row=1, column=1, padx=10, pady=10)
tbKelvin.grid(row=2, column=1, padx=10, pady=10)

# Botones
tk.Button(ventana, text="Calcular", command=Calcular_temps).grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(ventana, text="Limpiar", command=Limpiar).grid(row=4, column=0, padx=10, pady=10)
tk.Button(ventana, text="Salir", command=ventana.quit).grid(row=4, column=1, padx=10, pady=10)

ventana.mainloop()
