from collections import OrderedDict
from functools import reduce
from numbers import Number

import math

def vec2(x,y):
    return Vec(x=x, y=y)

def vec2proj(x,y,w=1):
    return Vec(x=x, y=y, w=w)

def vec3(x,y,z):
    return Vec(x=x, y=y, z=z)

def vec3proj(x,y,z,w=1):
    return Vec(x=x, y=y, z=z, w=w)

class Vec:
    def __init__(self, **val_dict):
        self.__dict__ = OrderedDict(val_dict)

    def __eq__(self, other):
        if isinstance(other, Vec):
            return self.__dict__ == other.__dict__
        return False

    def __getitem__(self, k):
        return self.__dict__[k]

    def keys(self):
        return tuple(self.__dict__.keys())

    def values(self):
        return tuple(self.__dict__.values())

    def __iter__(self):
        return iter(self.keys())

    def __str__(self):
        d = self.__dict__
        return str([d[k] for k in d])

    def __repr__(self):
        d = self.__dict__
        strs = ["{} = {}".format(k,d[k]) for k in d]
        out = reduce(lambda a, b: a + ", " + b, strs)
        return "<" + out + ">"

    def __add__(self, other):
        d0 = OrderedDict(self.__dict__)
        d1 = other.__dict__
        for k in d1:
            d0[k] = d0.get(k,0) + d1[k]
        return Vec(**d0)

    def __sub__(self, other):
        d0 = OrderedDict(self.__dict__)
        d1 = other.__dict__
        for k in d1:
            d0[k] = d0.get(k,0) - d1[k]
        return Vec(**d0)

    def __mul__(self, other):
        if isinstance(other, Number):
            return self.__mul_by_scalar(other)
        elif isinstance(other, Vec):
            d0 = self.__dict__
            d1 = other.__dict__
            out = 0
            for k in d0:
                out += d0[k]*d1[k]
            return out

    def __mul_by_scalar(self, c):
        d = OrderedDict(self.__dict__)
        for k in d:
            d[k] *= c
        return Vec(**d)

    def __rmul__(self, other):
        return self*other

    def l2(self):
        out = 0
        for v in self.values():
            out += v*v
        return math.sqrt(out)

    def max_len(self):
        lens = map(lambda x : len(str(x)), self.values())
        return reduce(max, lens)
