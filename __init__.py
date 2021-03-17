
class Word:
    def __init__(self, name, mean):
        self.__name = name
        self.__meaning = meaning


class Wordlist(Word):
    def __init__(self, index, name, mean, day):
        super().__init__(name, mean)
        self.__index = index
        self.__day = day
