from enum import Enum


class Header:

    SIGNATURE = "MThd"

    def __init__(self, raw_header):
        self.raw_header = raw_header
        self.blength = raw_header[1]
        self.length = int.from_bytes(raw_header[1], byteorder='big')
        self.format = self.Format(int.from_bytes(raw_header[2], byteorder='big'))
        self.tracks = int.from_bytes(raw_header[3], byteorder='big')
        self.division_type = self.Division((raw_header[4][0] >> 7))
        self.tick_division = raw_header[4][0] & ~(1 << 15)

    def parse(self):
        self.length = self.raw_header

    class Format(Enum):
        SINGLE_TRACK = 0
        SIMULTANEOUS = 1
        SEQUENTIAL = 2

    class Division(Enum):
        PQN = 0
        FPS = 1




