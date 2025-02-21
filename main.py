import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from LibmgbaEmulator import LibmgbaEmulator
from Emulator import Emulator
import mgba.audio
import mgba.core
import mgba.gba
import mgba.image
import mgba.log
import mgba.png
import mgba.vfs
from PIL import Image, ImageTk
import time
from GUI import GUI
from State import State

#init the emulator
emulator = Emulator()
#init state
state = State()
state.set_emulator(emulator)
#init the gui
gui = GUI()

#run the tkinter main loop
gui._root.mainloop()
