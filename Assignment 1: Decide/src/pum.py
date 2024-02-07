
def andd(a, b):
    """
    Helper function to create_pum(cmv) which translates connector 'ANDD' to the logical operator 'and'.

    :param a: First term in the conditional.
    :type a: bool

    :param b: Second term in the conditional.
    :type b: bool

    :return: Returns True if both a and b are true, False otherwise.
    :rtype: bool
    """
    return a and b


def orr(a, b):
    """
    Helper function to create_pum(cmv) which translates connector 'ORR' to the logical operator 'or'.

    :param a: First term in the conditional.
    :type a: bool

    :param b: Second term in the conditional.
    :type b: bool

    :return: Returns True if either a or b is true, False otherwise.
    :rtype: bool
    """
    return a or b


def not_used(a, b):
    """
    Helper function to create_pum(cmv) which translates connector 'NOTUSED' to the boolean value 'True'.

    :param a: First term in the conditional.
    :type a: bool

    :param b: Second term in the conditional.
    :type b: bool

    :return: Always returns True.
    :rtype: bool
    """
    return True


def create_pum(cmv):
    """
    Form the PUM matrix by using the data in the CMV_VECTOR in conjunction with the LCM. The boolean value PUM[i, j] is determined by the following:
    If LCM[i, j] = "ANDD":
    - PUM[i, j] = CMV_VECTOR[i] and CMV_VECTOR[j]
    If LCM[i, j] = "ORR":
    - PUM[i, j] = CMV_VECTOR[i] or CMV_VECTOR[j]
    If LCM[i, j] = "NOTUSED":
    - PUM[i, j] = True

    :param self: The CMV object.
    :type self: object

    :return: The Preliminary Unlocking Matrix (PUM).
    :rtype: list[list[bool]]
    """
    cmv_vector = cmv.CMV_VECTOR
    lcm = cmv.LCM

    connectors = {
        "ANDD": andd,
        "ORR": orr,
        "NOTUSED": not_used
    }

    pum = [[False] * 15 for _ in range(15)]

    for i in range(15):
        for j in range(15):
            if i != j:
                pum[i][j] = connectors[lcm[i][j]](cmv_vector[i], cmv_vector[j])
            else:
                pum[i][j] = True

    return pum
