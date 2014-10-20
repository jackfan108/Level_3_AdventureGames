from operator import itemgetter

class Clock (object):

    def __init__ (self,time):
      self._current = time
      self._functions = []
      
    def register(self,f,priority):
      self._functions.append((f, priority))
      self._functions = sorted(self._functions, key=itemgetter(1))
      
    def tick(self):
      self._current += 1
      for func in self._functions:
        func[1](self._current)
      

    # FIX ME
