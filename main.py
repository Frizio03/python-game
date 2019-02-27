class World:
  def __init__(self, level_numeber, larghezza, altezza):
    self.level_numeber = level_numeber
    self.larghezza = larghezza
    self.altezza = altezza

  def create(self):
    print()
    print("LEVEL N.", self.level_numeber)
    print()
    for y in range(self.altezza):
      for x in range(self.larghezza):
        if e.x == x and e.y == y:
          print("[{}]".format(e.graphic), end="")
        else:
          print("[ ]", end="")

class Entity:
  def __init__(self, x, y, graphic):
    self.x = x
    self.y = y
    self.graphic = graphic


e = Entity(5, 5, "X")
world = World(1, 10, 10)

world.create()

print()