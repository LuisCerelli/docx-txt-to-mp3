from setuptools import setup

APP = ['main.py']
OPTIONS = {
    'includes': ['tkinter'],
    'packages': ['gtts', 'docx'],
    'iconfile': 'Logo.icns'
}

setup(
    app=APP,
    name='Conversor Texto-Audio',
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)