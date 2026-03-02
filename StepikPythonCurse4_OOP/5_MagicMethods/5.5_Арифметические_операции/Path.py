class Path:

    def __init__(self, *args):
        self.parts = []
        for arg in args:
            if isinstance(arg, Path):
                self.parts.extend(arg.parts)
            elif isinstance(arg, str):
                self.parts.append(str(arg))
                
    def __repr__(self):
        return f"Path('{'/'.join(self.parts)}')"

    
    def __str__(self):
        return '/'.join(self.parts)

        
    def __truediv__(self, other):
        # Обработка оператора /
        if isinstance(other, (Path, str)):
            # Создаем новый объект Path, передавая текущий и новый путь
            return Path(self, other)
        return NotImplemented

    def __itruediv__(self, other):
        # Обработка оператора /=
        if isinstance(other, Path):
            self.parts.extend(other.parts)
        elif isinstance(other, str):
            self.parts.extend([p for p in other.split('/') if p])
        else:
            return NotImplemented
        return self
        
path1 = Path('home', 'user')
path2 = Path('projects', 'python')
path3 = Path('docs', '2025')
path4 = Path('book.pdf')


path_a = path1 / path2
print(path_a)

path_b = path_a / path3
print(path_b)

path_c = path_b / path4
print(path_c)

path_d = Path('var', 'log') / 'system'
print(path_d)

path_d /= Path('kernel')
print(path_d)

combined = Path('tmp', 'files') / '2025' / Path('reports/omg') / 'report.pdf'
print(combined)

seq_path = Path('home', 'user')
seq_path /= Path('downloads', 'photos')
print(seq_path)

seq_path /= 'vacation'
print(seq_path)

seq_path /= Path('2025', 'summer', 'trip.jpg')
print(seq_path)