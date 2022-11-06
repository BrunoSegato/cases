from cases.case3.vector import Vector
from cases.case3.circle import Circle

print('Circle \n')

c = Circle()
print(f'Getter {c.diameter}')
c.diameter = 3
print(f'Setter {c.radius}')
del c.diameter
print(f'Deleter {c.radius}')
help(Circle)

print('\n\n\n Vector \n\n\n')

v = Vector(9, 2, 6)
print(v.magnitude)
v.color = 'red'
print(v.magnitude)
v.color = 'green'
print(v.magnitude)
v.y = 18
print(v.magnitude)
v.color = 'black'
print(v.magnitude)
v.x = 2
print(v.magnitude)
