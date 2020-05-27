from random import Random


class RandomStringGenerator:

    def __init__(self):
        self.chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t",
                      "u", "v", "w", "x", "y", "z", " "]
        self.random = Random()

    def getRandomString(self, length):
        random_string = ""
        for i in range(length):
            random_string += self.random.choice(self.chars)
        return random_string
