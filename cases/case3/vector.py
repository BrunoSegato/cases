from math import sqrt
from cases.case3.computed_property import computed_property


class Vector:
    def __init__(self, x, y, z, color=None):
        self.x, self.y, self.z = x, y, z
        self.color = color

    @computed_property('x', 'y', 'z')
    def magnitude(self):
        print('computing magnitude')
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def __repr__(self):
        return f'x: {self.x} y: {self.y} z: {self.z} color: {self.color} = magnitude: {self.magnitude}'
