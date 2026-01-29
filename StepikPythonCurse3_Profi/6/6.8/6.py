from collections import Counter

def func_max():
    result = [(key, value) for key, value in data.items() if value == max(data.values())]
    return result

def func_min():
    result = [(key, value) for key, value in data.items() if value == min(data.values())]
    return result

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.__dict__['min_values'] = func_min
data.__dict__['max_values'] = func_max

data2 = Counter(['a', 'b', 'c','d'])
data2.__dict__['min_values'] = func_min
data2.__dict__['max_values'] = func_max

print(data2.min_values())