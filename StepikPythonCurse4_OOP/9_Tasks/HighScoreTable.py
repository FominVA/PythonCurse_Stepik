class HighScoreTable:
    def __init__(self, length):
        self.length = length
        self.scores_list = []
        self.scores = []

    def update_scores_attr(self):
        self.scores = sorted(self.scores_list, reverse=True)

    def update(self, num):
        if isinstance(num, int) and len(self.scores_list) < self.length:
            self.scores_list.append(num)
            self.scores_list.sort(reverse=True)
        elif isinstance(num, int) and len(self.scores_list) == self.length:
            min_score = min(self.scores_list)
            if num > min_score:
                self.scores_list[self.scores_list.index(min_score)] = num
                self.scores_list.sort(reverse=True)
        return self.update_scores_attr()

    def reset(self):
        self.scores.clear()

high_score_table = HighScoreTable(3)

print(high_score_table.scores)
high_score_table.update(10)
high_score_table.update(8)
high_score_table.update(12)
print(high_score_table.scores)

high_score_table.update(3)
high_score_table.update(6)
high_score_table.update(1)
print(high_score_table.scores)

high_score_table.reset()
print(high_score_table.scores)

