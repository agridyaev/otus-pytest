import pytest
from collections import namedtuple

Person = namedtuple('Person', 'name age')

persons = [
    Person('John', 1982),
    Person('Mike', 1990)
]


def id_func(test_data):
    return [f'Person({p.name},{p.age})' for p in test_data]


@pytest.fixture(params=persons, ids=id_func(persons))
def person(request):
    return request.param


@pytest.mark.parametrize('a', [1, 2])
def test_names(person, a):
    assert isinstance(person.name, str)
    assert isinstance(person.age, int)
