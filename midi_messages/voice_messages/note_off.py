import midi_constants
from midi_messages.midi_message import MidiMessage
from midi_common import MessageType
from utils_common import  get_note_name


class NoteOff(MidiMessage):
    
    message_type = MessageType.NOTE_OFF

    def __init__(self, bdelta, blength, bstatus, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        self.note_val = self.bdata[0]
        self.velocity = self.bdata[1]

        self.note = get_note_name(self.note_val)

    def parse(self):
        pass

    def __str__(self):
        return "|| Note Off       || {padding:10} note     - {0} {padding:4} velocity - {1}".format(self.note, self.velocity, padding="")