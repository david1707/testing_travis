class Worker:

    def __init__(self, _id, first_name, last_name, age, salary, position):
        self._id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary
        self.position = position

    def __repr__(self):
        return f'{self.__class__.__name__} ({self._id}, {self.first_name}, {self.last_name}, {self.age}, {self.salary}, {self.position})'

    def __str__(self):
        return f'{self.get_fullname()} works as a {self.position}'

    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'

    def yearly_salary_upgrade(self, upgrade_percentage=0.05):
        self.salary *= (1 + upgrade_percentage)
        print(f'{self.get_fullname()} pay upgraded to {self.salary}')

    def birthday(self):
        self.salary *= 1.01
        print(f'Happy birthday {self.get_fullname()}!')


