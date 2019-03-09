from midi_messages.midi_message import MidiMessage


class OmniModeOn(MidiMessage):

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        self