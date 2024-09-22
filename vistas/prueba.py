import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    email = entry_email.get()

    if not name or not age or not email:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return

    try:
        age = int(age)
    except ValueError:
        messagebox.showerror("Error", "La edad debe ser un número")
        return

    generate_pdf(name, age, email)
    messagebox.showinfo("Éxito", "PDF generado con éxito")

def generate_pdf(name, age, email):
    pdf_file = "reporte_formulario.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter

    c.drawString(100, height - 100, f"Nombre: {name}")
    c.drawString(100, height - 120, f"Edad: {age}")
    c.drawString(100, height - 140, f"Email: {email}")

    c.save()

app = tk.Tk()
app.title("Formulario")

tk.Label(app, text="Nombre").grid(row=0)
tk.Label(app, text="Edad").grid(row=1)
tk.Label(app, text="Email").grid(row=2)

entry_name = tk.Entry(app)
entry_age = tk.Entry(app)
entry_email = tk.Entry(app)

entry_name.grid(row=0, column=1)
entry_age.grid(row=1, column=1)
entry_email.grid(row=2, column=1)

tk.Button(app, text="Enviar", command=submit_form).grid(row=3, column=1, pady=4)

app.mainloop()
