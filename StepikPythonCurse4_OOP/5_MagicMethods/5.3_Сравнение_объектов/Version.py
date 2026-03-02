from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, version: str):
        parts = version.split('.')
        while len(parts) < 3:
            parts.append('0')

        self.version_tuple = tuple(int(p) for p in parts)
        self.version_str = '.'.join(parts)

    def __str__(self):
        return self.version_str
    
    def __repr__(self):
        return f"Version('{self.version_str}')"
    
    def __eq__(self, value):
        if isinstance(value, Version):
            return self.version_tuple == value.version_tuple
        return NotImplemented
    
    def __lt__(self, value):
        if isinstance(value, Version):
            return self.version_tuple < value.version_tuple
        return NotImplemented
    
print(Version('3.0.3') == Version('1.11.28'))
