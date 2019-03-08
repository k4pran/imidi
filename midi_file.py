from midi_reader import MidiReader, ChunkExtractor, MessageExtractor


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

    def allocate_messages(self, messages):
        for message in messages:
            delta = message[0]
            status_byte = message[1][0]
            length = message[1][1]
            data = message[1][2]
            print()


if __name__ == "__main__":
    midi_file = MidiFile("resources/Frozen - Let it go.midi")
    print()