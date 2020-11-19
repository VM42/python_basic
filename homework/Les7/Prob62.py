# "Schneiderei" solution

class Cloth:
    def __init__(self, height, size):
        self.height = height
        self.size = size

    def coat_mat(self):
        return self.size / 6.5 + 0.5

    def suit_mat(self):
        return self.height * 2 + 0.3

    @property
    def get_total_material(self):
        total_mat = round((self.size/ 6.5 + 0.5) + (self.height * 2 + 0.3))
        return str(f'Total amount of spent material: {total_mat}m.')

# stuck  for a little bit on way of noramly rounding numbers, don't want to double code =(


class Coat(Cloth):
    def __init__(self, height, size):
        super().__init__(height, size)
        self.coat_mat = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'{self.coat_mat}m of material was spent on your nice coat.'


class Suit(Cloth):
    def __init__(self, height, size):
        super().__init__(height, size)
        self.suit_mat = round(self.height / 6.5 + 0.5)

    def __str__(self):
        return f'{self.suit_mat}m of material was spent on your cool suit.'


NiceCoat = Coat(190, 10)
CoolSuit = Suit(190, 10)
print(NiceCoat)
print(CoolSuit)
print(Cloth.get_total_material)




