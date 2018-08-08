"""  Flyweight """

import abc

class Factory:

    def __init__(self):
        self._flyweight = {}

    def get_flyewight(self,key):

        if not self._flyweight.get(key, {}):
            flyewight = ConcreteFlyewight()
            self._flyweight.update({key:flyewight})
            return flyewight
        return self._flyweight.get(key, {})


class Flyweight():
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.state = None

    @abc.abstractmethod
    def operation(self,  extra_stat):
        pass

class ConcreteFlyewight(Flyweight):

    def operation(self, extra_stat):
        pass


def main():
    factory = Factory()
    for item in  ['cookies','data', 'flowers', 'keys']:
        concrete = factory.get_flyewight(item)
        concrete.operation(None)
        print(concrete)

if __name__ == '__main__':
    main()

