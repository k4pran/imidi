import midi_constants
from midi_messages.midi_message import MidiMessage
from midi_common import MessageType


class PolyphonicAftertouch(MidiMessage):

    message_type = MessageType.POLYPHONIC_AFTERTOUCH


    def __init__(self, bdelta, blength, bstatus, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        self.key = self.bdata[0]
        self.pressure = self.bdata[1]

    def parse(self):
        pass
