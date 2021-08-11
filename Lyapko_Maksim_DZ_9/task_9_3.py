saliry = {'wage':6000,
          'bonus':30000}
class Worker:
    name = 'Maksim'
    surname = 'Alekseevich'
    position = 'Programmer'
    _income = saliry['wage'] + saliry['bonus']

class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname} {self.position}')

    def get_total_income(self):
        print(self._income)
a = Position()
a.get_full_name()
a.get_total_income()