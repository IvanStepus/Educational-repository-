class WinDoor:
  def __init__(self, x, y, name="unk"):
    self.x = x
    self.y = y
    self.name = name
    self.square = x * y

  def __repr__(self):
    return f'{self.name} {self.x}x{self.y}'

class Room:
  def __init__(self, width, length, height):
    self.width = width
    self.length = length
    self.height = height
    self.wd = []

  def addWD(self, w, h, name='unk'):
    self.wd.append(WinDoor(w, h, name))

  def calc_wallpaper_area(self):
    new_square = 2 * (self.height * self.length + self.height * self.width)
    for i in self.wd:
      new_square -= i.square
    return new_square

  def calc_wallpaper_rolls(self, roll_length, roll_width):
    area = self.calc_wallpaper_area()
    return area / (roll_length * roll_width)


width = float(input('Введите ширину комнаты, м: '))
length = float(input('Введите длину комнаты, м: '))
height = float(input('Введите высоту комнаты, м: '))

room = Room(width, length, height)

while True:
  answer = input('Хотите добавить дверь или окно (y/n)? ')
  if answer == 'y':
    type_wd = input('Это дверь или окно (d/w)? ')
    if type_wd == 'd':
      name = input('Введите название 🚪: ')
    else:
      name = input('Введите название 🪟: ')
    width_wd = float(input(f'Введите ширину {name}, м: '))
    height_wd = float(input(f'Введите высоту {name}, м: '))
    room.addWD(width_wd, height_wd, name)
  else:
    break

roll_length = float(input("Введите длину рулона обоев, м: "))
roll_width = float(input("Введите ширину рулона обоев, м: "))

area = room.calc_wallpaper_area()
rolls = room.calc_wallpaper_rolls(roll_length, roll_width)

print(f'Площадь оклеиваемой поверхности: {area} м^2')
print(f"Количество необходимых рулонов: {rolls} шт.")