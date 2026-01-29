def sourcetemplate(url):
    def func(**kwargs):
        if kwargs:
            link = f'{url}?'
            for key, value in sorted(kwargs.items()):
                link=link+ f'{key}={value}&'
            return link[:-1]
        return url
    return func

url = 'https://stepik.org/lesson/651459/step/14'
load = sourcetemplate(url)
print(load(thread='solutions', unit=648165))
          