import abc


class Message:

    def __init__(self, bstatus, blength, bdata):
        self.bstatus = bstatus
        self.blength = blength
        self.bdata   = bdata

    @abc.abstractmethod
    def parse(self):
        raise NotImplementedError("Must implement parse method")
