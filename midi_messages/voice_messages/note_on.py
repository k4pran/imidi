import midi_constants
from midi_messages.midi_message import MidiMessage
from midi_common import MessageType


class NoteOn(MidiMessage):

    message_type = MessageType.NOTE_ON

    def __init__(self, bdelta, blength, bstatus, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        self.note = self.bdata[0]
        self.velocity = self.bdata[1]

    def parse(self):
        pass
