from operator import itemgetter
import uuid

class Clock (object):
    clocks = []
    def __init__ (self,time):
      self._current = time
      self._functions = []
      Clock.clocks.append(self)
      
    def register(self,priority,f, id):
      self._functions.append((priority, f, id))
      self._functions = sorted(self._functions, key=itemgetter(0))
      
    def tick(self):
      self._current += 1
      for func in self._functions:
        func[1](self._current)

    def unregister(self,id):
      for i, (priority, f, uuid) in enumerate(self._functions):
        if uuid == id:
          del self._functions[i]