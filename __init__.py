"""
Compare a list of face encodings against a candidate encoding to see if they match.
:param known_face_encodings: A list of known face encodings
:param face_encoding_to_check: A single face encoding to compare against the list
:param tolerance: How much distance between faces to consider it a match. Lower is more strict. 0.6 is typical best performance.
:return: A list of True/False values indicating which known_face_encodings match the face encoding to check
"""


class Node(object):
    def __init__(self, numbering, name, mean):
        if numbering == 0:
            raise ValueError(f"numbering have to be above 0")
        self.numbering = numbering
        self.name = name
        self.mean = mean

    def __get__(self):
        return self.numbering, self.name, self.mean

    def __set__(self, numbering=0, name=0, mean=0):
        if not (numbering == 0):
            self.numbering = numbering
        if not (name == 0):
            self.name = name
        if not (mean == 0):
            self.mean = mean


class Words(object):
    def __init__(self, day):
        self.wordlist = []
        # How to manage list only has the Node structure?
        self.day = day

    def __get__(self):
        return self.day, self.wordlist

    def __set__(self, day, wordlist):
        self.day = day
        self.wordlist = wordlist

    def edit(self, numbering, name, mean):
        if self.wordlist == []:
            print("no wordlist in words class")
            return 0
        else:
            for node in self.wordlist:
                if node.numbering == numbering and node.name == name:
                    node.mean = mean
                    break
            return 1

    def print_test(self):
        if self.wordlist == []:
            print("no wordlist in words class")
            return 0
        for node in self.wordlist:
            print(f"DAY{node.day}, {node.numbering}, {node.name}")
        return 1

    def print_answer(self):
        if self.wordlist == []:
            print("no wordlist in words class")
            return 0
        for node in self.wordlist:
            print(f"DAY{self.day}, {node.numbering}, {node.name} -> {node.mean}")
        return 1


'''
To need Edit
    Word List
    1 day Words - Node .... Node
    2 day Words - Node .... Node
    ...
    3 day Words - Node .... Node
    
    Node
        numbering
        name
        mean
'''
