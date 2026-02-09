class Scales:
    def __init__(self):
        self.r_scale = 0
        self.l_scale = 0

    def add_right(self, m):
        self.r_scale += m

    def add_left(self, m):
        self.l_scale += m

    def get_result(self):
        if self.r_scale > self.l_scale:
            return 'Правая чаша тяжелее'
        elif self.r_scale < self.l_scale:
            return 'Левая чаша тяжелее'
        else:
            return 'Весы в равновесии'