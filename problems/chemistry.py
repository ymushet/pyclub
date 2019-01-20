"""
See the full table at http://www.hemi.nsu.ru/mends.htm
"""

import string

MENDELEEV_TABLE = {
    'H': 1,
    'He': 4,
    'Li': 7,
    'Be': 9,
    'B': 11,
    'C': 12,
    'N': 14,
    'O': 16,
    'F': 19,
    'Ne': 20,
    'Na': 23,
    'Mg': 24,
    'Al': 27,
    'Si': 28,
    'P': 31,
    'S': 32,
    'Cl': 35,
    'Ar': 40,
    'K': 39,
    'Ca': 40,
    'Sc': 45,
    'Ti': 48,
    'V': 51,
    'Cr': 52,
    'Mn': 55,
    'Fe': 56,
    'Co': 59,
    'Ni': 59,
    'Cu': 64,
    'Zn': 65,
    'Ga': 70,
    'Ge': 73,
    'As': 75,
    'Se': 79,
    'Br': 80,
    'Kr': 84,
}


def molar_mass(text):
    """
    See https://en.wikipedia.org/wiki/Molar_mass

    >>> molar_mass('H2O')
    18
    >>> molar_mass('C2H5OH')
    46
    >>> molar_mass('H2SO4')
    98
    """
    return 0


def parse_molekula(text):
    """
    >>> parse_molekula('C2H5')
    [['C', 2], ['H', 5]]
    >>> parse_molekula('OH')
    [['O', 1], ['H', 1]]
    >>> parse_molekula('NaCl')
    [['Na', 1], ['Cl', 1]]
    """
    return []


def tokenize(text):
    """
    >>> tokenize('NaCl')
    ['Na', 'Cl']
    >>> tokenize('H2O')
    ['H2', 'O']
    """
    return []