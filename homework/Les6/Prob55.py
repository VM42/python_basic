class Stationery:
    title = 'Title'

    def draw(self):
        print('Start drawing, ')
# wanted to use __init__ but realised that I don't have to=)


class Pen(Stationery):
    def draw(self):
        print('drawing with a pen.')


class Pencil(Stationery):
    def draw(self):
        print('drawing with a pencil. ')


class Sharpie(Stationery):
    def draw(self):
        print('drawing with my favorite Sharpie marker.')


my_pen = Pen()
my_penc = Pencil()
my_sharp = Sharpie()

my_pen.draw()
my_penc.draw()
my_sharp.draw()

# hope I got this one right as I am not sure if I have to call draw from Stat. class and if I have to Idk how
