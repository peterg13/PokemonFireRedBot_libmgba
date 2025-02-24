
#making my own so we don't always have to type byteorder
def int_from_bytes(bytes: bytes) -> int:
    return int.from_bytes(bytes, byteorder='little')
