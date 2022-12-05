class Player:
    def __init__(self, name: str, old: int, score: int):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return self.score > 0


if __name__ == '__main__':
    lst_in = ['Балакирев; 34; 2048',
              'Mediel; 27; 0',
              'Влад; 18; 9012',
              'Nina P; 33; 0']
    players = []
    for line in lst_in:
        name, old, score = line.split('; ')
        players.append(Player(name, int(old), int(score)))
    players_filtered = [*filter(None, players)]
    print(players_filtered)