from midi_messages.midi_message import MidiMessage


class NotesOff(MidiMessage):

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        self