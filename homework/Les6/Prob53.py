class Worker:
    name = None
    surname = None
    position = None
    _income = None

    def __init__(self, name, surname, position, wage=None, bonus=None):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Pos(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_position(self):
        return self.position

    def get_full_name(self):
        return self.surname + ', ' + self.name + ', ' + self.surname

    def get_his_income(self):
        return self._income.get('wage') + self._income.get('bonus')


John = Pos('John', 'Constantine', 'Exorcist', 29, 13)
print(John.get_full_name())
print(John.get_position())
print(f'{John.get_his_income()} silver coins')
