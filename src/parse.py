from argparse import ArgumentError
import ast

PI = 3.1415926535 

def read_input_from_file(file_path):
    """
    Reads input data from a file and returns a list of lines.

    Parameters:
    - file_path (str): The path to the input file.

    Returns:
    - input_lines (list): List of lines read from the input file.
    """
    with open(file_path, 'r') as file:
        input_data = file.read()
        input_lines = input_data.split('\n')
    file.close()
    return input_lines

def validate_and_parse_input(input_lines):
    """
    Parses input lines into a dictionary and uses help function to validate criteria, following specified constraints.

    Parameters:
    - input_lines (list): List of lines from the input file.

    Returns:
    - d (dictionary): Parsed dictionary containing parameter-value pairs.
    """

    exp_inputs = [
        'NUMPOINTS', 'POINTS', 'LENGTH1', 'RADIUS1', 'EPSILON', 'AREA1', 'Q_PTS',
        'QUADS', 'DIST', 'N_PTS', 'K_PTS', 'A_PTS', 'B_PTS', 'C_PTS', 'D_PTS',
        'E_PTS', 'F_PTS', 'G_PTS', 'LENGTH2', 'RADIUS2', 'AREA2', 'LCM', 'PUV'
    ]
    d = {}
    
    try:
        for key, value in zip(exp_inputs, input_lines):
            value_str = value.split("=")[1]
            val = ast.literal_eval(value_str)
            d[key] = val
    except (ValueError, SyntaxError):
        raise Exception(f'Invalid value for {key}')


    validate(d)
    return d

def validate(d):
    """
    Performs the validation on the parsed dictionary based on predefined constraints.

    Parameters:
    - d (dictionary): Parsed dictionary containing parameter-value pairs.

    Raises:
    - ArgumentError: If any of the validation constraints is not satisfied.
    """
    constraints =[
        ("NUMPOINTS", lambda x: x == len(d['POINTS']) and 2 <= x <= 100),
        ("LENGTH1", lambda x: x >= 0),
        ("RADIUS1", lambda x: x >= 0),
        ("EPSILON", lambda x: 0 <= x < PI),
        ("AREA1", lambda x: x >= 0),
        ("Q_PTS", lambda x: d["NUMPOINTS"] >= x >= 2),
        ("QUADS", lambda x: 3 >= x >= 1),
        ("DIST", lambda x: x >= 0),
        ("N_PTS", lambda x: d["NUMPOINTS"] >= x >= 3),
        ("K_PTS", lambda x: d["NUMPOINTS"] - 2 >= x >= 1),
        ("A_PTS", lambda x: x >= 1),
        ("B_PTS", lambda x: x >= 1),
        ("C_PTS", lambda x: x >= 1),
        ("D_PTS", lambda x: x >= 1),
        ("E_PTS", lambda x: x >= 1),
        ("F_PTS", lambda x: x >= 1),
        ("G_PTS", lambda x: 1 <= x <= d["NUMPOINTS"] - 2),
        ("LENGTH2", lambda x: x >= 0),
        ("RADIUS2", lambda x: x >= 0),
        ("AREA2", lambda x: x >= 0),
        ("LCM", lambda x: len(x) == 15 and all(len(row) == 15 for row in x)),
        ("PUV", lambda x: len(x) == 15),
    ]

    for key, lambda_func in constraints:
        if not lambda_func(d[key]):
            raise Exception(f'Invalid value for {key}')

def read_input_to_dict(file_path='template.in'):
    """
    Combines the above functions to read and validate input data from a file,
    returning the parsed dictionary.

    Parameters:
    - file_path (str): The path to the input file.

    Returns:
    - d (dictionary): Parsed dictionary containing validated parameter-value pairs.
    """
    input_lines = read_input_from_file(file_path)
    d = validate_and_parse_input(input_lines)
    
    return d


if __name__ == '__main__':
    print(read_input_to_dict('../tests/data/template.in'))
