_original_print = print
def custom_print(*args, sep=' ', end='\n', file=None, flush=False):
    modified_args = []
    for arg in args:
        if isinstance(arg, str):
            modified_args.append(arg.upper())
        else:
            modified_args.append(arg)
    
    if isinstance(sep, str):
        modified_sep = sep.upper()
        
    # 3. Модификация end: если end является строкой, преобразуем ее
    modified_end = end
    if isinstance(end, str):
        modified_end = end.upper()

    _original_print(*modified_args, sep=modified_sep, end=modified_end, file=file, flush=flush)

print = custom_print

print('beegeek', [1, 2, 3], 4)