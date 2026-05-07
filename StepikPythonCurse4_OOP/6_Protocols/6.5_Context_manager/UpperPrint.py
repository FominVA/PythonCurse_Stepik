import sys

class UpperPrint:

    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.upper_write

    def upper_write(self, text):
        self.original_write(text.upper())

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.original_write

with UpperPrint():
    print('Bee', 'Geek', 'Love', sep=' one ', end=' end')