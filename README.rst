# Rotate any square matrix clockwise and anticlockwise in any degree of angle.
```matrix-rotation``` is a simple package for rotating elements of any square matrix in clockwise and anticlockwise direction. This rotation can be performed with any degree of angle or step size. This version is most suitable for small size matrix. 

## How to install the package
```
pip install matrix-rotation
```

## How to use it in python code
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

## How to use from command line interface

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

### Calling for python package
```matrix_rotation``` can be directly called without using ```python3``` to work with command line interface.

#### Calling with --matrix or -M
Here default arguments will be ```degree=1, clockwise=True, print_matrix=False```
```
matrix_rotation --matrix "[['a', 'b'], ['d', 'c']]"
matrix_rotation -M "[['a', 'b'], ['d', 'c']]"
```

#### Calling with --matrix or -M and degree or -D
Here default arguments will be ```clockwise=True, print_matrix=False```
```
matrix_rotation --matrix "[['a', 'b'], ['d', 'c']]" --degree 2
matrix_rotation -M "[['a', 'b'], ['d', 'c']]" -D 2
```

#### Calling with --matrix or -M, degree or -D and clockwise or -C 
Here default arguments will be ```print_matrix=False```
```
matrix_rotation --matrix "[['a', 'b'], ['d', 'c']]" --degree 2 --clockwise False
matrix_rotation -M "[['a', 'b'], ['d', 'c']]" -D 2
```

#### Calling with --matrix or -M, degree or -D, clockwise or -C and --print_matrix or -S
```
matrix_rotation --matrix "[['a', 'b'], ['d', 'c']]" --degree 2 --clockwise False --print_matrix True
matrix_rotation -M "[['a', 'b'], ['d', 'c']]" -D 2 -S True
```

### Calling for doctest:
```
python3 -m doctest matrix_rotation/matrix_rotation.py
```

### Calling for sample examples
Use the following command to run sample examples from command line interface:
```
matrix_rotation
```
This command will prompt a message in the console. If you want to run sample examples just type ```None``` in the console.
```
Type "None" to display default examples.
Enter your matrix: <None>
```

Use the following command to run sample examples in the python code:
```
>>> from matrix_rotation import examples
>>> examples()
```

### Output of above sample examples
```
Original Matrix:
[['a', 'b'],
['d', 'c']]

Clockwise Rotated Matrix with Degree = 1:
[['d', 'a'],
 ['c', 'b']]
---------------------------------------------

Original Matrix:
[['a', 'b'],
 ['d', 'c']]

Anitclockwise Rotated Matrix with Degree = 1:
[['b', 'c'],
 ['a', 'd']]
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
# License
MIT License
