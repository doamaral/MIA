__author__ = 'Lucas'

from cx_Freeze import setup, Executable

setup(name = "Lucas Amaral", version = "1.0", description = "Py to EXE", executables = [Executable("main.py")])