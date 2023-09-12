import tkinter as tk
import re

def click(key):
    if key == "=":
        try:
            # Obtener la expresión desde la variable de control, reemplazar "^" por "**" y evaluarla
            expression = entry_var.get().replace("^", "**")
            # Eliminar ceros a la izquierda de los números utilizando expresiones regulares
            expression = re.sub(r'\b0+(\d+)', r'\1', expression)
            result = str(eval(expression))
            entry_var.set(result)  # Actualizar el resultado en la Entry
            memory_label.config(text=expression + " =", anchor="e")  # Mostrar la memoria con la expresión evaluada y justificar a la derecha
        except:
            entry_var.set("Error")  # En caso de error, mostrar "Error"
            memory_label.config(text="", anchor="e")  # Borrar la memoria en caso de error
    elif key == "C":
        entry_var.set("")  # Borrar la entrada actual
    else:
        current_text = entry_var.get()
        entry_var.set(current_text + key)  # Agregar el carácter al final de la entrada

root = tk.Tk()
root.title("Calculadora")

# Configurar una variable de control para la Entry
entry_var = tk.StringVar()

# Configurar la Entry para que no tenga bordes, no admita entrada de teclado y sea de solo lectura
entry = tk.Entry(root, textvariable=entry_var, font=("Helvetica", 16), borderwidth=0, readonlybackground='white', state="readonly", justify="right")
entry.grid(row=1, column=0, columnspan=4, sticky="nsew")

# Configurar un Label para mostrar la memoria con justificación a la derecha
memory_label = tk.Label(root, text="", font=("Helvetica", 10), anchor="e")
memory_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C", "^"
]

row = 2
col = 0

# Crear y colocar los botones en la ventana
for button in buttons:
    tk.Button(root, text=button, font=("Helvetica", 12), padx=20, pady=20, command=lambda b=button: click(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()  # Iniciar el bucle principal de la interfaz gráfica
