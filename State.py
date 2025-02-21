from Emulator import Emulator
from PIL import ImageTk

class State:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    # Initialize default values for the state
    def _initialize(self):
        self.pokemon1_current_hp = 0
        self.pokemon1_max_hp = 0
        self.pokemon1_level = 0
        self.pokemon1_attack = 0
        self.pokemon1_defense = 0
        self.pokemon1_speed = 0
        self.pokemon1_sp_attack = 0
        self.pokemon1_sp_defense = 0

        self._current_screenshot: ImageTk.PhotoImage = None

        pass

    def set_emulator(self, emulator: Emulator):
        self._emulator = emulator
    
    def update_state(self):
        self._current_screenshot = ImageTk.PhotoImage(self._emulator.get_current_screen_image())

        self.pokemon1_level = self._emulator.read_bytes(0x020242D8, 1)[0]
        self.pokemon1_current_hp = self._emulator.read_bytes(0x020242DA, 1)[0]
        self.pokemon1_max_hp = self._emulator.read_bytes(0x020242DC, 1)[0]
        self.pokemon1_attack = self._emulator.read_bytes(0x020242DE, 1)[0]
        self.pokemon1_defense = self._emulator.read_bytes(0x020242E0, 1)[0]
        self.pokemon1_speed = self._emulator.read_bytes(0x020242E2, 1)[0]
        self.pokemon1_sp_attack = self._emulator.read_bytes(0x020242E4, 1)[0]
        self.pokemon1_sp_defense = self._emulator.read_bytes(0x020242E6, 1)[0]
        

#party pokemon 1 02024284
#enemy pokemon 1 0202402C
