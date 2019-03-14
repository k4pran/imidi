import midi_constants
from midi_messages.midi_message import MidiMessage
from midi_common import MessageType


class ProgramChange(MidiMessage):

    message_type = MessageType.PROGRAM_CHANGE

    def __init__(self, bdelta, blength, bstatus, bdata):
        super().__init__(bdelta, blength, bstatus, bdata)
        self.program_num = self.bdata[0]

    def parse(self):
        pass
