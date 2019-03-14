from midi_reader import ChunkExtractor, MessageExtractor
from header import Header
from message_allocator import *
from midi_common import MessageType
from track import Track
from note import Note

class MidiFile:

    def __init__(self, midi_path):
        self.midi_path = midi_path
        self.name = None
        self.header = None
        self.tracks = []
        self.note_on_msgs = []
        self.note_off_msgs = []
        self.load_midi()

    def load_midi(self):
        chunk_extractor = ChunkExtractor(self.midi_path)
        self.header = Header(chunk_extractor.header)
        for track in chunk_extractor.tracks:
            message_extractor = MessageExtractor(track)
            self.tracks.append(Track(message_extractor.track[1], message_extractor.track[2]))
            self.allocate_messages(message_extractor.events)

    def allocate_messages(self, raw_messages):
        for raw_message in raw_messages:
            delta = raw_message[0]
            status_byte = raw_message[1][0]
            length = raw_message[1][1]
            data = raw_message[1][2]

            message = allocate(delta, status_byte, length, data)
            self.tracks[-1].messages.append(message)
            self.handle_message(message)

        Note.pair_notes(self.note_on_msgs, self.note_off_msgs)

    def handle_message(self, message):
        message_type = message.message_type
        if message_type == MessageType.NOTE_ON:
            if message.velocity == 0:
                self.note_off_msgs.append(message)
            else:
                self.note_on_msgs.append(message)

        elif message_type == MessageType.NOTE_OFF or message_type == MessageType.ALL_NOTES_OFF:
            self.note_off_msgs.append(message)

        elif message_type == MessageType.TIME_SIGNATURE:
            pass

        elif message_type == MessageType.KEY_SIGNATURE:
            pass

        elif message_type == MessageType.TEMPO:
            pass

    def get_track_count(self):
        return self.header.tracks


if __name__ == "__main__":
    midi_file = MidiFile("resources/Frozen - Let it go.midi")
    print()
