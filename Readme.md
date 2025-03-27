

# 🎙️ Conversor Texto → Audio (.txt/.docx a .mp3)
<img src="imagenes/Logo.webp" alt="LogoApp" width="600"/>

Convierte archivos de texto planos(txt) o Word escritos en inglés (para practicar y aprender) directamente en archivos de audio `.mp3` usando una interfaz amigable y moderna con Google Text-to-Speech (gTTS).

---

## ☁️ ¿Y si quiero llevarlo a Azure?

También podés usar esta app en la nube con **Azure**, adaptándola según tu necesidad:

### 1. Web App (Azure App Service)
- ✅ Versión web accesible desde navegador
- 💻 Requiere convertir el código a Flask o FastAPI
- 💸 Gratis en plan F1, desde **€12/mes** en plan B1
- 🌍 Ideal si querés compartir el conversor online

### 2. API serverless (Azure Functions)
- ✅ Código como función que procesa y devuelve `.mp3`
- ⚙️ Ideal para integrarlo en apps web o móviles
- 💸 1M ejecuciones gratis/mes, luego €0.20/100k
- ❌ No tiene interfaz visual

### 3. Contenedor (Azure Container Apps)
- ✅ Corrés la app como está, dentro de un contenedor Docker
- 💪 Máxima compatibilidad y control
- 💸 Gratis hasta cierto uso, luego desde €4–8/mes
- 🔧 Requiere saber Docker básico

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

### 2. Crear y activar entorno virtual (recomendado para Python 3.10, al cual podés descargar usando pyenv)

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
