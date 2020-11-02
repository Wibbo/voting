
import random

class voter:
    def __init__(self, id, options):
        self.id = id
        self.options = options.copy()
        self.voted_for = None

        self.random_choice()

    def random_choice(self):
        random.shuffle(self.options)

        