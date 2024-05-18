import threading

class WordCounter:
    def __init__(self):
        self.lock = threading.Lock()
        self.word_counts = {}

    def process_text(self, text):
        words = text.split(" ")
        temporary_word_counts = {}
        for word in words:
            if word not in temporary_word_counts:
                temporary_word_counts[word] = 0
            temporary_word_counts[word] += 1
        self._increase_word_counts(temporary_word_counts)

    def get_word_count(self, word):
        self.lock.acquire()
        count = self.word_counts.get(word, 0)
        self.lock.release()
        return count

    def _increase_word_counts(self, word_counts):
        self.lock.acquire()
        for word in word_counts:
            self.word_counts[word] = self.word_counts.get(word, 0) + word_counts[word]
        self.lock.release()
