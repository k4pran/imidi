from midi_reader import ChunkExtractor, MessageExtractor
from message_allocator import *


class MidiFile:

    def __init__(self, midi_path):
        self.midi_path = midi_path
        self.name = None
        self.messages = []
        self.parse()

    def parse(self):
        chunk_extractor = ChunkExtractor(self.midi_path)
        for track in chunk_extractor.tracks:
            message_extractor = MessageExtractor(track)
            self.allocate_messages(message_extractor.events)

    def allocate_messages(self, raw_messages):
        ind = 0
        for raw_message in raw_messages:
            ind += 1
            delta = raw_message[0]
            status_byte = raw_message[1][0]
            length = raw_message[1][1]
            data = raw_message[1][2]

            self.messages.append(allocate(delta, status_byte, length, data))
        print()


if __name__ == "__main__":
    midi_file = MidiFile("resources/Frozen - Let it go.midi")
    print()