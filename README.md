# Rotate outer layer of any square matrix clockwise and anticlockwise in any degree.

## How to use
```
>>> matrix = [['a', 'b', 'c'],\
          ['h', 'i', 'd'],\
          ['g', 'f', 'e']]

>>> rotated_matrix = rotate_outer_layer(matrix, degree=2, clockwise=True)

>>> rotated_matrix 
[['g', 'h', 'a'], ['f', 'i', 'b'], ['e', 'd', 'c']]

>>> rotated_matrix = matrix_rotation(matrix, degree=2, clockwise=True)

Original Matrix:
[['a', 'b', 'c'],
['h', 'i', 'd'],
['g', 'f', 'e']]

Clockwise Rotated Matrix with Degree = 2:
[['g', 'h', 'a'],
['f', 'i', 'b'],
['e', 'd', 'c']]
---------------------------------------------

>>> rotated_matrix
[['g', 'h', 'a'], ['f', 'i', 'b'], ['e', 'd', 'c']]
```

# Examples:
## Calling:
```
python3 -m doctest matrix_rotation.py
python3 matrix_rotation.py 
```
## Output
```
Original Matrix:
[['a', 'b'],
 ['d', 'c']]

Clockwise Rotated Matrix with Degree = 1:
[['d', 'a'],
 ['c', 'b']]
---------------------------------------------

Original Matrix:
[['a', 'b', 'c'],
 ['h', 'i', 'd'],
 ['g', 'f', 'e']]

Anitclockwise Rotated Matrix with Degree = 1:
[['b', 'c', 'd'],
 ['a', 'i', 'e'],
 ['h', 'g', 'f']]
---------------------------------------------

Original Matrix:
[['a', 'b', 'c', 'd'],
 ['l', 'i', 'd', 'e'],
 ['k', 'f', 'e', 'f'],
 ['j', 'i', 'h', 'g']]

Clockwise Rotated Matrix with Degree = 2:
[['k', 'l', 'a', 'b'],
 ['j', 'i', 'd', 'c'],
 ['i', 'f', 'e', 'd'],
 ['h', 'g', 'f', 'e']]
---------------------------------------------
```
