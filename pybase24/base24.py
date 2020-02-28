from typing import Union

ALPHABET = 'ZAC2B3EF4GH5TK67P8RS9WXY'
ALPHABET_LENGTH = 24

encode_map = dict(zip(range(ALPHABET_LENGTH), ALPHABET))
decode_map = {
    **dict(zip(ALPHABET, range(ALPHABET_LENGTH))),
    **dict(zip(ALPHABET.lower(), range(ALPHABET_LENGTH)))
}


def encode24(data: Union[bytes, bytearray]) -> str:
    """
    Encode bytes to a string using base24.
    :param data: A byte array, length must be a multiple of 4.
    :return: The encoded string.
    """
    if not isinstance(data, (bytes, bytearray)):
        raise ValueError(
            f'data must be a bytes-like object, received: {type(data)}')

    data_length = len(data)
    if data_length % 4 != 0:
        raise ValueError('data length must be a multiple of 4 bytes (32 bits)')

    result = list()
    for i in range(data_length // 4):
        j = i * 4
        mask = 0xFF

        b3 = data[j + 0] & mask
        b2 = data[j + 1] & mask
        b1 = data[j + 2] & mask
        b0 = data[j + 3] & mask
        value = 0xFFFFFFFF & ((b3 << 24) | (b2 << 16) | (b1 << 8) | b0)

        sub_result = list()
        for _ in range(7):
            idx = int(value % ALPHABET_LENGTH)
            value = value // ALPHABET_LENGTH
            sub_result.insert(0, encode_map.get(idx))

        sub_result = ''.join(sub_result)
        result.append(sub_result)

    return ''.join(result)


def decode24(data: str) -> bytearray:
    """
    Decode a string to a byte array using base24.
    :param data: A string encoded in base24, length must be a multiple of 7.
    :return: The decoded bytes.
    """
    data_length = len(data)
    if data_length % 7 != 0:
        raise ValueError('data length must be a multiple of 7 chars.')

    result = bytearray()

    for i in range(data_length // 7):
        j = i * 7
        value = 0

        sub_data = data[j:j + 7]
        for s in sub_data:
            idx = decode_map.get(s)
            if idx is None:
                raise ValueError(f'Unsupported character in input: {s}')
            else:
                value = ALPHABET_LENGTH * value + idx

        mask = 0xFF
        b0 = (value & (mask << 24)) >> 24
        b1 = (value & (mask << 16)) >> 16
        b2 = (value & (mask << 8)) >> 8
        b3 = (value & (mask << 0)) >> 0

        result.append(b0)
        result.append(b1)
        result.append(b2)
        result.append(b3)

    return result
