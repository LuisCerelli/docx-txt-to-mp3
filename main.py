import tkinter as tk
from tkinter import filedialog, messagebox
from gtts import gTTS
from docx import Document
import threading

# Leer archivos .txt y .docx
def leer_archivo(path):
    if path.endswith('.txt'):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    elif path.endswith('.docx'):
        doc = Document(path)
        return '\n'.join(p.text for p in doc.paragraphs)
    else:
        raise ValueError("Formato no soportado")

# Conversión a audio
def texto_a_audio():
    path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt *.docx")])
    if not path:
        return

    try:
        texto = leer_archivo(path)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo leer el archivo:\n{e}")
        return

    out = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("Audio", "*.mp3")])
    if not out:
        return

    # Cambiar texto del botón y desactivar
    btn.config(text="⏳ Generando audio...", state="disabled")
    root.update_idletasks()

    def convertir():
        try:
            tts = gTTS(text=texto, lang='en')
            tts.save(out)
            messagebox.showinfo("Listo", f"✅ Archivo generado:\n{out}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el audio:\n{e}")
        finally:
            btn.config(text="Seleccionar archivo de texto", state="normal")

    threading.Thread(target=convertir).start()

# Interfaz gráfica
root = tk.Tk()
root.title("Texto a Audio")
btn = tk.Button(root, text="Seleccionar archivo de texto", command=texto_a_audio, height=2, width=40)
btn.pack(padx=20, pady=30)
root.mainloop()
