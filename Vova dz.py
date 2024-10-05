class GeneratorIterable:
    def __init__(self, max_value):
        self.max_value = max_value

    def __iter__(self):
        return GeneratorIterator(self.max_value)


class GeneratorIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current_value = 0

    def __next__(self):
        if self.current_value < self.max_value:
            result = self.current_value
            self.current_value += 1
            return result
        raise StopIteration



iterable = GeneratorIterable(5)
for value in iterable:
    print(value)
