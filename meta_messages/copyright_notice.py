from meta_messages.meta_message import MetaMessage
from midi_exceptions import IncorrectStatusException
from midi_common import MessageType


class CopyrightNotice(MetaMessage):

    btype = b'\x02'
    message_type = MessageType.COPYRIGHT_NOTICE
    name = "copyright notice"

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        if bstatus != b'\xFF':
            raise IncorrectStatusException("Invalid status: {:2x} for meta event".format(bstatus))
        self.copyright_text = ""

    def parse(self):
        self.copyright_text = self.bdata.decode("utf-8")
