import math
def n_length_vector(length,defaults=[],init=False):
  class _vector: 
    def __init__(self,*args):
      self.size = length
      self.value = []
      self.value.extend(expand_vectors(args))
      if len(self.value) != self.size:
        raise Exception(f'Can only specify {self.size} values for Vector[{self.size}], but {len(expand_vectors(args))} were given.')
        self = None
    def __repr__(self):
      return f'Vector{self.size}({str(self.value).strip("[]")})'
    __str__ = lambda s: s.__repr__()
    def __neg__(self):
      x = []
      for i in self.value:
        x.append(-i)
      return n_length_vector(len(x),defaults=x,init=True)
    def __pos__(self):
      x = []
      for i in self.value:
        x.append(abs(i))
      return n_length_vector(len(x),defaults=x,init=True)
    def __add__(self,other):
      if type(other) == int or type(other) == float:
        x = []
        for i in self.value:
          x.append(i+other)
        return n_length_vector(len(x),defaults=x,init=True)
      x = self.value.copy()
      while len(x) > len(self.value):
        x.append(0)
      for i in range(len(x)):
        try:
          x[i] += other.value[i]
        except:pass
      return n_length_vector(len(x),defaults=x,init=True)
    def __sub__(self,other):
      if type(other) == int or type(other) == float:
        x = []
        for i in self.value:
          x.append(i-other)
        return n_length_vector(len(x),defaults=x,init=True)
      x = self.value.copy()
      while len(x) < len(other.value):
        x.append(0)
      for i in range(len(x)):
        try:
          x[i] -= other.value[i]
        except:pass
      return n_length_vector(len(x),defaults=x,init=True)
    def __mul__(self,other):
      if type(other) == int or type(other) == float:
        x = []
        for i in self.value:
          x.append(i*other)
        return n_length_vector(len(x),defaults=x,init=True)
      x = self.value.copy()
      while len(x) < len(other.value):
        x.append(0)
      for i in range(len(x)):
        try:
          x[i] *= other.value[i]
        except:pass
      return n_length_vector(len(x),defaults=x,init=True)
    def __truediv__(self,other):
      if type(other) == int or type(other) == float:
        x = []
        for i in self.value:
          x.append(i/other)
        return n_length_vector(len(x),defaults=x,init=True)
      x = self.value.copy()
      while len(x) < len(other.value):
        x.append(0)
      for i in range(len(x)):
        try:
          x[i] /= other.value[i]
        except:pass
      return n_length_vector(len(x),defaults=x,init=True)
    def __floordiv__(self,other):
      if type(other) == int or type(other) == float:
        x = []
        for i in self.value:
          x.append(i//other)
        return n_length_vector(len(x),defaults=x,init=True)
      x = self.value.copy()
      while len(x) < len(other.value):
        x.append(0)
      for i in range(len(x)):
        try:
          x[i] //= other.value[i]
        except:pass
      return n_length_vector(len(x),defaults=x,init=True)
    def __mod__(self,other):
      if type(other) == int or type(other) == float:
        x = []
        for i in self.value:
          x.append(i%other)
        return n_length_vector(len(x),defaults=x,init=True)
      x = self.value.copy()
      while len(x) < len(other.value):
        x.append(0)
      for i in range(len(x)):
        try:
          x[i] %= other.value[i]
        except:pass
      return n_length_vector(len(x),defaults=x,init=True)
    def __pow__(self,other):
      if type(other) == int or type(other) == float:
        x = []
        for i in self.value:
          x.append(i**other)
        return n_length_vector(len(x),defaults=x,init=True)
      x = self.value.copy()
      while len(x) < len(other.value):
        x.append(0)
      for i in range(len(x)):
        try:
          x[i] **= other.value[i]
        except:pass
      return n_length_vector(len(x),defaults=x,init=True)
    def __lshift__(self,other):
      if type(other) == int or type(other) == float:
        x = []
        for i in self.value:
          x.append(i<<other)
        return n_length_vector(len(x),defaults=x,init=True)
      x = self.value.copy()
      while len(x) < len(other.value):
        x.append(0)
      for i in range(len(x)):
        try:
          x[i] <<= other.value[i]
        except:pass
      return n_length_vector(len(x),defaults=x,init=True)
    def __rshift__(self,other):
      if type(other) == int or type(other) == float:
        x = []
        for i in self.value:
          x.append(i>>other)
        return n_length_vector(len(x),defaults=x,init=True)
      x = self.value.copy()
      while len(x) < len(other.value):
        x.append(0)
      for i in range(len(x)):
        try:
          x[i] >>= other.value[i]
        except:pass
      return n_length_vector(len(x),defaults=x,init=True)
    def __and__(self,other):
      if type(other) == int or type(other) == float:
        x = []
        for i in self.value:
          x.append(i&other)
        return n_length_vector(len(x),defaults=x,init=True)
      x = self.value.copy()
      while len(x) < len(other.value):
        x.append(0)
      for i in range(len(x)):
        try:
          x[i] &= other.value[i]
        except:pass
      return n_length_vector(len(x),defaults=x,init=True)
    def __or__(self,other):
      if type(other) == int or type(other) == float:
        x = []
        for i in self.value:
          x.append(i|other)
        return n_length_vector(len(x),defaults=x,init=True)
      x = self.value.copy()
      while len(x) < len(other.value):
        x.append(0)
      for i in range(len(x)):
        try:
          x[i] |= other.value[i]
        except:pass
      return n_length_vector(len(x),defaults=x,init=True)
    def __xor__(self,other):
      if type(other) == int or type(other) == float:
        x = []
        for i in self.value:
          x.append(i^other)
        return n_length_vector(len(x),defaults=x,init=True)
      x = self.value.copy()
      while len(x) < len(other.value):
        x.append(0)
      for i in range(len(x)):
        try:
          x[i] ^= other.value[i]
        except:pass
      return n_length_vector(len(x),defaults=x,init=True)
    def __invert__(self):
      x = self.value.copy()
      for i in range(len(x)):
        try:
          x[i] = ~x[i]
        except:pass
      return n_length_vector(len(x),defaults=x,init=True)
    def __abs__(self):
      x = self.value.copy()
      for i in range(len(x)):
        try:
          x[i] = abs(x[i])
        except:pass
      return n_length_vector(len(x),defaults=x,init=True)
    def __round__(self,length):
      x = self.value.copy()
      for i in range(len(x)):
        try:
          x[i] = round(x[i],length)
        except:pass
      return n_length_vector(len(x),defaults=x,init=True)
    def __floor__(self):
      x = self.value.copy()
      for i in range(len(x)):
        try:
          x[i] = math.floor(x[i])
        except:pass
      return n_length_vector(len(x),defaults=x,init=True)
    def __ceil__(self):
      x = self.value.copy()
      for i in range(len(x)):
        try:
          x[i] = math.ceil(x[i])
        except:pass
      return n_length_vector(len(x),defaults=x,init=True)
    def __trunc__(self):
      x = self.value.copy()
      for i in range(len(x)):
        try:
          x[i] = math.trunc(x[i])
        except:pass
      return n_length_vector(len(x),defaults=x,init=True)
    def __getitem__(self,item):
      return self.value[item]
    def __setitem__(self,item,value):
      self.value[item] = value
    def __iter__(self):
      return iter(self.value.copy())
    @property
    def x(self):
      return self.value[0]
    @x.setter
    def set_x(self,value):
      self.value[0] = value
    @property
    def y(self):
      return self.value[1]
    @y.setter
    def set_y(self,value):
      self.value[1] = value
    @property
    def z(self):
      return self.value[2]
    @z.setter
    def set_z(self,value):
      self.value[2] = value
  if init:
    return _vector(*defaults)
  return _vector
class _vectorPrefix:
  def __getitem__(self,slice):
    if not str(slice).isdigit():
      raise SyntaxError(f'Unexpected "{slice}"')
      return None
    return n_length_vector(length=int(slice),init=False)
def expand_vectors(array):
  out = []
  for i in array:
    if not type(i).__name__ == '_vector':
      out.append(i)
    else:
      for j in i:
        out.append(j)
  return out
Vector = _vectorPrefix()
__all__ = ["Vector","expand_vectors"]
