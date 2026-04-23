class DevelopmentTeam:
    def __init__(self):
        self.juniors = []
        self.seniors = []

    def add_junior(self, *name):
        for i in name:
            self.juniors.append((i, 'junior'))

    def add_senior(self, *name):
        for i in name:
            self.seniors.append((i, 'senior'))

    def __iter__(self):
        yield from self.juniors
        yield from self.seniors

smart_monkey = DevelopmentTeam()

smart_monkey.add_senior('Gvido', 'Alan')
smart_monkey.add_junior('Denis')

print(list(smart_monkey))

