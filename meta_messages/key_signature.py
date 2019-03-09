from meta_messages.meta_message import MetaMessage
from enum import Enum

from midi_exceptions import IncorrectStatusException


class KeySignature(MetaMessage):

    btype = b'\x59'
    name = "key signature"

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        if bstatus != b'\xFF':
            raise IncorrectStatusException("Invalid status: {:2x} for meta event".format(bstatus))
        self.minor_flag: bool = None
        self.key = None

    def parse(self):
        self.minor_flag = bool.from_bytes(self.bdata[1], byteorder='big')
        if self.is_major():
            self.key = MajorKey(int.from_bytes(self.bdata[0], byteorder='big'))
        else:
            self.key = MinorKey(int.from_bytes(self.bdata[0], byteorder='big'))

    def is_major(self):
        return not self.minor_flag

    def is_minor(self):
        return self.minor_flag


class MajorKey(Enum):
    C_FLAT_MAJOR = -7
    G_FLAT_MAJOR = -6
    D_FLAT_MAJOR = -5
    A_FLAT_MAJOR = -4
    E_FLAT_MAJOR = -3
    B_FLAT_MAJOR = -2
    F_MAJOR = -1

    C_MAJOR = 0

    G_MAJOR = 1
    D_MAJOR = 2
    A_MAJOR = 3
    E_MAJOR = 4
    B_MAJOR = 5
    F_SHARP_MAJOR = 6
    C_SHARP_MAJOR = 7

class MinorKey(Enum):
    A_FLAT_MINOR = -7
    E_FLAT_MINOR = -6
    B_FLAT_MINOR = -5
    F_MINOR = -4
    C_MINOR = -3
    G_MINOR = -2
    D_MINOR = -1

    A_MINOR = 0

    E_MINOR = 1
    B_MINOR = 2
    F_SHARP_MINOR = 3
    C_SHARP_MINOR = 4
    G_SHARP_MINOR = 5
    D_SHARP_MINOR = 6
    A_SHARP_MINOR = 7