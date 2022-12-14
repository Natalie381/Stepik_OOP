class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self._attrs = tuple(self.__dict__)
        self._len_atrs = len(self._attrs)
        self._iter_ind = -1

    def check_ind(self, indx):
        if not (isinstance(indx, int) and 0 <= indx <= 4):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check_ind(item)
        return self.__getattribute__(self._attrs[item])

    def __setitem__(self, key, value):
        self.check_ind(key)
        self.__setattr__(self._attrs[key], value)

    def __next__(self):
        if self._iter_ind>=4:
            self._iter_ind += 1
            return self.__getattribute__(self._attrs[self._iter_ind])
        raise StopIteration

    def __iter__(self):
        self._iter_ind = -1
        return self


if __name__ == '__main__':
    pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
    pers[0] = 'Балакирев С.М.'
    for v in pers:
        print(v)
    # pers[5] = 123  # IndexError
