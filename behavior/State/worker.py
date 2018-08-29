from state import State

class Transtction(State):

    def run(self) -> str:
        return f'Run {self.__class__.__name__}'

    def stop(self) -> str:
        return f'Stop {self.__class__.__name__}'

    def put(self) -> str:
        return f'Put {self.__class__.__name__}'

    def take(self) -> str:
        return f'Take {self.__class__.__name__}'

    def pause(self) -> str:
        return f'Pause {self.__class__.__name__}'

class Point(State):
    def run(self):
        return f'Run {self.__class__.__name__}'

    def stop(self):
        return f'Stop {self.__class__.__name__}'

    def put(self) -> str:
        return f'Put {self.__class__.__name__}'

    def pause(self) -> str:
        return f'Pause {self.__class__.__name__}'

    def take(self) -> str:
        return f'Take {self.__class__.__name__}'

class Runner:
   def __init__(self, state:State):
       self.state = state

   def chenge(self, state:State):
       self.state =  state

   def exe(self, method):
       exe_result = self._executor(method)
       return exe_result
   
   def _executor(self, method):
       text = getattr(self.state, method)
       return text


