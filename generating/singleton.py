"""
Singleton - a pattern that generates objects.
Ensures that the class has only one instance.
Singleton allows you to implement patterns (abstract factory, builder, prototype)
"""
import six


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(
                *args, **kwargs)
        return cls._instances[cls]

# Python2


class TestClass():
    __metaclass__ = Singleton

    def add(self, args):
        return f'argument: {args} hash: {self.__hash__()}'

# Python3


class TestClass(metaclass=Singleton):
    def add(self, args):
        return f'argument: {args} hash: {self.__hash__()}'


if __name__ == '__main__':
    object_one = TestClass()
    object_two = TestClass()

    if six.PY2:
        # this is python2.x
        print(object_one.add("One"))
        print(object_two.add('Two'))
    else:
        # this id python3.x
        print(object_one.add("One"))
        print(object_two.add('Two'))
