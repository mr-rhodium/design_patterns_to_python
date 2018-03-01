"""This Adapter pattern example"""


class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def switch_settings(self):
        return f'switch settings'


class Tv:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def switch_channel(self):
        return f'switch channel'


class Radio:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def switch_station(self):
        return f'switch station'


class Microwave:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def power_mode(self):

        return f'power mode'


class TechDevices:
    """this class adaptor"""

    def __init__(self, object, method):
        self.object = object
        self.__dict__.update(method)

    def __str__(self):
        return str(self.object)


if __name__ == '__main__':
    list_objects = []
    object_computer = Computer('Notebook')
    object_tv = Tv('Home Tv')
    object_radio = Radio('Radio receivers')
    object_microwave = Microwave('Stove')

    list_objects.append(
        TechDevices(
            object_computer, dict(
                switch=object_computer.switch_settings)))

    list_objects.append(
        TechDevices(
            object_tv, dict(
                switch=object_tv.switch_channel)))

    list_objects.append(
        TechDevices(
            object_radio, dict(
                switch=object_radio.switch_station)))
    
    list_objects.append(
        TechDevices(
            object_microwave, dict(
                switch=object_microwave.power_mode)))

    for item in list_objects:
        print(f'{item} {item.switch()}')
