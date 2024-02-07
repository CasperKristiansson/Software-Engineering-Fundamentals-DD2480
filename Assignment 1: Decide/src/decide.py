import sys
import os

# Add root folder to current path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.cmv import CMV
from src.fuv import generate_fuv
from src.pum import create_pum
from src.parse import read_input_to_dict


def instantiate_input(file_path):
    """
    Initiate all input variables before calling the decide method.

    :param file_path: Path to file containing input data.
    :type file_path: str

    :return: Returns True if the decide method returns True, False otherwise.
    :rtype: bool
    """
    d = read_input_to_dict(file_path)
    cmv = CMV(d)
    pum = create_pum(cmv)
    fuv = generate_fuv(pum, cmv.PUV)

    return decide(cmv, pum, fuv)


def print_matrix(mtx):
    """
    Helper function to print a matrix in a clear and visible way.

    :param mtx: The matrix to print.
    :type mtx: list[list[int]] | list[list[float]]

    :return: None
    :rtype: NoneType
    """
    for row in mtx:
        print(row)


def decide(cmv, pum, fuv):
    """
    This is the decide function that determines if a launch is required, based on the Final Unlocking Vector (FUV).

    :param cmv: The CMV object.
    :type cmv: object

    :param pum: The Preliminary Unlocking Matrix (PUM).
    :type pum: list[list[bool]]

    :param fuv: The Final Unlocking Vector.
    :type fuv: list[bool]

    :return: Returns True if Launch is required, False otherwise.
    :rtype: bool
    """
    LAUNCH = all(fuv)
    if LAUNCH:
        print('YES')
        # print()
        # print(f'The cmv is {cmv.CMV_VECTOR}')
        # print()
        # print("The pum is:")
        # print_matrix(pum)
        # print()
        # print(f'The fuv is {fuv}')

    else:
        print('NO')
        # print()
        # print(f'The cmv is {cmv.CMV_VECTOR}')
        # print()
        # print("The pum is:")
        # print_matrix(pum)
        # print()
        # print(f'The fuv is {fuv}')

    return LAUNCH

# if __name__ == '__main__':
#     instantiate_input(os.path.dirname(__file__)+"/../"+sys.argv[1])
