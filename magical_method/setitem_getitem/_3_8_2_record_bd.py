class Record:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__dict__[key] = value
        self.keys = list(self.__dict__.keys())

    def _check(self, item):
        if not (isinstance(item, int) and 0 <= item <= len(self.keys)-1):
            raise IndexError('неверный индекс поля')

    def __getitem__(self, item):
        self._check(item)
        return self.__getattribute__(self.keys[item])

    def __setitem__(self, key, value):
        self._check(key)
        self.__setattr__(self.keys[key], value)

if __name__ == '__main__':
    r = Record(pk=1, title='Python ООП', author='Балакирев')
    print(r.pk, r.title, r.author)
    print(r[1])
    r[0] = 2  # доступ к полю pk
    r[1] = 'Супер курс по ООП'  # доступ к полю title
    r[2] = 'Балакирев С.М.'  # доступ к полю author
    print(r[1])  # Супер курс по ООП
    # r[3]  # генерируется исключение IndexError

