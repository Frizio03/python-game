class World:
  def __init__(self, level_numeber, w, h):
    self.level_numeber = level_numeber
    self.w = w
    self.h = h

  def draw(self, *n_entities):
    print()
    print("LEVEL N.", self.level_numeber)
    print()
    for y in range(self.h):
      for x in range(self.w):
        for ent in n_entities:
          if (ent.x - 1) == x and (ent.y - 1) == y:
            print("[{}]".format(ent.graphic), end="")
            break
        else:
          print("[ ]", end="")
      print()

class Entity:
  def __init__(self, x, y, graphic):
    self.x = x
    self.y = y
    self.graphic = graphic


e = Entity(5, 5, "X")
e2 = Entity(7, 6, "Y")
world = World(1, 10, 10)

world.draw(e, e2)

print()