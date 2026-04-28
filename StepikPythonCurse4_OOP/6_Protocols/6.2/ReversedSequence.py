class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return ReversedSequence(self.sequence[-1-item])
        if isinstance(item, int):
            return self.sequence[-1-item]

    def __reversed__(self):
        return self.sequence

    def __iter__(self):
        return iter(reversed(self.sequence))


reversed_list = ReversedSequence([1, 2, 3, 4, 5])

print(reversed_list[0])
print(reversed_list[1])
print(reversed_list[2])