from Emulator import Emulator
from PIL import ImageTk
from Pokemon import Pokemon
# from helpers import load_pokemon_library

class State:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(State, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, emulator: Emulator = None):
        if not self._initialized:
            self._emulator = emulator

            self._pokemon_1 = Pokemon(self._emulator, 0x02024284)
            self._pokemon_2 = Pokemon(self._emulator, 0x020242E8)
            self._pokemon_3 = Pokemon(self._emulator, 0x0202434C)
            self._enemy_pokemon = Pokemon(self._emulator, 0x0202402C)
            self._current_screenshot: ImageTk.PhotoImage = None

            self._initialized = True


    def set_emulator(self, emulator: Emulator):
        self._emulator = emulator
    
    def update_state(self):
        self._current_screenshot = ImageTk.PhotoImage(self._emulator.get_current_screen_image())

        self._pokemon_1.update()
        self._pokemon_2.update()
        self._pokemon_3.update()
        self._enemy_pokemon.update()
        # print(f"1: {self._pokemon_1._pokedex_number} - 2: {self._pokemon_2._pokedex_number} - 3: {self._pokemon_3._pokedex_number}")
        print(f"1: {self._pokemon_1._name} - 2: {self._pokemon_2._name} - 3: {self._pokemon_3._name} - 4: {self._enemy_pokemon._name}")
        # print(self._enemy_pokemon.__dict__)
        # print(self._enemy_pokemon._pokedex_number)
        # print(f"mine: {self._pokemon_1._decrypted_data}")
        # print(f"enemy: {self._enemy_pokemon._decrypted_data}")
        

#party pokemon 1 02024284
#enemy pokemon 1 0202402C
