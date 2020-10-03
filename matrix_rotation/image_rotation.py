import cv2
import pathlib
import numpy as np
from matrix_rotation import rotate_layers

FILE_PATH = pathlib.PosixPath(__file__)
BASE_PATH = FILE_PATH.parent
IMAGE_PATH = BASE_PATH / pathlib.PosixPath('images')

path = (IMAGE_PATH / pathlib.PosixPath('Kills_skull_64x64.png')).absolute()
path = path.as_posix()

image = cv2.imread(path)
red_channel = image[:, :, 2]
matrix = red_channel.tolist()

image_name = 'Kill_skull_64x64_red_channel.png'
path = (IMAGE_PATH / pathlib.PosixPath(image_name)).absolute()
path = path.as_posix()
cv2.imwrite(path, red_channel)

rotated_matrix = rotate_layers(matrix, degree=15, clockwise=True)
rotated_matrix = np.array(rotated_matrix)
image_name = 'Kill_skull_64x64_red_channel_rotated_15_degree_clockwise.png'
path = (IMAGE_PATH / pathlib.PosixPath(image_name)).absolute()
path = path.as_posix()
cv2.imwrite(path, rotated_matrix)

rotated_matrix = rotate_layers(matrix, degree=30, clockwise=True)
rotated_matrix = np.array(rotated_matrix)
image_name = 'Kill_skull_64x64_red_channel_rotated_30_degree_clockwise.png'
path = (IMAGE_PATH / pathlib.PosixPath(image_name)).absolute()
path = path.as_posix()
cv2.imwrite(path, rotated_matrix)

rotated_matrix = rotate_layers(matrix, degree=45, clockwise=True)
rotated_matrix = np.array(rotated_matrix)
image_name = 'Kill_skull_64x64_red_channel_rotated_45_degree_clockwise.png'
path = (IMAGE_PATH / pathlib.PosixPath(image_name)).absolute()
path = path.as_posix()
cv2.imwrite(path, rotated_matrix)

rotated_matrix = rotate_layers(matrix, degree=60, clockwise=True)
rotated_matrix = np.array(rotated_matrix)
image_name = 'Kill_skull_64x64_red_channel_rotated_60_degree_clockwise.png'
path = (IMAGE_PATH / pathlib.PosixPath(image_name)).absolute()
path = path.as_posix()
cv2.imwrite(path, rotated_matrix)

rotated_matrix = rotate_layers(matrix, degree=90, clockwise=True)
rotated_matrix = np.array(rotated_matrix)
image_name = 'Kill_skull_64x64_red_channel_rotated_90_degree_clockwise.png'
path = (IMAGE_PATH / pathlib.PosixPath(image_name)).absolute()
path = path.as_posix()
cv2.imwrite(path, rotated_matrix)

###############################################################################

rotated_matrix = rotate_layers(matrix, degree=15, clockwise=False)
rotated_matrix = np.array(rotated_matrix)
image_name = 'Kill_skull_64x64_red_channel_rotated_15_degree_anticlockwise.png'
path = (IMAGE_PATH / pathlib.PosixPath(image_name)).absolute()
path = path.as_posix()
cv2.imwrite(path, rotated_matrix)

rotated_matrix = rotate_layers(matrix, degree=30, clockwise=False)
rotated_matrix = np.array(rotated_matrix)
image_name = 'Kill_skull_64x64_red_channel_rotated_30_degree_anticlockwise.png'
path = (IMAGE_PATH / pathlib.PosixPath(image_name)).absolute()
path = path.as_posix()
cv2.imwrite(path, rotated_matrix)

rotated_matrix = rotate_layers(matrix, degree=45, clockwise=False)
rotated_matrix = np.array(rotated_matrix)
image_name = 'Kill_skull_64x64_red_channel_rotated_45_degree_anticlockwise.png'
path = (IMAGE_PATH / pathlib.PosixPath(image_name)).absolute()
path = path.as_posix()
cv2.imwrite(path, rotated_matrix)

rotated_matrix = rotate_layers(matrix, degree=60, clockwise=False)
rotated_matrix = np.array(rotated_matrix)
image_name = 'Kill_skull_64x64_red_channel_rotated_60_degree_anticlockwise.png'
path = (IMAGE_PATH / pathlib.PosixPath(image_name)).absolute()
path = path.as_posix()
cv2.imwrite(path, rotated_matrix)

rotated_matrix = rotate_layers(matrix, degree=90, clockwise=False)
rotated_matrix = np.array(rotated_matrix)
image_name = 'Kill_skull_64x64_red_channel_rotated_90_degree_anticlockwise.png'
path = (IMAGE_PATH / pathlib.PosixPath(image_name)).absolute()
path = path.as_posix()
cv2.imwrite(path, rotated_matrix)
