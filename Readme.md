# 🎙️ Conversor Texto → Audio (.txt/.docx a .mp3)
<img src="imagenes/Logo.webp" alt="LogoApp" width="600"/>

Convierte archivos de texto planos o Word directamente en archivos de audio `.mp3` usando una interfaz amigable y moderna con Google Text-to-Speech (gTTS).

---

## 📦 ¿Qué hace esta app?

✅ Abre archivos `.txt` o `.docx`  
✅ Convierte el texto a audio con voz en inglés  
✅ Guarda el resultado como archivo `.mp3`  
✅ No necesitas cerrar la app para que funcione 😉  
✅ Te muestra el progreso y confirma al terminar  

---

## 🚀 ¿Cómo usarla?

### 1. Cloná o descargá el proyecto

```bash
git clone https://github.com/tuusuario/conversor_audio.git
cd conversor_audio
```

### 2. Crear y activar entorno virtual (recomendado para Python 3.10, al cual podes descargar usando pyenv)

```bash
pyenv install 3.10.13
pyenv local 3.10.13
python -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la app desde Terminal

```bash
python main.py
```

---

## 🍎 ¿Querés una app `.app` para macOS?

1. Asegurate de tener `pyenv` y Python 3.10.13
2. Activá el entorno y empaquetá:

```bash
python setup.py py2app
```

3. Abrí la app desde el ```Finder```
4. O desde la terminal:
```
dist/Conversor Texto-Audio.app
```

---

## 💻 Compatibilidad multiplataforma

✅ **macOS** — ejecución directa o como `.app` con `py2app`  
✅ **Windows** — ejecutable con `pyinstaller` o `python main.py`  
✅ **Linux** — funciona directamente desde terminal con Python 3.10+  

🎯 Solo el empaquetado `.app` es exclusivo de macOS. Todo lo demás funciona igual en cualquier sistema operativo.

---

## 🧠 ¿Cómo funciona?

Usamos `gTTS`, que conecta con Google Text-to-Speech para generar el audio.  
El resultado se guarda como `.mp3` al instante.  
El botón principal cambia durante el proceso, y no bloquea la ventana.

---

## 📄 Requisitos

- Python 3.10+ recomendado
- Acceso a Internet (para gTTS)
- macOS con `py2app` si querés exportar como `.app`

---

## 💬 ¿Preguntas o mejoras?

Abrí un issue o escribime. ¡Siempre hay margen para mejorar! 🙌
