import sys
import math


class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.lines = []


class Player:
    def __init__(self, score):
        self.score = score
        self.pacs = []


class Pellet:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value


class Pacman:
    def __init__(self, p_id, mine, x, y, type_id, turns, cooldown):
        self.p_id = int(p_id)
        self.mine = int(mine)
        self.x = int(x)
        self.y = int(y)
        self.type_id = type_id
        self.turns = turns
        self.cooldown = cooldown

    def move(self):
        return 'MOVE 0 15 10'


class Game:
    def __init__(self, player, enemy, grid):
        self.player = player
        self.enemy = enemy
        self.grid = grid
        self.pellets = []


# Grab the pellets as fast as you can!

# width: size of the grid
# height: top left corner is (x=0, y=0)
width, height = [int(i) for i in input().split()]
my_grid = Grid(rows=height, cols=width)
for i in range(height):
    my_grid.lines.append(list(input()))
# game loop
while True:
    my_score, opponent_score = [int(i) for i in input().split()]
    visible_pac_count = int(input())  # all your pacs and enemy pacs in sight
    player = Player(my_score)
    enemy = Player(opponent_score)
    game = Game(player, enemy, grid=my_grid)
    for i in range(visible_pac_count):
        # pac_id: pac number (unique within a team)
        # mine: true if this pac is yours
        # x: position in the grid
        # y: position in the grid
        # type_id: unused in wood leagues
        # speed_turns_left: unused in wood leagues
        # ability_cooldown: unused in wood leagues
        pac = Pacman(*input().split())
        if pac.mine == 1:
            player.pacs.append(pac)
        else:
            enemy.pacs.append(pac)
    visible_pellet_count = int(input())  # all pellets in sight
    for i in range(visible_pellet_count):
        # value: amount of points this pellet is worth
        pellet = Pellet(*[int(j) for j in input().split()])
        game.pellets.append(pellet)
    for k, p in enumerate(player.pacs):
        if k == 0:
            print(f'{p.move()}', end='')
        else:
            print(f' | {p.move()}', end='')
    print()
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # MOVE <pacId> <x> <y>
    # print("MOVE 0 15 10")
