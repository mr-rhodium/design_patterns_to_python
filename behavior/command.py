"""This pattern design command is pattern
 create class sender and class recipient
  do not depend on each other directly.
  """


class TreatmentFile(object):
    def __init__(self, in_file, out_file):
        self._in_file = in_file
        self._out_file = out_file

    def sort_lines(self):
        """
        The file processing method
        :return:
        """
        print(f'sort lines in file {self._in_file} to file {self._out_file}')

    def reversed_lines(self):
        """
        The method revers lines in file
        :return:
        """
        print(f'revers lines in file {self._in_file} to file {self._out_file}')


class Exsecutor(object):
    def __init__(self):
        self._list_object = list()

    def add(self, command):
        self._list_object.append(command)

    def sort_lines(self):
        for item in self._list_object:
            item.sort_lines()

    def reversed_lines(self):
        for item in self._list_object:
            item.reversed_lines()


if __name__ == '__main__':
    obj_one = TreatmentFile('data.csv', 'data_2.csv')
    obj_two = TreatmentFile('name.txt', 'name_2.csv')

    run = Exsecutor()
    run.add(obj_one)
    run.add(obj_two)

    run.sort_lines()
    run.reversed_lines()
