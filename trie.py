import string


class Node(object):
    '''Trie node class.'''

    def __init__(self):
        self.next = dict.fromkeys(string.ascii_lowercase, None)
        self.end = False  # check if it's end of words


class Trie(object):
    '''Trie data structure class.'''

    def __init__(self):
        self.root = Node()

    def insert_words(self, word_list: list) -> None:
        '''Insert words into trie - 1 time thing.'''
        for word in word_list:
            if len(word) >= 3 and word.isalpha():
                temp = self.root
                for char in word.lower():
                    if temp.next[char] is None:
                        temp.next[char] = Node()
                    temp = temp.next[char]
                temp.end = True
