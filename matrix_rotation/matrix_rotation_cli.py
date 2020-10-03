import numpy as np
from matrix_rotation import rotate_matrix, print_rotate_matrix
import click

__all__ = ["main", "examples"]


def examples():
    """
    Run some exmaples

    Returns None
    -------
    None.

    """
    matrix = [['a', 'b'],
              ['d', 'c']]
    rotated_matrix = print_rotate_matrix(matrix, degree=1, clockwise=True)

    matrix = [['a', 'b'],
              ['d', 'c']]
    rotated_matrix = print_rotate_matrix(matrix, degree=1, clockwise=False)

    matrix = [['a', 'b', 'c'],
              ['h', 'i', 'd'],
              ['g', 'f', 'e']]
    rotated_matrix = print_rotate_matrix(matrix, degree=1, clockwise=False)

    matrix = [['a', 'b', 'c', 'd'],
              ['l', 'm', 'n', 'e'],
              ['k', 'p', 'o', 'f'],
              ['j', 'i', 'h', 'g']]
    rotated_matrix = print_rotate_matrix(matrix, degree=2, clockwise=True)

    matrix = [['a', 'b', 'c', 'd', 'e'],
              ['p', 'q', 'r', 's', 'f'],
              ['o', 'x', 'y', 't', 'g'],
              ['n', 'w', 'v', 'u', 'h'],
              ['m', 'l', 'k', 'j', 'i']]
    rotated_matrix = print_rotate_matrix(matrix, degree=2, clockwise=True)

    matrix = [['1', '2', '3', '4', '5', '6'],
              ['20', '21', '22', '23', '24', '7'],
              ['19', '32', '33', '34', '25', '8'],
              ['18', '31', '36', '35', '26', '9'],
              ['17', '30', '29', '28', '27', '10'],
              ['16', '15', '14', '13', '12', '11']]
    rotated_matrix = print_rotate_matrix(matrix, degree=3, clockwise=True)

    matrix = [['1', '2', '3', '4', '5', '6', '7'],
              ['24', '25', '26', '27', '28', '29', '8'],
              ['23', '40', '41', '42', '43', '30', '9'],
              ['22', '39', '48', '49', '44', '31', '10'],
              ['21', '38', '47', '46', '45', '32', '11'],
              ['20', '37', '36', '35', '34', '33', '12'],
              ['19', '18', '17', '16', '15', '14', '13']]
    rotated_matrix = print_rotate_matrix(matrix, degree=4, clockwise=False)


@click.command()
@click.option('--matrix', '-M', prompt='Type "None" to display default \
examples.\nEnter your matrix', help='Use to show default examples of matrix \
rotation. Otherwise use the input matrix from command line.\nInput \
example : [["a", "b"],["d", "c"]]')
@click.option('--degree', '-D', default=1, show_default='1', help='Degree of \
rotation. Can rotate matrix in between 0 degree to 360 degree.')
@click.option('--clockwise', '-C', default=True, show_default='True',
              type=bool, help='Use True to rotate matrix in a clockwise direction. \
False for rotation in anticlockwise direction.')
@click.option('--print_matrix', '-S', default=False, show_default='False',
              type=bool, help='Use True to show the result of Original \
and Rotated Matrix.')
def main(matrix=None, degree=1, clockwise=True, print_matrix=False):
    try:
        matrix = eval(matrix)
        shape = np.array(matrix).shape
    except (SyntaxError, TypeError, NameError):
        matrix = None
        click.echo("Please Enter a Valid list for matrix\n")
        return main()

    try:
        if matrix and shape[0] != shape[1]:
            click.echo("Please Enter a Valid Square Matrix\n")
            return main()
    except IndexError:
        click.echo("Please Enter a Valid 2D List\n")
        return main()

    if not matrix:
        examples()
    else:
        if print_matrix:
            rotated_matrix = print_rotate_matrix(
                matrix, degree=degree, clockwise=clockwise)
        else:
            rotated_matrix = rotate_matrix(
                matrix, degree=degree, clockwise=clockwise)
        click.echo(rotated_matrix)
        return rotated_matrix


if __name__ == '__main__':
    main()
