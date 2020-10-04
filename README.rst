# Rotate any square matrix clockwise and anticlockwise in any degree.
```matrix-rotation``` is a simple package for rotating elements of any square matrix in clockwise and anticlockwise direction. This rotation can be performed with any degree or step size. It is most suitable for small size matrix. 

## How to use
Following are some of the sample examples to show the use of ```matrix_rotation``` package. This package has a function named ```rotate_matrix``` which essentially takes input 2 dimensional square ```matrix``` as a first argument, ```degree``` as a second argument to determine the step size and default ```clockwise``` rotation as the final argument. ```print_rotate_matrix``` function is just the extension of ```rotate_matrix``` function which print the original matrix and rotated matrix on the console. Let's take a look.
```
>> from matrix_rotation import rotate_matrix, print_rotate_matrix

>>> matrix = [['a', 'b', 'c'],\
              ['h', 'i', 'd'],\
              ['g', 'f', 'e']]
    
>>> rotated_matrix = rotate_matrix(matrix, degree=2, clockwise=True)

>>> rotated_matrix 
[['g', 'h', 'a'], ['f', 'i', 'b'], ['e', 'd', 'c']]

>>> rotated_matrix = print_rotate_matrix(matrix, degree=2, clockwise=True)

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

## Examples:

### Calling python package
```matrix-rotation``` can be directly called using ```python3``` to work with commond line interface.
```
python3 matrix-rotation
```

### Calling from Command Line Interface (CLI)
```
python3 matrix_rotation/matrix_rotation_cli.py --matrix "[['a', 'b'],['d', 'c']]"

python3 matrix_rotation/matrix_rotation_cli.py --matrix "[['a', 'b'],['d', 'c']]" --degree 1 

python3 matrix_rotation/matrix_rotation_cli.py --matrix "[['a', 'b'],['d', 'c']]" --degree 1 --clockwise False

python3 matrix_rotation/matrix_rotation_cli.py --matrix "[['a', 'b'],['d', 'c']]" --degree 1 --clockwise False --print_matrix True

```

### Calling for doctest:
```
python3 -m doctest matrix_rotation/matrix_rotation.py
```

### Calling for unittest
```
python3 -m unittest discover
python3 -m pytest 
```

# Licence
MIT License

Note: If you find this project useful, please include reference link in your work.
