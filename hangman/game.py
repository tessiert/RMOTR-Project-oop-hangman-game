from .exceptions import *


class GuessAttempt(object):

    def __init__(self, letter, hit=False, miss=False):

        # Truth values for 'hit' and 'miss' must be different
        if hit == miss:
            raise InvalidGuessAttempt

        self.hit = hit
        self.miss = miss

    def is_hit(self):
        return self.hit

    def is_miss(self):
        return self.miss






class GuessWord(object):

    def __init__(self, answer):

        self.answer = answer
        self.masked = '*'*len(answer)

    def perform_attempt(self, letter):

        pass


class HangmanGame(object):

    WORD_LIST = ['rmotr', 'python', 'awesome']

    def __init__(self, word_list=WORD_LIST, number_of_guesses=5):

        self.word_list = word_list
        self.number_of_guesses = number_of_guesses

    #@select_random_word
    def select_random_word(cls):
        pass
