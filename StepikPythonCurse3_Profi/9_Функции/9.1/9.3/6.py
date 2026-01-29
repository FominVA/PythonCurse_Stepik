from string import ascii_letters, ascii_uppercase, ascii_lowercase

d = { 0: 'в пароле нет ни одной буквы',
      1: 'в пароле нет ни одной заглавной буквы',
      2: 'в пароле нет ни одной строчной буквы',
      3: 'в пароле нет ни одной цифры'}

def verification(login, password, success, failure):
    result = [any(map(lambda x: True if x in ascii_letters else False, password)),
              any(map(lambda x: True if x in ascii_uppercase else False, password)),
              any(map(lambda x: True if x in ascii_lowercase else False, password)),
              any(map(lambda x: True if x.isdigit()  else False, password)),
             ]
    if all(result):
        return success(login)
    return failure(login,d.get(result.index(False)))



def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', '797777777777', success, failure)