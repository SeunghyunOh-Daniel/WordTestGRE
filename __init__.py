
class Node:
    def __init__(self, day, numbering, name, mean):
        self.__day = day
        self.__numbering = numbering
        self.__name = name
        self.__mean = mean
    def __getattr__(self):
        return [self.__day, self.__numbering, self.__name, self.__mean]
    def __setattr__(self, day, numbering, name, mean):
        self.__day = day
        self.__numbering = numbering
        self.__name = name
        self.__mean = mean


class Word(Node):
    def __init__(self, index, day, numbering, name, mean):
        super().__init__(day, numbering, name, mean)
        self.__index = index
    def __getattr__(self):
        return [self.__index] + super().__getattr__()

    def __setattr__(self, index, day, numbering, name, mean):
        self.__index = index
        self.__setattr__(day, numbering, name, mean)
