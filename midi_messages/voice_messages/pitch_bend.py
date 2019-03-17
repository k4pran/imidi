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

    def __str__(self):
        return "|| Pitch bend || {padding:10} coarse - {0} {padding:4} fine - {1}".format(self.msb, self.lsb, padding="")