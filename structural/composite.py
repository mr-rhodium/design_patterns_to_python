#!/usr/bin/env python
"""
Composite - pattern structuring objects
"""
from abc import ABCMeta, abstractmethod


class Unit(metaclass=ABCMeta):
    """ Abstract class"""

    @abstractmethod
    def show_unit(self)-> str:
        """Mhetod to reload, print info to unit """


class Box(Unit):
    """Unit Box"""

    def show_unit(self)-> str:
        return f'Box  => '


class Block(Unit):
    """Unit Block"""

    def show_unit(self)-> str:
        return 'Block  => '


class Detail(Unit):
    """Unit Detali"""

    def show_unit(self)-> str:
        return 'Detali  => '


class Сontainer(Unit):
    """Сontainer Unit"""

    def show_unit(self)-> str:
        return 'Сontainer  => '


class ReportStok(Unit):
    """
    Class composer
    :param unit: objact classa unit
    """

    def __init__(self):
        self._report = []

    def show_unit(self):
        counter = {}
        for item in self._report:
            class_name = item.__class__.__name__
            if not counter.get(class_name):
                counter.setdefault(class_name, 1)
            else:
                value = counter.get(class_name)
                counter.update({class_name: value + 1})
        for key, value in counter.items():
            info = f'{key} there is {value} in stock {self.__hash__()}'
            print(info)

    def add(self, unit: Unit):
        self._report.append(unit)
        info = f'{unit.show_unit()} add to stock {self.__hash__()}'
        print(info)

    def delete(self, unit: Unit):
        """
        Deleted unit whis stock
        :param unit: objact classa unit
        """
        for item in self._report:
            if item == unit:
                self._report.remove(unit)
                info = f'{unit.show_unit()} deleted whis stock {self.__hash__()}'
        else:
            info = f'{unit.show_unit()} not found in stock {self.__hash__()}'
            print(info)


if __name__ == '__main__':

    report = ReportStok()

    obj_1 = Box()
    obj_2 = Box()
    obj_3 = Block()
    obj_4 = Block()
    obj_5 = Detail()
    obj_6 = Detail()
    obj_7 = Сontainer()
    obj_8 = Сontainer()

    print('Add \n')

    report.add(obj_1)
    report.add(obj_2)
    report.add(obj_3)
    report.add(obj_4)
    report.add(obj_5)
    report.add(obj_6)
    report.add(obj_7)
    report.add(obj_8)

    print('\nDeleted \n')

    report.delete(obj_4)
    report.delete(obj_8)

    print('\nShow all count \n')

    report.show_unit()
