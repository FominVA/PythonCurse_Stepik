from collections import Counter, defaultdict

books = Counter(input().split(' '))
buyer = int(input())
income = 0
for num in range(buyer):
    book, price = input().split(' ')
    d ={}
    d[book] = d.get(book, 1)
    if books[book]:
        income+=int(price)
        books.subtract(d)
        print(books)