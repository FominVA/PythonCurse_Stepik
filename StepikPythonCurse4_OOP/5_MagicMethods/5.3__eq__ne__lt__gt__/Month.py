from functools import total_ordering

@total_ordering
class Month:

    def __init__(self, year, month):
        self.year = year
        self.month = month

    def __str__(self):
        return f"{self.year}-{self.month}"

    def __repr__(self):
        return f"Month({self.year}, {self.month})"
        
    def __eq__(self, other):
        if isinstance(other, Month):
            return self.year == other.year and self.month == other.month
        elif isinstance(other, tuple) and len(other) == 2:
            return (self.year, self.month) == other
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Month):
            # Tuples compare lexicographically: first element, then second
            return (self.year, self.month) < (other.year, other.month)
        elif isinstance(other, tuple) and len(other) == 2:
            return (self.year, self.month) < other
        return NotImplemented
    
print(Month(1999, 12) == Month(1999, 12))
print(Month(1999, 12) < Month(2000, 1))
print(Month(1999, 12) > Month(2000, 1))
print(Month(1999, 12) <= Month(1999, 12))
print(Month(1999, 12) >= Month(2000, 1))