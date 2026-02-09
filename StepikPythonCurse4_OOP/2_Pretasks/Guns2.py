class Gun:
    def __init__(self):
        self.shots = 0

    def shoot(self):
        if self.shots % 2 == 0:
            print('pif')
        else:
            print('paf')
        self.shots += 1

    def shots_count(self):
        return self.shots

    def shots_reset(self):
        self.shots = 0
        return self.shots
