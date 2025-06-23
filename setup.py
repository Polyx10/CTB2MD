"""
Script de configuration pour py2app
"""
from setuptools import setup

APP = ['ctb2md.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'CFBundleName': 'CTB2MD',
        'CFBundleDisplayName': 'CTB2MD',
        'CFBundleIdentifier': 'com.polyx10.ctb2md',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'LSMinimumSystemVersion': '10.15',
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
