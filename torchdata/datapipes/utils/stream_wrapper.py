from torch.utils.data.datapipes.utils.common import TorchStreamWrapper


class StreamWrapper(TorchStreamWrapper):

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, obj):
        self.__dict__ = obj
