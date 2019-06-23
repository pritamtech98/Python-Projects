from cx_Freeze import setup, Executable
import sys

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(name = "tic-tac-toe", version = "0.1", description ="First tic-tac-toe", executables = [Executable("de.py", base=base)])
