from enum import Enum


class Header:

    SIGNATURE = "MThd"

    def __init__(self, raw_header):
        self.raw_header = raw_header
        self.length: int
        self.format: self.Format
        self.tracks: int
        self.division: self.Division

    def parse(self):
        pass

    class Format(Enum):
        SINGLE_TRACK = 0
        SIMULTANEOUS = 1
        SEQUENTIAL = 2

    class Division(Enum):
        pass




