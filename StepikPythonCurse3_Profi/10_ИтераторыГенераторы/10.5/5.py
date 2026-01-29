from datetime import date, timedelta

def dates(start, count=None):
    if count is None:
        while True:
            try:
                yield start
                start += timedelta(1)
            except OverflowError:
                break
    else:
        for x in range(count):
            current_date = start+timedelta(x)
            yield current_date


generator = dates(date(2022, 3, 8))

print(next(generator))
print(next(generator))
print(next(generator))