import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import time
from State import State

class EmulatorScreen:

    _main_frame: ttk.Frame = None
    _game_screen: ttk.Label = None
    _data_frame: ttk.Frame = None

    _current_screenshot: ImageTk.PhotoImage = None

    def __init__(self, window: ThemedTk):
        self._state = State()

        self._main_frame = ttk.Frame(window, relief="solid", borderwidth=2)
        self._main_frame.pack(padx=10, pady=10, fill='x')

        self._game_screen = ttk.Label(self._main_frame)
        self._game_screen.pack(side=tk.LEFT)

        self._data_frame = DataFrame(self._main_frame)

        

    def update_screen_and_data(self):
        self._game_screen.config(image=self._state._current_screenshot)

        self._data_frame._level.config(text=self._state.pokemon1_level)
        self._data_frame._hp.config(text=f"{self._state.pokemon1_current_hp} / {self._state.pokemon1_max_hp}")
        self._data_frame._attack.config(text=self._state.pokemon1_attack)
        self._data_frame._defense.config(text=self._state.pokemon1_defense)
        self._data_frame._speed.config(text=self._state.pokemon1_speed)
        self._data_frame._sp_attack.config(text=self._state.pokemon1_sp_attack)
        self._data_frame._sp_defense.config(text=self._state.pokemon1_sp_defense)



class DataFrame:
    _data_frame: ttk.Frame = None
    _level: ttk.Label = None
    _hp: ttk.Label = None
    _attack: ttk.Label = None
    _defense: ttk.Label = None
    _speed: ttk.Label = None
    _sp_attack: ttk.Label = None
    _sp_defense: ttk.Label = None


    def __init__(self, window: ThemedTk):
        self._data_frame = ttk.Frame(window)
        self._data_frame.pack(side=tk.LEFT, fill='both', expand=True)
        
        header = ttk.Label(self._data_frame, text='POKEMON DATA')
        header.pack()

        self.setup_level()
        self.setup_hp()
        self.setup_attack()
        self.setup_defense()
        self.setup_speed()
        self.setup_sp_attack()
        self.setup_sp_defense()

        

    def setup_level(self):
        level_frame = ttk.Frame(self._data_frame, relief="solid", borderwidth=2)
        level_label = ttk.Label(level_frame, text='Level')
        level_separator = ttk.Separator(level_frame, orient='vertical')
        self._level = ttk.Label(level_frame, text='0')
        level_frame.pack()
        level_label.pack(side=tk.LEFT)
        level_separator.pack(side=tk.LEFT, fill="y", padx=5, pady=5)
        self._level.pack(side=tk.LEFT)

    def setup_hp(self):
        hp_frame = ttk.Frame(self._data_frame, relief="solid", borderwidth=2)
        hp_label = ttk.Label(hp_frame, text='HP')
        hp_separator = ttk.Separator(hp_frame, orient='vertical')
        self._hp = ttk.Label(hp_frame, text='0 / 0')
        hp_frame.pack()
        hp_label.pack(side=tk.LEFT)
        hp_separator.pack(side=tk.LEFT, fill="y", padx=5, pady=5)
        self._hp.pack(side=tk.LEFT)

    def setup_attack(self):
        attack_frame = ttk.Frame(self._data_frame, relief="solid", borderwidth=2)
        attack_label = ttk.Label(attack_frame, text='Attack')
        attack_separator = ttk.Separator(attack_frame, orient='vertical')
        self._attack = ttk.Label(attack_frame, text='0')
        attack_frame.pack()
        attack_label.pack(side=tk.LEFT)
        attack_separator.pack(side=tk.LEFT, fill="y", padx=5, pady=5)
        self._attack.pack(side=tk.LEFT)

    def setup_defense(self):
        defense_frame = ttk.Frame(self._data_frame, relief="solid", borderwidth=2)
        defense_label = ttk.Label(defense_frame, text='Defense')
        defense_separator = ttk.Separator(defense_frame, orient='vertical')
        self._defense = ttk.Label(defense_frame, text='0')
        defense_frame.pack()
        defense_label.pack(side=tk.LEFT)
        defense_separator.pack(side=tk.LEFT, fill="y", padx=5, pady=5)
        self._defense.pack(side=tk.LEFT)

    def setup_speed(self):
        speed_frame = ttk.Frame(self._data_frame, relief="solid", borderwidth=2)
        speed_label = ttk.Label(speed_frame, text='Speed')
        speed_separator = ttk.Separator(speed_frame, orient='vertical')
        self._speed = ttk.Label(speed_frame, text='0')
        speed_frame.pack()
        speed_label.pack(side=tk.LEFT)
        speed_separator.pack(side=tk.LEFT, fill="y", padx=5, pady=5)
        self._speed.pack(side=tk.LEFT)
    
    def setup_sp_attack(self):
        sp_attack_frame = ttk.Frame(self._data_frame, relief="solid", borderwidth=2)
        sp_attack_label = ttk.Label(sp_attack_frame, text='SP Attack')
        sp_attack_separator = ttk.Separator(sp_attack_frame, orient='vertical')
        self._sp_attack = ttk.Label(sp_attack_frame, text='0')
        sp_attack_frame.pack()
        sp_attack_label.pack(side=tk.LEFT)
        sp_attack_separator.pack(side=tk.LEFT, fill="y", padx=5, pady=5)
        self._sp_attack.pack(side=tk.LEFT)

    def setup_sp_defense(self):
        sp_defense_frame = ttk.Frame(self._data_frame, relief="solid", borderwidth=2)
        sp_defense_label = ttk.Label(sp_defense_frame, text='SP Defense')
        sp_defense_separator = ttk.Separator(sp_defense_frame, orient='vertical')
        self._sp_defense = ttk.Label(sp_defense_frame, text='0')
        sp_defense_frame.pack()
        sp_defense_label.pack(side=tk.LEFT)
        sp_defense_separator.pack(side=tk.LEFT, fill="y", padx=5, pady=5)
        self._sp_defense.pack(side=tk.LEFT)
