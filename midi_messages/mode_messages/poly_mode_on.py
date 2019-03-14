from midi_messages.midi_message import MidiMessage
from midi_common import MessageType


class PolyModeOn(MidiMessage):

    message_type = MessageType.POLY_MODE_ON

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)

