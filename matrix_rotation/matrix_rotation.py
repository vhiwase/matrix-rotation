import itertools

__all__ = ["rotate_matrix", "print_rotate_matrix", "pprint", "printing"]


def rotate_matrix(matrix: list, degree: int, clockwise: bool = True) -> list:
    """
    Generalize function to rotate any matrix's outer layer clockwise and
    anticlockwise'

    Parameters
    ----------
    matrix : list
        Input square matrix.
    degree : int
        Degree of rotation.
    clockwise : TYPE, optional
        Direction of rotation. The default is True.
        True for clockwise direction
        False for anticlockwise direction

    Returns
    -------
    rotated_matrix : list
        Rotated square matrix

    >>> matrix = [['a', 'b', 'c', 'd'],\
                  ['l', 'm', 'n', 'e'],\
                  ['k', 'p', 'o', 'f'],\
                  ['j', 'i', 'h', 'g']]

    >>> rotated_matrix = rotate_matrix(matrix=matrix, degree=1, clockwise=True)

    >>> rotated_matrix
    [['l', 'a', 'b', 'c'], ['k', 'p', 'm', 'd'], ['j', 'o', 'n', 'e'], ['i', 'h', 'g', 'f']]
    """

    # Getting matrix's positional index and its value
    pos_dict = {}
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            pos_dict[(row_index, col_index)] = col

    # Defining the length of first row, last row and middle rows
    first = min(range(len(matrix)))
    last = max(range(len(matrix)))
    _, *middle, _ = list(range(len(matrix)))

    if len(list(range(len(matrix)))) >= 3:
        _, *middle, _ = list(range(len(matrix)))
    else:
        middle = None

    # Creating pattern for rows
    pattern = []
    pattern.extend([first] * len(matrix))
    if middle is not None:
        for m in middle:
            pattern.extend([m])

    pattern.extend([last] * len(matrix))
    if middle is not None:
        for m in middle[::-1]:
            pattern.extend([m])

    rows = pattern
    # Creating pattern for columns
    columns = pattern[len(matrix)-1:]+pattern[:len(matrix)-1]

    # Creating original matrix's positional index from patterns
    orignal_matrix_pos = []
    for r, c in zip(rows, columns):
        orignal_matrix_pos.append((r, c))

    # Creating copy of original matrix
    rotated_matrix = []
    for inner_list in matrix:
        rotated_matrix.append(inner_list.copy())

    all_matrix_pos = set([tuple(item) for item in list(orignal_matrix_pos)])

    # Rotate original matrix
    rotated_matrix = _rotate(rotated_matrix=rotated_matrix,
                             matrix_pos=orignal_matrix_pos,
                             degree=degree,
                             clockwise=clockwise,
                             pos_dict=pos_dict,
                             size=int((len(orignal_matrix_pos)+4)/4),
                             all_matrix_pos=all_matrix_pos)
    return rotated_matrix


