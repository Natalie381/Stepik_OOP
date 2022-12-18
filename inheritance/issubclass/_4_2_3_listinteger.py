class ListInteger(list):
    def _check_int(self, lst):
        if not all([isinstance(x, int) for x in lst]):
            raise TypeError('можно передавать только целочисленные значения')

    def __init__(self, lst):
        self._check_int(lst)
        super().__init__(*lst)

    def __setitem__(self, key, value):
        self._check_int(value)
        super().__setitem__(key,value)

    def append(self, obj):
        self._check_int(obj)
        super().append(obj)

