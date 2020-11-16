class Road:
    _length = None
    _width = None
    thickness = 0.01

# and for thickness 1cm is given
    def __init__(self, length, width, thickness):
        self.width = width
        self.length = length
        self.thickness = thickness

# as mass of 1m^3 of asphalt = 1100~1500kg, was decided to take app.num. 1300kg for 1m^3

    def weight(self):

        cubic_meters = self.width * self.length * self.thickness
        total_weight = cubic_meters * 1300
        print(f'{total_weight} tons are needed to build your own way.')


MyWay = Road(4200, 6.9, 0.01)
MyWay.weight()
