class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:                       # при первом вызове создаем объект
            cls._instance = object.__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.program_name = 'GenerationPy'
        self.environment = 'release'
        self.loglevel = 'verbose'
        self.version = '1.0.0'