class DataBase:
    def __init__(self, path: str):
        self.path = path
        self.dict_db = {}
        self.dick_pk = {}

    def write(self, record):
        '''Для добавления новой записи в БД, представленной объектом record'''
        self.dict_db.setdefault(record, []).append(record)
        self.dick_pk[record.pk] = record

    def read(self, pk):
        '''Чтение записи из БД (возвращает объект Record) по ее уникальному идентификатору pk'''
        return self.dick_pk.get(pk, 'Такого pk в базе данных нет')


class Record:
    RECORD_ID = 0
    @classmethod
    def __record_id(cls):
        cls.RECORD_ID += 1
        return cls.RECORD_ID

    def __init__(self, fio: str, descr: str, old: int):
        self.pk = self.__record_id()
        self.fio = fio
        self.descr = descr
        self.old = old

    def __hash__(self):
        return hash((self.fio, self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)


if __name__ == '__main__':
    lst_in = ['Балакирев С.М.; программист; 33',
              'Кузнецов Н.И.; разведчик-нелегал; 35',
              'Суворов А.В.; полководец; 42',
              'Иванов И.И.; фигурант всех подобных списков; 26',
              'Балакирев С.М.; преподаватель; 33'
              ]

    db = DataBase('my_path')
    for line in lst_in:
        fio, descr, old = [x for x in line.split((';'))]
        obj = Record(fio, descr, int(old))
        db.write(obj)

    db22345 = DataBase('123')
    r1 = Record('fio', 'descr', 10)
    r2 = Record('fio', 'descr', 10)
    assert r1.pk != r2.pk, "равные значения атрибута pk у разных объектов класса Record"

    db22345.write(r2)
    r22 = db22345.read(r2.pk)
    assert r22.pk == r2.pk and r22.fio == r2.fio and r22.descr == r2.descr and r22.old == r2.old, "при операциях write и read прочитанный объект имеет неверные значения атрибутов"

    assert len(db22345.dict_db) == 1, "неверное число объектов в словаре dict_db"

    fio = lst_in[0].split(';')[0].strip()
    v = list(db.dict_db.values())
    if fio == "Балакирев С.М.":
        assert len(v[0]) == 2 and len(v[1]) == 1 and len(v[2]) == 1 and len(
            v[3]) == 1, "неверно сформирован словарь dict_db"

    if fio == "Гейтс Б.":
        assert len(v[0]) == 2 and len(v[1]) == 2 and len(v[2]) == 1 and len(
            v[3]) == 1, "неверно сформирован словарь dict_db"
