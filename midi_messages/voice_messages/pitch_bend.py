import midi_constants
from midi_messages.midi_message import MidiMessage
from midi_common import MessageType


class PitchBend(MidiMessage):
    
    message_type = MessageType.PITCH_BEND

    def __init__(self, bdelta, blength, bstatus, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        self.lsb = self.bdata[0]
        self.msb = self.bdata[1]

    def parse(self):
        pass
