from Worker import Worker


def test_worker_creation():
    my_worker = Worker(3, 'David', 'Membrives', 34, 10000, 'Developer')
    assert my_worker.first_name == 'David'
    assert my_worker.last_name == 'Membrives'
    assert my_worker._id == 3
    assert my_worker.age == 34
    assert my_worker.salary == 10000
    assert my_worker.position == 'Developer'


def test_worker_get_fullname():
    my_worker = Worker(3, 'David', 'Membrives', 34, 10000, 'Developer')
    assert my_worker.get_fullname() == 'David Membrives'


def test_yearly_salary_upgrade_default():
    my_worker = Worker(3, 'David', 'Membrives', 34, 10000, 'Developer')
    assert my_worker.salary == 10000
    my_worker.yearly_salary_upgrade()
    assert my_worker.salary == 10500


def test_yearly_salary_upgrade():
    my_worker = Worker(3, 'David', 'Membrives', 34, 10000, 'Developer')
    assert my_worker.salary == 10000
    my_worker.yearly_salary_upgrade(0.1)
    assert my_worker.salary == 11000


def test_birthday():
    my_worker = Worker(3, 'David', 'Membrives', 34, 10000, 'Developer')
    assert my_worker.salary == 10000
    my_worker.birthday()
    assert my_worker.salary == 10100


def test_dunder_str():
    my_worker = Worker(3, 'David', 'Membrives', 34, 10000, 'Developer')
    assert my_worker.__str__() == 'David Membrives works as a Developer'


def test_dunder_repr():
    my_worker = Worker(3, 'David', 'Membrives', 34, 10000, 'Developer')
    assert my_worker.__repr__() == 'Worker (3, David, Membrives, 34, 10000, Developer)'
