import abc

from message import Message
import midi_constants


class MetaMessage(Message):

    bstatus = b'\xFF'
    fixed_length_types = frozenset([
        b'\x00', b'\x20', b'\x21', b'\x2F',
        b'\x51', b'\x54', b'\x58',
        b'\x59'])

    def __init__(self, blength, bdata):
        super().__init__(MetaMessage.bstatus, blength, bdata)
        self.type = self.determine_type()

    @abc.abstractmethod
    def parse(self):
        raise NotImplementedError("Must implement parse method")

    def determine_type(self):
        type_ind = midi_constants.META_TYPE_IND
        return self.bdata[type_ind, type_ind + midi_constants.META_TYPE_SIZE]
