from operator import itemgetter

class Clock (object):

    def __init__ (self,time):
      self._current = time
      self._functions = []
      
    def register(self,priority,f):
      self._functions.append((priority, f))
      self._functions = sorted(self._functions, key=itemgetter(0))
      
    def tick(self):
      self._current += 1
      for func in self._functions:
        func[1](self._current)