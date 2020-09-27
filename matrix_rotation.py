def rotate_outer_layer(matrix:list, degree:int, clockwise=True)-> list:
    """
    Generalize function to rotate any matrix's outer layer clockwise and anticlockwise'

    Parameters
    ----------
    matrix : list[list]
        Input matrix.
    degree : int
        degree of rotation.
    clockwise : TYPE, optional
        DESCRIPTION. The default is True.
        Not True will rotate anticlockwise

    Returns
    -------
    rotated_matrix : list[list]
        .Rotated matrix

    """
    
    # Getting matrix position of and its value 
    pos_dict = {}
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            pos_dict[(row_index, col_index)] = col
    
    # Defining the length of first row, last row and middle rows
    length_pos = max(range(len(matrix)))
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

def pprint(matrix):
    matrix_string = str(matrix)
    matrix_string = matrix_string.replace('],', '],\n')
    return matrix_string

def printing(matrix, rotated_matrix, degree, clockwise):
    print("\nOriginal Matrix:\n{}\n".format(pprint(matrix)))
    if clockwise:
        rotation = 'Clockwise'
    else:
        rotation = "Anitclockwise"
    print("{} Rotated Matrix with Degree = {}:\n{}".format(rotation, degree, pprint(rotated_matrix)))
    print("-"*45)

if __name__ == '__main__':
    matrix = [['a', 'b'],
              ['d', 'c']]
    
    rotated_matrix = rotate_outer_layer(matrix=matrix, degree=1, clockwise=True)
    printing(matrix, rotated_matrix, degree=1, clockwise=True)

    matrix = [['a', 'b', 'c'],
              ['h', 'i', 'd'],
              ['g', 'f', 'e']]

    rotated_matrix = rotate_outer_layer(matrix=matrix, degree=1, clockwise=False)
    printing(matrix, rotated_matrix, degree=1, clockwise=False)
    
    matrix = [['a', 'b', 'c', 'd'],
              ['l', 'i', 'd', 'e'],
              ['k', 'f', 'e', 'f'],
              ['j', 'i', 'h', 'g']]

    rotated_matrix = rotate_outer_layer(matrix=matrix, degree=2, clockwise=True)
    printing(matrix, rotated_matrix, degree=2, clockwise=True)





