# Rotate any square matrix clockwise and anticlockwise in any degree.

## How to use
```
>>> matrix = [['a', 'b', 'c', 'd'],\
              ['l', 'm', 'n', 'e'],\
              ['k', 'p', 'o', 'f'],\
              ['j', 'i', 'h', 'g']]

>>> rotated_matrix = rotate_layers(matrix=matrix, degree=1, clockwise=True)

>>> rotated_matrix
[['l', 'a', 'b', 'c'], ['k', 'p', 'm', 'd'], ['j', 'o', 'n', 'e'], ['i', 'h', 'g', 'f']]

>>> matrix = [['a', 'b', 'c'],\
              ['h', 'i', 'd'],\
              ['g', 'f', 'e']]
    
>>> rotated_matrix = rotate_layers(matrix, degree=2, clockwise=True)

>>> rotated_matrix 
[['g', 'h', 'a'], ['f', 'i', 'b'], ['e', 'd', 'c']]

>>> rotated_matrix = matrix_rotation(matrix, degree=2, clockwise=True)
<BLANKLINE>
Original Matrix:
[['a', 'b', 'c'],
['h', 'i', 'd'],
['g', 'f', 'e']]
<BLANKLINE>
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
 ['l', 'm', 'n', 'e'],
 ['k', 'p', 'o', 'f'],
 ['j', 'i', 'h', 'g']]

Clockwise Rotated Matrix with Degree = 2:
[['k', 'l', 'a', 'b'],
 ['j', 'o', 'p', 'c'],
 ['i', 'n', 'm', 'd'],
 ['h', 'g', 'f', 'e']]
---------------------------------------------

Original Matrix:
[['a', 'b', 'c', 'd', 'e'],
 ['p', 'q', 'r', 's', 'f'],
 ['o', 'x', 'y', 't', 'g'],
 ['n', 'w', 'v', 'u', 'h'],
 ['m', 'l', 'k', 'j', 'i']]

Clockwise Rotated Matrix with Degree = 2:
[['o', 'p', 'a', 'b', 'c'],
 ['n', 'w', 'x', 'q', 'd'],
 ['m', 'v', 'y', 'r', 'e'],
 ['l', 'u', 't', 's', 'f'],
 ['k', 'j', 'i', 'h', 'g']]
---------------------------------------------

Original Matrix:
[['1', '2', '3', '4', '5', '6'],
 ['20', '21', '22', '23', '24', '7'],
 ['19', '32', '33', '34', '25', '8'],
 ['18', '31', '36', '35', '26', '9'],
 ['17', '30', '29', '28', '27', '10'],
 ['16', '15', '14', '13', '12', '11']]

Clockwise Rotated Matrix with Degree = 3:
[['18', '19', '20', '1', '2', '3'],
 ['17', '30', '31', '32', '21', '4'],
 ['16', '29', '34', '35', '22', '5'],
 ['15', '28', '33', '36', '23', '6'],
 ['14', '27', '26', '25', '24', '7'],
 ['13', '12', '11', '10', '9', '8']]
---------------------------------------------

Original Matrix:
[['1', '2', '3', '4', '5', '6', '7'],
 ['24', '25', '26', '27', '28', '29', '8'],
 ['23', '40', '41', '42', '43', '30', '9'],
 ['22', '39', '48', '49', '44', '31', '10'],
 ['21', '38', '47', '46', '45', '32', '11'],
 ['20', '37', '36', '35', '34', '33', '12'],
 ['19', '18', '17', '16', '15', '14', '13']]

Anitclockwise Rotated Matrix with Degree = 4:
[['5', '6', '7', '8', '9', '10', '11'],
 ['4', '29', '30', '31', '32', '33', '12'],
 ['3', '28', '45', '46', '47', '34', '13'],
 ['2', '27', '44', '49', '48', '35', '14'],
 ['1', '26', '43', '42', '41', '36', '15'],
 ['24', '25', '40', '39', '38', '37', '16'],
 ['23', '22', '21', '20', '19', '18', '17']]
---------------------------------------------
```
