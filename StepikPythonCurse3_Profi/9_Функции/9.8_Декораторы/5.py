import functools

def make_html(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            result = f'<{tag}>{func(*args, **kwargs)}</{tag}>'
            return result
        return wrapper
    return decorator

@make_html('del')
def get_text(text):
    return text
    
print(get_text('Python'))