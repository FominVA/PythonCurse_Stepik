def alternating_sequence(count=None):
    counter = 1
    generated_count = 0
    while True:
        if count is not None and generated_count >= count:
            return

        if counter % 2 == 1:
            yield counter
        else:
            yield -counter
        
        counter += 1
        if count is not None:
            generated_count += 1


generator = alternating_sequence()

print(next(generator))
print(next(generator))