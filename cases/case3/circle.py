from cases.case3.computed_property import computed_property


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    @computed_property('radius', 'area')
    def diameter(self):
        """Circle diameter from radius"""
        print('computing diameter')
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @diameter.deleter
    def diameter(self):
        self.radius = 0

    def __repr__(self):
        return f'Diameter: {self.diameter}'
