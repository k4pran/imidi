from meta_messages.meta_message import MetaMessage
from midi_exceptions import IncorrectStatusException


class Lyric(MetaMessage):

    btype = b'\x05'
    name = "lyric"

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        if bstatus != b'\xFF':
            raise IncorrectStatusException("Invalid status: {:2x} for meta event".format(bstatus))
        self.lyric = ""

    def parse(self):
        self.lyric = self.bdata.decode("utf-8")
