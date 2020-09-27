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
                  ['l', 'm', 'n', 'e'],\
                  ['k', 'p', 'o', 'f'],\
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

    if len(list(range(len(matrix))))>=3:
        _, *middle, _ = list(range(len(matrix)))
    else:
        middle = None

    
    # Creating pattern for first rows
    pattern = []
    pattern.extend([first]* len(matrix))
    if middle is not None:
        for m in middle:
            pattern.extend([m])
        
    pattern.extend([last]* len(matrix))
    if middle is not None:  
        for m in middle[::-1]:
            pattern.extend([m])
    
    rows  = pattern
    # creating pattern for columns
    columns = pattern[len(matrix)-1:]+pattern[:len(matrix)-1]
    
    # Creatring matrix position from patterns
    orignal_matrix_pos =[]
    for r, c in zip(rows, columns):
        orignal_matrix_pos.append((r, c))

    # creating rotated matrix
    rotated_matrix = []
    for inner_list in matrix:
        rotated_matrix.append(inner_list.copy())
    
    
    rotated_matrix = rotate(rotated_matrix = rotated_matrix, matrix_pos=orignal_matrix_pos, degree=1, clockwise=True, pos_dict=pos_dict, size = int((len(orignal_matrix_pos)+4)/4), all_matrix_pos = orignal_matrix_pos)

    
    
    ## creating matrix position for n degree rotation
    # if clockwise:
    #     rotated_matrix_pos = orignal_matrix_pos[degree:] + orignal_matrix_pos[:degree]
    # else:
    #     rotated_matrix_pos = orignal_matrix_pos[-degree:]+orignal_matrix_pos[:-degree]
    
    # # creating rotated dictionary with positions and values
    # rotated_pos_dict = {}
    # for om_pos, rm_pos in zip(orignal_matrix_pos, rotated_matrix_pos):
    #     rotated_pos_dict[rm_pos] = pos_dict[om_pos]
    
    # # creating rotated matrix
    # rotated_matrix = []
    # for inner_list in matrix:
    #     rotated_matrix.append(inner_list.copy())
       
        
    # for row_index in range(len(rotated_matrix)):
    #     for col_index in range(len(rotated_matrix[row_index])):
    #         try:
    #             rotated_matrix[row_index][col_index] = rotated_pos_dict[(row_index, col_index)]
    #         except KeyError:
    #             print(row_index, col_index)
    #             continue    




            
    return rotated_matrix



def rotate(rotated_matrix, matrix_pos, degree, clockwise, pos_dict, size,all_matrix_pos):
    # creating matrix position for n degree rotation
    if clockwise:
        rotated_matrix_pos = matrix_pos[degree:] + matrix_pos[:degree]
    else:
        rotated_matrix_pos = matrix_pos[-degree:]+matrix_pos[:-degree]
    
    # creating rotated dictionary with positions and values
    rotated_pos_dict = {}
    for om_pos, rm_pos in zip(matrix_pos, rotated_matrix_pos):
        rotated_pos_dict[rm_pos] = pos_dict[om_pos]
    
    my_list = []
    for row_index in range(len(rotated_matrix)):
        for col_index in range(len(rotated_matrix[row_index])):
            try:
                rotated_matrix[row_index][col_index] = rotated_pos_dict[(row_index, col_index)]
                all_matrix_pos.extend(list(rotated_pos_dict.keys()))
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
        if len(list(range(start, end+1)))>=3:
            _, *middle, _ = list(range(start, end+1))
        else:
            middle = None

    
        size = size - 2
    
        # Creating pattern for first rows
        pattern = []
        pattern.extend([first]* size)
    
        if middle is not None:
            for m in middle:
                pattern.extend([m])
            
        pattern.extend([last]* size)
        
        if middle is not None:  
            for m in middle[::-1]:
                pattern.extend([m])
        
        
        rows  = pattern
        # creating pattern for columns
        columns = pattern[size-1:]+pattern[:size-1]
        
        # Creatring matrix position from patterns
        recursion_matrix_pos = []
        for r, c in zip(rows, columns):
            recursion_matrix_pos.append((r, c))
        return rotate(rotated_matrix, recursion_matrix_pos, degree, clockwise, pos_dict=pos_dict, size = int((len(recursion_matrix_pos)+4)/4), all_matrix_pos = all_matrix_pos)
    








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
              ['l', 'm', 'n', 'e'],
              ['k', 'p', 'o', 'f'],
              ['j', 'i', 'h', 'g']]
    rotated_matrix = matrix_rotation(matrix, degree=2, clockwise=True)

    matrix = [['a', 'b', 'c', 'd', 'e'],
              ['p', 'q', 'r', 's', 'f'],
              ['o', 'x', 'y', 't', 'g'],
              ['n', 'w', 'v', 'u', 'h'],
              ['m', 'l', 'k', 'j', 'i']]
    rotated_matrix = matrix_rotation(matrix, degree=2, clockwise=True)


    matrix = [['1', '2', '3', '4', '5', '6'],
              ['20', '21', '22', '23', '24', '7'],
              ['19', '32', '33', '34', '25', '8'],
              ['18', '31', '36', '35', '26', '9'],
              ['17', '30', '29', '28', '27', '10'],
              ['16', '15', '14', '13', '12', '11']]
    rotated_matrix = matrix_rotation(matrix, degree=2, clockwise=True)




# import cv2

# image = cv2.imread('/home/vaibhav/Documents/Vaibhav/GitHub/matrix_rotation/Kills_skull_64x64.png')

# red_channel = image[:,:,2]

# print(red_channel.shape)
# matrix = red_channel.tolist()
# rotated_matrix = matrix_rotation(matrix, degree=99, clockwise=True)

# cv2.imwrite('Kill_skull_64x64_red_channel.png', red_channel)

# import numpy as np
# cv2.imwrite('Kill_skull_64x64_rotated.png', np.array(rotated_matrix))


# matrix = [['a', 'b', 'c', 'd'],
#           ['l', 'i', 'd', 'e'],
#           ['k', 'f', 'e', 'f'],
#           ['j', 'i', 'h', 'g']]
# rotated_matrix = matrix_rotation(matrix, degree=1, clockwise=True)




