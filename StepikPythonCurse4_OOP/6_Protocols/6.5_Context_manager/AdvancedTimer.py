from time import perf_counter, sleep

class AdvancedTimer:

    def __init__(self):
        self.last_run = None
        self.runs = []
        self.min = None
        self.max = None

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.last_run = perf_counter() - self.start
        self.runs.append(self.last_run)
        if self.min is None:
            self.min = self.last_run
        else:
            self.min = min(self.runs)
        if self.max is None:
            self.max = self.last_run
        else:
            self.max = max(self.runs)
        return False
    
timer = AdvancedTimer()

with timer:
    sleep(1.5)
print(round(timer.last_run, 1))

with timer:
    sleep(0.7)
print(round(timer.last_run, 1))

with timer:
    sleep(1)
print(round(timer.last_run, 1))
