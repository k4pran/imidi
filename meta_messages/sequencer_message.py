import midi_constants
from meta_messages import meta_message


class SequencerMessage(meta_message.MetaMessage):

    type = b'\x7F'

    def __init__(self, blength, bdata):
        super().__init__(blength, bdata)
        self.id: str = None
        self.id_len: int = None

    def parse(self):
        self.id_len = int.from_bytes(self.blength, byteorder='big') - midi_constants.SEQUENCER_MESSAGE_DATA_SIZE
        self.id = self.bdata[:-1].decode("utf-8")
