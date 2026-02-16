class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode

    @property
    def hexcode(self):
        return f"{self.r:02X}{self.g:02X}{self.b:02X}"
    
    @hexcode.setter
    def hexcode(self, value):
        self.r = int(value[0:2], 16)
        self.g = int(value[2:4], 16)
        self.b = int(value[4:6], 16)
