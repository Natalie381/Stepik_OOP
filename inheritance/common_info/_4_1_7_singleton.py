class Singleton:
    _instance = None
    _instance_base = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if not cls._instance_base:
                cls._instance_base = object.__new__(cls)
            return cls._instance_base

        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance


class Game(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name


if __name__ == '__main__':
    game1 = Game('first')
    game2 = Game('second')
    print(id(game1), id(game2), game2.name)
