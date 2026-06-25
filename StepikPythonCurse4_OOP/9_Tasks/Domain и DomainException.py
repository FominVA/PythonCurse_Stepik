import re

class DomainException(Exception):
    pass

class Domain:
    DOMAIN_PATTERN = re.compile(r'^[A-Za-z]+\.[A-Za-z]+$')
    URL_PATTERN    = re.compile(r'^https?://[A-Za-z]+\.[A-Za-z]+$')
    EMAIL_PATTERN  = re.compile(r'^[A-Za-z]+@[A-Za-z]+\.[A-Za-z]+$')

    def __init__(self, domain):
        if not self.DOMAIN_PATTERN.fullmatch(domain):
            raise DomainException('Недопустимый домен, url или email')
        self.domain = domain

    @classmethod
    def from_url(cls, url: str) -> 'Domain':
        if  not cls.URL_PATTERN.fullmatch(url):
            raise DomainException('Недопустимый домен, url или email')
        domain = url.split("://", 1)[1]
        return cls(domain)

    @classmethod
    def from_email(cls, email: str) -> 'Domain':
        if not cls.EMAIL_PATTERN.fullmatch(email):
            raise DomainException('Недопустимый домен, url или email')
        domain = email.split("@", 1)[1]
        return cls(domain)

    def __str__(self) -> str:
        return self.domain

    def __repr__(self) -> str:
        return f'Domain("{self.domain}")'

try:
    domain1 = Domain('pygen..org')
except DomainException as e:
    print(e)
