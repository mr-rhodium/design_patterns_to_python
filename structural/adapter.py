

class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def switch_settings(self):
        return f'switch_settings'


class Tv:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def switch_channel(self):
        return f'{self.name} switch channel'


class Radio:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def switch_station(self):
        return f'{self.name} switch station'


class Microwave:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def power_mode(self):

        return f'{self.name} power mode'


class TechDevices:
    """this class adaptor"""

    def __init__(self, object, method):
        self.object = object
        self.__dict__.uptade(dict(method))

    def __str__(self):
        return self.object


if __name__ == '__main__':
    pass
