class BookStudy:
    def __init__(self, name: str, author: str, year: int):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name, self.author))

    def __eq__(self, other):
        return hash(self) == hash(other)


if __name__ == '__main__':
    lst_in = [
        'Python; Балакирев С.М.; 2020',
        'Python ООП; Балакирев С.М.; 2021',
        'Python ООП; Балакирев С.М.; 2022',
        'Python; Балакирев С.М.; 2021',
    ]
    lst_bs = []
    for line in lst_in:
        name, author, year = line.split('; ')
        book = BookStudy(name, author, int(year))
        lst_bs.append(book)

    unique_books = len(set(lst_bs))
    print(unique_books)
