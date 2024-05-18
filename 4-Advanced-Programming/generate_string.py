def generate_string(string, frequency):
    for char in string:
        for _ in range(frequency):
            yield char


class GenerateString:
    def __init__(self, string, frequency):
        self.string = string
        self.frequency = frequency

    def __iter__(self):
        self.current_char_index = 0
        self.char_counter = 0
        return self

    def __next__(self):
        if self.char_counter >= self.frequency:
            self.char_counter = 0
            self.current_char_index += 1

        if self.current_char_index >= len(self.string):
            raise StopIteration

        self.char_counter += 1
        return self.string[self.current_char_index]