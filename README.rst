# Rotate any square matrix clockwise and anticlockwise in any degree of angle.
```matrix-rotation``` is a simple package for rotating elements of any square matrix in clockwise and anticlockwise direction. This rotation can be performed with any degree of angle or step size. This version is most suitable for small size matrix. 

## Use in python code
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

## Use from command line interface

### ```matrix_rotation --help```
```
Usage: matrix_rotation [OPTIONS]

Options:
  -M, --matrix TEXT           Use to show default examples of matrix rotation.
                              Otherwise use the input matrix from command
                              line. Input example : [["a", "b"],["d", "c"]]

  -D, --degree INTEGER        Degree of rotation. Can rotate matrix in between
                              0 degree to 360 degree.  [default: (1)]

  -C, --clockwise BOOLEAN     Use True to rotate matrix in a clockwise
                              direction. False for rotation in anticlockwise
                              direction.  [default: (True)]

  -S, --print_matrix BOOLEAN  Use True to show the result of Original and
                              Rotated Matrix.  [default: (False)]

  --help                      Show this message and exit.
```
For more information please visit [GitHub](https://github.com/vhiwase/matrix-rotation/ "Github Link")

# License
MIT License
