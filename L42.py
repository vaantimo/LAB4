Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#B

import turtle
jack = turtle.Turtle()
jack.color("yellow")

for side in range(4):
...     if side == 3:
...         jack.color("yellow")
...     jack.forward(100)
...     jack.right(90)
... 
...     
>>> import turtle
>>> jack = turtle.Turtle()
>>> jack.color("yellow")
>>> 
>>> for side in range(4):
...     jack.forward(100)
...     jack.right(90)
...     if side == 3:
...         jack.color("purple")
... 
...         
>>> import turtle
>>> jack = turtle.Turtle()
>>> jack.color("yellow")
>>> 
>>> for side in range(4):
...     if side == 2:
...         jack.color("purple")
...     jack.forward(100)
...     jack.right(90)
... 
...     
>>> import turtle
>>> jack = turtle.Turtle()
>>> jack.color("yellow")
>>> 
>>> for side in range(4):
...     if side == 2:
...         jack.color("red")
...     jack.forward(100)
...     jack.right(90)
... 
...     
