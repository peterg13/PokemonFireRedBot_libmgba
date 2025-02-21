import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import time
from Emulator import Emulator
from EmulatorScreen import EmulatorScreen
from State import State


class GUI:

    _root: ThemedTk = None
    _speed_control_frame: ttk.Frame = None
    _emulator_screen: EmulatorScreen = None
    _pokemon_frame: ttk.Frame = None
    _control_frame: ttk.Frame = None

    _tester_label: ttk.Label = None

    def __init__(self):
        self._state = State()
        self._root = ThemedTk(className="PokeBot", theme="equilux")
        self._root.geometry("1080x800");
        style = ttk.Style()
        self._root.configure(bg=style.lookup("TFrame", "background"))

        self._emulator_screen = EmulatorScreen(self._root)
        self.setup_control_frame()

        self._root.mainloop = self.mainLoop
    
    def mainLoop(self):
        while(True):
            self._state._emulator.run_frame()
            self._state.update_state()
            self._emulator_screen.update_screen_and_data()
            
            self._root.update()
            time.sleep(self._state._emulator.emulation_speed)

    
    def setup_control_frame(self):
        self._control_frame = ttk.Frame(self._root, relief="solid", borderwidth=2)
        self._control_frame.pack(padx=10, pady=10, fill='both')

        #left half: manual controls
        self._manual_control_frame = ttk.Frame(self._control_frame, relief="solid", borderwidth=2)
        self._manual_control_frame.pack(side=tk.LEFT, fill='both')
        directional_control_frame = ttk.Frame(self._manual_control_frame)
        directional_control_frame.pack()
        up = ttk.Button(directional_control_frame, text='up', command=lambda: self._state._emulator.press_button("Up"))
        up.pack(side=tk.TOP)
        down = ttk.Button(directional_control_frame, text='down', command=lambda: self._state._emulator.press_button("Down"))
        down.pack(side=tk.BOTTOM)
        left = ttk.Button(directional_control_frame, text='left', command=lambda: self._state._emulator.press_button("Left"))
        left.pack(side=tk.LEFT)
        right = ttk.Button(directional_control_frame, text='right', command=lambda: self._state._emulator.press_button("Right"))
        right.pack(side=tk.RIGHT)
        a_b_button_frame = ttk.Frame(self._manual_control_frame)
        a_b_button_frame.pack()
        a = ttk.Button(a_b_button_frame, text='a', command=lambda: self._state._emulator.press_button("A"))
        a.pack(side=tk.RIGHT)
        b = ttk.Button(a_b_button_frame, text='b', command=lambda: self._state._emulator.press_button("B"))
        b.pack(side=tk.LEFT)

        #right half: speed controls
        self._speed_control_frame = ttk.Frame(self._control_frame, relief="solid", borderwidth=2)
        self._speed_control_frame.pack(side=tk.LEFT, fill='x')

        speed1xButton = ttk.Button(self._speed_control_frame, text="1x", command=lambda: self._state._emulator.set_emulation_speed(1))
        speed1xButton.pack(side=tk.LEFT, padx=5)

        speed2xButton = ttk.Button(self._speed_control_frame, text="2x", command=lambda: self._state._emulator.set_emulation_speed(2))
        speed2xButton.pack(side=tk.LEFT, padx=5)

        speed5xButton = ttk.Button(self._speed_control_frame, text="5x", command=lambda: self._state._emulator.set_emulation_speed(5))
        speed5xButton.pack(side=tk.LEFT, padx=5)
           