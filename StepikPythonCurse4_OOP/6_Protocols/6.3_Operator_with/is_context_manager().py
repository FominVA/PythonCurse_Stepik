def is_context_manager(obj):
    return hasattr(obj, '__enter__') and hasattr(obj, '__exit__')

print(is_context_manager(open('../output.txt', mode='w')))

