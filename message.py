import abc


class Message:

    def __init__(self, bdelta, bstatus, blength, bdata):
        self.delta = bdelta
        self.blength = blength
        self.bdata = bdata

    @abc.abstractmethod
    def parse(self):
        raise NotImplementedError("Must implement parse method")
