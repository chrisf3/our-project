#oop first classes example
class cat:
  def __init__(self, name, owner, color):
    self.name = name
    self.owner = owner
    self.color = color
cat_1=cat('Clocharde','Hannah','multicolored')
cat_2=cat('Leia','Paula','orange')


print(cat_1.color)
