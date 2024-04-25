import os
import sys

def restart_software():
    python = sys.executable
    os.execl(python, python, * sys.argv)
