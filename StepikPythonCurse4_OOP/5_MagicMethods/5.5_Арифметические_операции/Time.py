class Time:

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self._normalize()

    def _normalize(self):
        """Helper to handle minute overflow and 24-hour wrap-around."""
        self.hours += self.minutes // 60
        self.minutes %= 60
        self.hours %= 24

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}"
    
    def __add__(self, other):
        if isinstance(other, Time):
            return Time(self.hours+other.hours, self.minutes+other.minutes)
        return NotImplemented
    
    def __iadd__(self, other):
        if isinstance(other, Time):
            self.minutes += other.minutes
            self.hours += other.hours 
            self._normalize()
            return self
        return NotImplemented

time1 = Time(2, 30)
time2 = Time(3, 10)

time1 += time2

print(time1)
print(time2)