def _rotate(rotated_matrix: list, matrix_pos: list, degree: int,
            clockwise: bool, pos_dict: dict, size: int,
            all_matrix_pos: set) -> list:
    """
    Recursive rotation of array pixel in clockwise and anticlockwise direction
    with a degree of rotation ranging from 0 to 360.
    This rotation starts from outer layer towards inner layer.

    Parameters
    ----------
    rotated_matrix : list
        Input square matrix.
    matrix_pos : list
        (row, column) index position for rotation.
    degree : int
        Degree of rotation.
    clockwise : bool
        Direction of rotation. The default is True.
        True for clockwise direction
        False for anticlockwise direction.
    pos_dict : dict
        Dictionary of index position and its value.
    size : int
        Size of square matrix to rotate.
    all_matrix_pos : set
        Set of appeared index postions in a recursive calling.

    Returns
    -------
    list
        Rotated matrix with one layer of rotation at a time.

    """
    # Creating matrix position for n degree rotation
    if clockwise:
        rotated_matrix_pos = list(
            matrix_pos[degree:]) + list(matrix_pos[:degree])
    else:
        rotated_matrix_pos = list(
            matrix_pos[-degree:]) + list(matrix_pos[:-degree])

    # Creating rotated dictionary with positional index and value
    rotated_pos_dict = {}
    for om_pos, rm_pos in zip(matrix_pos, rotated_matrix_pos):
        rotated_pos_dict[tuple(rm_pos)] = pos_dict[tuple(om_pos)]

    my_list = []
    range_list = list(range(len(rotated_matrix)))
    index_range = list(itertools.product(range_list, range_list))

    for item in index_range:
        row_index, col_index = item
        try:
            rotated_matrix[row_index][col_index] = rotated_pos_dict[(
                row_index, col_index)]
            all_matrix_pos = list(all_matrix_pos)
            all_matrix_pos.extend(list(rotated_pos_dict.keys()))
            all_matrix_pos = set(all_matrix_pos)
        except KeyError:
            if (row_index, col_index) not in all_matrix_pos:
                my_list.append((row_index, col_index))
            continue

    start = my_list and min(min(my_list))
    end = my_list and max(max(my_list))

    if len(matrix_pos) < 5:
        return rotated_matrix
    elif start == end:
        return rotated_matrix
    else:
        # Defining the length of first row, last row and middle rows
        first = min(range(start, end))
        last = max(range(start, end+1))
        if len(list(range(start, end+1))) >= 3:
            _, *middle, _ = list(range(start, end+1))
        else:
            middle = None
        size = size - 2

        # Creating pattern for rows
        pattern = []
        pattern.extend([first] * size)

        if middle is not None:
            for m in middle:
                pattern.extend([m])

        pattern.extend([last] * size)

        if middle is not None:
            for m in middle[::-1]:
                pattern.extend([m])

        rows = pattern
        # creating pattern for columns
        columns = pattern[size-1:]+pattern[:size-1]

        # Creating original matrix's positional index from patterns
        recursion_matrix_pos = []
        for r, c in zip(rows, columns):
            recursion_matrix_pos.append((r, c))

        # Recursive call
        return _rotate(rotated_matrix,
                       recursion_matrix_pos,
                       degree,
                       clockwise, pos_dict=pos_dict,
                       size=int((len(recursion_matrix_pos)+4)/4),
                       all_matrix_pos=all_matrix_pos)


def pprint(matrix: list) -> str:
    """
    Preety print matrix string

    Parameters
    ----------
    matrix : list
        Square matrix.

    Returns
    -------
    str
        Preety string form of matrix.

    """
    matrix_string = str(matrix)
    matrix_string = matrix_string.replace('],', '],\n')
    return matrix_string


def printing(matrix: list, rotated_matrix: list, degree: int, clockwise: bool):
    """
    Printing Original Matrix and Rotated Matrix with the Degree of rotation

    Parameters
    ----------
    matrix : list
        Original square matrix.
    rotated_matrix : list
        Rotated square matrix.
    degree : int
        Degree of rotation..
    clockwise : bool
        Direction of rotation. The default is True.
        True for clockwise direction
        False for anticlockwise direction
    Returns
    -------
    None

    """
    print("\nOriginal Matrix:\n{}\n".format(pprint(matrix)))
    if clockwise:
        rotation = 'Clockwise'
    else:
        rotation = "Anitclockwise"
    print("{} Rotated Matrix with Degree = {}:\n{}".format(
        rotation, degree, pprint(rotated_matrix)))
    print("-"*45)


def print_rotate_matrix(matrix: list, degree: int = 1,
                        clockwise: bool = True) -> list:
    """
    Generalize function to rotate any matrix's outer layer clockwise and
    anticlockwise and printing the original and rotated matrix.

    Parameters
    ----------
    matrix : list
        Input square matrix.
    degree : int, optional
        Degree of rotation. The default is 1.
    clockwise : bool, optional
        Direction of rotation. The default is True.
        True for clockwise direction
        False for anticlockwise direction

    Returns
    -------
    rotated_matrix : list
        Rotated square matrix.

    >>> matrix = [['a', 'b', 'c'],\
                  ['h', 'i', 'd'],\
                  ['g', 'f', 'e']]

    >>> rotated_matrix = rotate_matrix(matrix, degree=2, clockwise=True)

    >>> rotated_matrix
    [['g', 'h', 'a'], ['f', 'i', 'b'], ['e', 'd', 'c']]

    >>> rotated_matrix = print_rotate_matrix(matrix, degree=2, clockwise=True)
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
    """
    rotated_matrix = rotate_matrix(
        matrix=matrix, degree=degree, clockwise=clockwise)
    printing(matrix, rotated_matrix, degree=degree, clockwise=clockwise)
    return rotated_matrix


if __name__ == "__main__":
    import random
    import time

    n = 64
    matrix = []
    for _ in range(n):
        arr = [random.randint(1, 100) for i in range(n)]
        matrix.append(arr)

    tic = time.time()
    rotated_matrix = rotate_matrix(matrix, degree=1, clockwise=True)
    toc = time.time()
    print("Time required to rotate 64x64 matrix is {} sec".format(toc-tic))
