from midi_reader import ChunkExtractor, MessageExtractor
from header import Header
from message_allocator import *
from midi_common import MessageType
from track import Track
from note import Note
from pathlib import Path

class MidiFile:

    def __init__(self, midi_path):
        self.midi_path = midi_path
        self.name = Path(midi_path).stem
        self.header = None
        self.tracks = []

        self.copyright_notice = ""

        self._current_track = None

        self.load_midi()

    def load_midi(self):
        chunk_extractor = ChunkExtractor(self.midi_path)
        self.header = Header(chunk_extractor.header)
        for track in chunk_extractor.tracks:
            self._current_track = Track(track[1], track[2])
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
            self._current_track.add_message(message)
            self.handle_special(message)

        self._current_track.parse()

    def handle_special(self, message):
        if message.message_type == MessageType.COPYRIGHT_NOTICE:
            self.copyright_notice = message.copyright_text


    def get_track_count(self):
        return self.header.tracks


if __name__ == "__main__":
    midi_file = MidiFile("resources/Frozen - Let it go.midi")
