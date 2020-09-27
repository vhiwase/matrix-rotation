def rotate_outer_layer(matrix:list, degree:int, clockwise:bool=True)-> list:
    """
    Generalize function to rotate any matrix's outer layer clockwise and anticlockwise'

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
                  ['l', 'i', 'd', 'e'],\
                  ['k', 'f', 'e', 'f'],\
                  ['j', 'i', 'h', 'g']]
    >>> rotated_matrix = rotate_outer_layer(matrix=matrix, degree=1, clockwise=True)
    >>> rotated_matrix
    [['l', 'a', 'b', 'c'], ['k', 'i', 'd', 'd'], ['j', 'f', 'e', 'e'], ['i', 'h', 'g', 'f']]
    """
    
    # Getting matrix position of and its value 
    pos_dict = {}
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            pos_dict[(row_index, col_index)] = col
    
    # Defining the length of first row, last row and middle rows
    first = min(range(len(matrix)))
    last = max(range(len(matrix)))
    _, *middle, _ = list(range(len(matrix)))
    
    # Creating pattern for first rows
    pattern = []
    pattern.extend([first]* len(matrix))
    for m in middle:
        pattern.extend([m])
    else:   
        pattern.extend([last]* len(matrix))
    for m in middle[::-1]:
        pattern.extend([m])
    
    rows  = pattern
    # creating pattern for columns
    columns = pattern[len(matrix)-1:]+pattern[:len(matrix)-1]
    
    # Creatring matrix position from patterns
    orignal_matrix_pos =[]
    for r, c in zip(rows, columns):
        orignal_matrix_pos.append((r, c))
    
    # creating matrix position for n degree rotation
    if clockwise:
        rotated_matrix_pos = orignal_matrix_pos[degree:] + orignal_matrix_pos[:degree]
    else:
        rotated_matrix_pos = orignal_matrix_pos[-degree:]+orignal_matrix_pos[:-degree]
    
    # creating rotated dictionary with positions and values
    rotated_pos_dict = {}
    for om_pos, rm_pos in zip(orignal_matrix_pos, rotated_matrix_pos):
        rotated_pos_dict[rm_pos] = pos_dict[om_pos]
    
    # creating rotated matrix
    rotated_matrix = []
    for inner_list in matrix:
        rotated_matrix.append(inner_list.copy())
        
    for row_index in range(len(rotated_matrix)):
        for col_index in range(len(rotated_matrix[row_index])):
            try:
                rotated_matrix[row_index][col_index] = rotated_pos_dict[(row_index, col_index)]
            except KeyError:
                continue                
    return rotated_matrix


def pprint(matrix:list)->str:
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


def printing(matrix:list, rotated_matrix:list, degree:int, clockwise:bool)->None:
    """
    Printing Original Matrix and Clockwise Rotated Matrix with the Degree.

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
    print("{} Rotated Matrix with Degree = {}:\n{}".format(rotation, degree, pprint(rotated_matrix)))
    print("-"*45)


def matrix_rotation(matrix:list, degree:int=1, clockwise:bool=True)->list:
    """
    Generalize function to rotate any matrix's outer layer clockwise and anticlockwise 
    and printing the original and rotated matrix.

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
    
    >>> rotated_matrix = rotate_outer_layer(matrix, degree=2, clockwise=True)
    
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
    """
    rotated_matrix = rotate_outer_layer(matrix=matrix, degree=degree, clockwise=clockwise)
    printing(matrix, rotated_matrix, degree=degree, clockwise=clockwise)
    return rotated_matrix


if __name__ == '__main__':
    matrix = [['a', 'b'],
              ['d', 'c']]    
    rotated_matrix = matrix_rotation(matrix, degree=1, clockwise=True)

    matrix = [['a', 'b', 'c'],
              ['h', 'i', 'd'],
              ['g', 'f', 'e']]
    rotated_matrix = matrix_rotation(matrix, degree=1, clockwise=False)
    
    matrix = [['a', 'b', 'c', 'd'],
              ['l', 'i', 'd', 'e'],
              ['k', 'f', 'e', 'f'],
              ['j', 'i', 'h', 'g']]
    rotated_matrix = matrix_rotation(matrix, degree=2, clockwise=True)





