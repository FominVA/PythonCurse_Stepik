def parse_ranges(ranges):
    ranges = (i for i in ranges.split(','))
    new_ranges = (r.split('-') for r in ranges)
    numbers = ((int(a), int(b)) for a, b in new_ranges)
    
    for a, b in numbers:
        yield from range(a, b+1)


print(*parse_ranges('1-2,4-4,8-10'))