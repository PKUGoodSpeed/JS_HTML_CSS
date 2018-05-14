"""
@author: PKUGoodSpeed
Basic functions that can convert python objects into strings
"""

import random


def getRandomColor(num_colors=1):
    """
    :param num_colors: number of entries
    :return: a list of random colors
    """
    return ["#" + "".join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(num_colors)]


def listToString(l):
    """
    Converting list to string
    :param l: The input list, within which each entry is in the type of int, float, string, tuple, or bool
    :return: a string, with list elements are parsed by comma
    """
    return '[' + ', '.join([str(v) for v in l]) + "]"


def dictToString(d):
    """
    Converting a dictionary in to string
    :param d: The input dictionary, within which, each entry is in the type of int, float, bool, tuple, string, simple list
    :return: a string version of dictionary
    """
    if not d:
        return "{}"
    out_str = "{\n"
    for k, v in d.items():
        assert type(k) is str, "The key of the input dictionary should be strings."
        out_str += k + ": "
        if type(v) is str:
            out_str += "\'" + v + "\',\n"
        elif type(v) is list:
            out_str += listToString(v) + ",\n"
        elif type(v) is dict:
            out_str += dictToString(v) + ",\n"
        else:
            out_str += str(v) + ",\n"
    out_str = out_str[:-2]
    out_str += "}"
    return out_str
