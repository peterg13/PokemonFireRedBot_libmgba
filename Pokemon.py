from Emulator import Emulator
from helpers import int_from_bytes
from pokemon_library import get_pokedex_entry

SUBSTRUCTURE_ORDER = ['GAEM', 'GAME', 'GEAM', 'GEMA', 'GMAE', 'GMEA', 'AGEM', 'AGME', 'AEGM', 'AEMG', 'AMGE', 'AMEG', 'EGAM', 'EGMA', 'EAGM', 'EAMG', 'EMGA', 'EMAG', 'MGAE', 'MGEA', 'MAGE', 'MAEG', 'MEGA', 'MEAG']

class Pokemon:

    _address: int = 0
    _decrypted_data: bytes = None

    _personality_value: int = ''
    _original_trainer_id: int = ''
    _key: int = ''
    _G: int = 0
    _A: int = 0
    _E: int = 0
    _M: int = 0

    _pokedex_number: int = 0
    _name: str = ''
    _type_1: str = ''
    _type_2: str | None = None
    
    _level: int = 0
    _experience: int = 0
    _current_hp: int = 0
    _max_hp: int = 0
    _attack: int = 0
    _defense: int = 0
    _speed: int = 0
    _sp_attack: int = 0
    _sp_defense: int = 0

    

    def __init__(self, emulator: Emulator, address: int):
        self._emulator = emulator
        self._address = address

        self.update()


    def update(self):
        self._personality_value = int_from_bytes(self._emulator.read_bytes(self._address, 4)) & 0xFFFFFFFF
        self._original_trainer_id = int_from_bytes(self._emulator.read_bytes(self._address + 0x04, 4)) & 0xFFFFFFFF
        self._key = (self._personality_value ^ self._original_trainer_id) & 0xFFFFFFFF

        pkmn_sub_order = SUBSTRUCTURE_ORDER[self._personality_value % 24]
        self._G = pkmn_sub_order.index('G') * 12
        self._A = pkmn_sub_order.index('A') * 12
        self._E = pkmn_sub_order.index('E') * 12
        self._M = pkmn_sub_order.index('M') * 12


        self.decrypt_data(self._emulator.read_bytes(self._address + 0x20, 48))
        self.get_growth_data()

        self._level = self._emulator.read_bytes(self._address + 0x54, 1)[0]
        self._current_hp = int_from_bytes(self._emulator.read_bytes(self._address + 0x56, 2))
        self._max_hp = int_from_bytes(self._emulator.read_bytes(self._address + 0x58, 2))
        self._attack = int_from_bytes(self._emulator.read_bytes(self._address + 0x5A, 2))
        self._defense = int_from_bytes(self._emulator.read_bytes(self._address + 0x5C, 2))
        self._speed = int_from_bytes(self._emulator.read_bytes(self._address + 0x5E, 2))
        self._sp_attack = int_from_bytes(self._emulator.read_bytes(self._address + 0x60, 2))
        self._sp_defense = int_from_bytes(self._emulator.read_bytes(self._address + 0x62, 2))

        pokedex_entry = get_pokedex_entry(self._pokedex_number)
        self._name = pokedex_entry.name

    def get_growth_data(self):
        growth_data = self._decrypted_data[self._G:self._G+12]
        # print(growth_data)
        self._pokedex_number = int_from_bytes(growth_data[0:2])
        # self._item_held = int_from_bytes(growth_data[2:4]) UNUSED
        self._experience = int_from_bytes(growth_data[4:8])
        # self._pp_bonuses = int_from_bytes(growth_data[8]) UNUSED
        # self._friendship = int_from_bytes(growth_data[9]) UNUSED


    def decrypt_data(self, data: bytes):
        if len(data) != 48:
            raise ValueError("Data must be exactly 48 bytes long.")
        
        chunks = [data[i:i+4] for i in range(0, 48, 4)]

        xor_result = b""
        for chunk in chunks:
            # Convert the 4-byte chunk to an integer
            chunk_int = int.from_bytes(chunk, byteorder='little', signed=False)
            # XOR the chunk with the key
            xor_chunk_int = chunk_int ^ self._key
            # Convert the result back to 4 bytes
            xor_chunk_bytes = xor_chunk_int.to_bytes(4, byteorder='little', signed=False)
            # Append to the result
            xor_result += xor_chunk_bytes

        self._decrypted_data = xor_result