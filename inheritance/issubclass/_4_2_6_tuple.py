class IterAttrs:
    def __iter__(self):
        return ((k, self.__getattribute__(k)) for k in self.__dict__)


class SmartPhone(IterAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory

if __name__ == '__main__':
    phone = SmartPhone(123, 234, 545)
    for attr, value in phone:
        print(attr, value)
