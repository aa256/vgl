from .vector import Vec, vec2, vec2proj, vec3, vec3proj

from collections import OrderedDict
from functools import reduce
from numbers import Number

def mat2(xx,xy,yx,yy):
    return Mat(x=vec2(xx,xy), y=vec2(yx,yy))

def mat2proj(xx,xy,xw,yx,yy,yw,wx,wy,ww):
    return Mat(
    x=vec2proj(xx,xy,xw),
    y=vec2proj(yx,yy,yw),
    w=vec2proj(wx,wy,ww))

def mat3(xx,xy,xz,yx,yy,yz,zx,zy,zz):
    return Mat(x=vec3(xx,xy,xz), y=vec3(yx,yy,yz), z=vec3(zx,zy,zz))

def mat3proj(xx,xy,xz,xw,yx,yy,yz,yw,zx,zy,zz,zw,wx,wy,wz,ww):
    return Mat(
    x=vec3proj(xx,xy,xz,xw),
    y=vec3proj(yx,yy,yz,yw),
    z=vec3proj(zx,zy,zz,zw),
    w=vec3proj(wx,wy,wz,ww))

def mat32(xx, xy, xz, yx, yy, yz):
    return Mat(x=vec3(xx,xy,xz), y=vec3(yx,yy,yz))

class Mat:

    def __init__(self, **vecs_by_kw):
        self.__dict__ = OrderedDict(vecs_by_kw)

    def with_indices(xvars=None, yvars=None, *args):
        if xvars==None or yvars==None:
            return ValueError(
                "Need to set xvars and yvars as lists of distinct strings")
        m = len(xvars)
        n = len(yvars)
        if len(args) != m*n:
            return ValueError(
            "Need to pass m*n numerical args, where m")


    def __eq__(self, other):
        if isinstance(other, Mat):
            return self.__dict__ == other.__dict__
        return False

    def __getitem__(self, k):
        return self.__dict__[k]

    def keys(self):
        return tuple(self.__dict__.keys())

    def values(self):
        return tuple(self.__dict__.values())

    def __iter__(self):
        return iter(self.__dict)

    def __str__(self):
        d = self.__dict__
        out = ""
        first = True
        out = ""
        for k in d:
            if first:
                out += "["
                first = False
            else:
                out += ",\n "
            out += str(d[k])
        return out + "]"

    def __repr__(self):
        xkeys = self.keys()
        ykeys = self[xkeys[0]].keys()
        ell = self.max_len()
        rows = []
        row = [" "*2]
        row.extend(['{v:>{ell}}'.format(v=v, r=' ', ell=ell) for v in xkeys])
        rows.append(' '.join(row))
        for kx in xkeys:
            row = ['{v:>2}'.format(v=kx, r=' ')]
            row.extend(['{v:>{ell}}'.format(v=self[kx][ky], r=' ', ell=ell) for ky in ykeys])
            rows.append(' '.join(row))
        return "\n".join(rows)

    def __add__(self, other):
        out = dict(self.__dict__)
        for k in other:
            out[k] += other[k]
        return Mat(**other)

    def __sub__(self, other):
        out = dict(self.__dict__)
        for k in other:
            out[k] -= other[k]
        return Mat(**out)

    def __mul__(self, other):
        if isinstance(other, Number):
            return self.__mul_by_scalar(other)
        if isinstance(other, Vec):
            return self.__mul_by_vec(other)
        elif isinstance(other, Mat):
            return self.__mul_by_mat(other)
        return TypeError(
            "Mat does not support multiplication by {}".format(type(other)))

    def __mul_by_scalar(self, other):
        d = dict(self.__dict__)
        for k in d:
            d[k] *= other
        return Mat(**d)

    def __mul_by_vec(self, other):
        d = dict(self.__dict__)
        for k in d:
            d[k] *= other
        return Vec(**d)

    def __mul_by_mat(self, other):
        trans = +other
        kx = self.keys()
        ky = trans.keys()
        out = OrderedDict(self.__dict__)
        for x in kx:
            out[x] = dict()
            for y in ky:
                out[x][y] = self[x]*trans[y]
                print("ffff")
                print(self[x], trans[y], out[x][y])
            out[x] = Vec(**out[x])
        return Mat(**out)

    def __pos__(self):
        return self.transpose()

    def transpose(self):
        kx = self.keys()
        ky = self[kx[0]].keys()
        out = dict()
        for x in kx:
            out[x] = dict()
            for y in ky:
                out[x][y] = self[y][x]
            out[x] = Vec(**out[x])
        return Mat(**out)

    def max_len(self):
        return max(v.max_len() for v in self.values())
