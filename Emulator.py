import mgba.audio
import mgba.core
import mgba.gba
import mgba.image
import mgba.log
import mgba.png
import mgba.vfs
from mgba import ffi, lib, libmgba_version_string

import PIL.Image
import PIL.PngImagePlugin

save_state_path = "C:/Users/Peter/Documents/Projects/PokemonFireRedBot_libmgba/rom/saves/"
# state_path = f"{save_state_path}intro.ss0"
# state_path = f"{save_state_path}squirtle_start.ss0"
# state_path = f"{save_state_path}squirtle_level_6.ss0"
state_path = f"{save_state_path}forrest.ss0"

button_map = {
    "A": 0x1,
    "B": 0x2,
    "Select": 0x4,
    "Start": 0x8,
    "Right": 0x10,
    "Left": 0x20,
    "Up": 0x40,
    "Down": 0x80,
    "R": 0x100,
    "L": 0x200,
}

class Emulator:

    _emulation_speed: float = ( 1 / 60 )
    _image_width: int = 540
    _image_height: int = 400

    _pressed_button: int = 0

    def __init__(self):
        
        # Prevents relentless spamming to stdout by libmgba.
        mgba.log.silence()

        self._core = mgba.core.load_path("C:/Users/Peter/Documents/Projects/PokemonFireRedBot_libmgba/rom/Pokemon - FireRed Version (USA, Europe).gba");
        # self._core.load_save(mgba.vfs.open_path(state_path, "r+"))
        self._core.load_save(mgba.vfs.open_path(state_path, "r+"))

        self._screen = mgba.image.Image(*self._core.desired_video_dimensions())
        self._core.set_video_buffer(self._screen)
        self._core.reset()

        with open(state_path, "rb") as state_file:
                self.load_save_state(state_file.read())

    def run_frame(self):
        self._core.run_frame()

        #resets the pressed key
        if self._pressed_button != 0:
            self._pressed_button = 0
            self._core._core.setKeys(self._core._core, 0x0)



    @property
    def emulation_speed(self):
        return self._emulation_speed

    def set_emulation_speed(self, speed: int):
        self._emulation_speed = (1 / (60 * speed))

    def get_current_screen_image(self) -> PIL.Image.Image:
        return self._screen.to_pil().resize((self._image_width, self._image_height), resample=False)
    
    def read_bytes(self, address: int, length: int = 1) -> bytes:
        """
        Reads a block of memory from an arbitrary address on the system
        bus. That means that you need to specify the full memory address
        rather than an offset relative to the start of a given memory
        area.

        This is helpful if you are working with the symbol table or
        pointers.

        :param address: Full memory address to read from
        :param length: Number of bytes to read
        :return: Data read from that memory location
        """
        bank = address >> 0x18
        result = bytearray(length)
        if bank == 0x2:
            offset = address & 0x3FFFF
            if offset + length > 0x3FFFF:
                raise RuntimeError("Illegal range: EWRAM only extends from 0x02000000 to 0x0203FFFF")
            ffi.memmove(result, ffi.cast("char*", self._core._native.memory.wram) + offset, length)
        elif bank == 0x3:
            offset = address & 0x7FFF
            if offset + length > 0x7FFF:
                raise RuntimeError("Illegal range: IWRAM only extends from 0x03000000 to 0x03007FFF")
            ffi.memmove(result, ffi.cast("char*", self._core._native.memory.iwram) + offset, length)
        elif bank >= 0x8:
            offset = address - 0x08000000
            ffi.memmove(result, ffi.cast("char*", self._core._native.memory.rom) + offset, length)
        else:
            raise RuntimeError(f"Invalid memory address for reading: {hex(address)}")
        return result
    
    def load_save_state(self, state: bytes) -> None:
        """
        Loads a serialised emulator state (i.e. a save state in mGBA parlance)
        :param state: The raw save state data
        """
        vfile = mgba.vfs.VFile.fromEmpty()
        vfile.write(state, len(state))
        vfile.seek(0, whence=0)
        self._core.load_state(vfile)

    def press_button(self, button: str):
        self._pressed_button = button_map[button]
        self._core._core.setKeys(self._core._core, button_map[button])
