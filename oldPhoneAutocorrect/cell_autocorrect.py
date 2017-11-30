# Input format: Textfile starts with a list of words seperated by newlines that
# comprises the available dictionary.  Followed by a list of digits seperated
# by newlines to be autocorrected based on the dictionary
class TrieNode:

    def __init__(self):
        self.words = []
        self.children = {}

    @staticmethod
    def char2int(char):
        conversion = {"A": "2", "B": "2", "C": "2", "D": "3", "E": "3",
                      "F": "3", "G": "4", "H": "4", "I": "4", "J": "5",
                      "K": "5", "L": "5", "M": "6", "N": "6", "O": "6",
                      "P": "7", "Q": "7", "R": "7", "S": "7", "T": "8",
                      "U": "8", "V": "8", "W": "9", "X": "9", "Y": "9",
                      "Z": "9"}
        return conversion[char]

    def traverse(self, str):
        if (str == ""):
            if self.words == []:
                return "<No Results>"
            else:
                return ",".join(self.words).lower()
        if str[0] not in self.children:
            return "<No Results>"
        return self.children[str[0]].traverse(str[1:])

    def construct(self, word, partial_word):
        if (partial_word == ""):
            self.words.append(word)
        else:
            if self.char2int(partial_word[0]) not in self.children.keys():
                self.children[self.char2int(partial_word[0])] = TrieNode()
            self.children[self.char2int(partial_word[0])].\
                construct(word, partial_word[1:])

    def __repr__(self):
        return "vals: " + str(self.words) + "children: " + str(self.children)


class Autocorrect:
    def __init__(self, filein, fileout):
        self.filein = filein
        self.fileout = fileout

    def process(self):
        words = True
        base_node = TrieNode()
        nums = []
        results = []
        with open(self.filein) as f:
            for line in f:
                line = line.rstrip()

                # Checks that line is word
                if words:
                    if not line[0].isalpha():
                        words = False

                if words:
                    base_node.construct(line, line)
                else:
                    nums.append(line)

        with open(self.fileout, 'w') as f:
            for line in nums:
                f.write(line+": " + base_node.traverse(line))
                results.append(line+": " + base_node.traverse(line))

# Example Use:
# Autocorrect("t9-test-input.txt", "t9-test-output.txt").process()
