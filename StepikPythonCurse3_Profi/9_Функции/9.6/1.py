
def get_digits(number: int | float) -> list[int]:
    result = []
    if isinstance(number, int):
        for i in str(number):
            result.append(int(i))
    if isinstance(number, float):
        number = str(number).replace('.', '')
        for i in number:
            result.append(int(i))
    return result
    
print(get_digits(16733))