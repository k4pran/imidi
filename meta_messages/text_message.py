from meta_messages.meta_message import MetaMessage
from midi_exceptions import IncorrectStatusException
from midi_common import MessageType


class TextMessage(MetaMessage):

    btype = b'\x01'
    message_type = MessageType.TEXT_MESSAGE
    name = "text"

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        if bstatus != b'\xFF':
            raise IncorrectStatusException("Invalid status: {:2x} for meta event".format(bstatus))
        self.text = ""

    def parse(self):
        self.text = self.bdata.decode("utf-8")

