class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None



class Stack:
    def __init__(self):
        self.top = None
        self.last = None
        self.__len = 0

    def __iter__(self):
        self._iter = self.top
        return self

    def __next__(self):
        if self._iter == self.top:
            self._iter = self._iter.next
            return self.top
        elif self._iter!=self.last:
            self._iter = self._iter.next
            return self._iter
        raise StopIteration

    def push_back(self, obj):
        if not self.top:
            self.top = obj
            self.last = obj
        else:
            self.last.next = obj
            self.last = obj
        self.__len += 1

    def push_front(self, obj):
        if not self.top:
            self.top = obj
            self.last = obj
        else:
            obj.next = self.top
            self.top = obj
        self.__len += 1


    def pop(self):
        temp = self.top
        while temp and temp.next != self.last:
            temp = temp.next
        temp, self.last = self.last, temp
        if self.last:
            self.last.next = None
        self.__len -= 1
        return temp

    def check(self, value):
        if not (isinstance(value, int) and 0 <= value < self.__len):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check(item)
        answer = self.top
        for _ in range(item):
            answer = answer.next
        return  answer.data

    def __setitem__(self, key, value):
        self.check(key)
        answer = self.top
        for _ in range(key):
            answer = answer.next
        answer.data = value.data

    def __len__(self):
        return self.__len


    def __add__(self, other):
        self.push(other)
        return self

    def __iadd__(self, other):
        self.push(other)
        return self

    def __mul__(self, other):
        for i in other:
            i = StackObj(i)
            self.push(i)
        return self

    def __imul__(self, other):
        return self * other

    def get_data(self):
        if not self.top:
            return []
        temp = self.top
        otvet = []
        while temp:
            otvet.append(temp.data)
            temp = temp.next
        print(otvet)

if __name__ == '__main__':
    st = Stack()
    st.push_back(StackObj("obj1"))
    st.push_front(StackObj("obj2"))
    st.push_back(StackObj("obj3"))
    st[1] = StackObj("new obj2")
    print(st[2])  # obj3
    print(st[1])  # new obj2
    # res = st[3]  # исключение IndexError

    n = len(st)  # получение общего числа объектов стека

    for obj in st:  # перебор объектов стека (с начала и до конца)
        print(obj.data)