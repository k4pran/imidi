from note import Note
from midi_common import MessageType

class Track:

    SIGNATURE = "MTrk"

    def __init__(self, blength, bdata):
        self.blength = blength
        self.bdata = bdata
        self.messages = []
        self.notes = []

        self.track_name = None
        self.track_number = None
        self.instrument = None

        self.key = None
        self.time_sig = None
        self.tempo = None

        self.key_changes = []
        self.time_sig_changes = []
        self.tempo_changes = []

        self._note_on_msgs = []
        self._note_off_msgs = []

    def add_message(self, message):
        self.messages.append(message)
        self.handle_message(message)

    def handle_message(self, message):
        message_type = message.message_type

        if message_type == MessageType.TRACK_NAME:
            self.track_name = message

        elif message_type == MessageType.SEQUENCE_NUMBER:
            self.track_number = message

        elif message_type == MessageType.INSTRUMENT:
            self.instrument = message

        elif message_type == MessageType.NOTE_ON:
            if message.velocity == 0:
                self._note_off_msgs.append(message)
            else:
                self._note_on_msgs.append(message)

        elif message_type == MessageType.NOTE_OFF or message_type == MessageType.ALL_NOTES_OFF:
            self._note_off_msgs.append(message)

        elif message_type == MessageType.TIME_SIGNATURE:
            if not self.time_sig:
                self.time_sig = message
            else:
                self.time_sig_changes.append(message)

        elif message_type == MessageType.KEY_SIGNATURE:
            if not self.key:
                self.key = message
            else:
                self.key_changes.append(message)

        elif message_type == MessageType.TEMPO:
            if not self.tempo:
                self.tempo = message
            else:
                self.tempo_changes.append(message)

    def parse(self):
        self.notes = Note.pair_notes(self._note_on_msgs, self._note_off_msgs)