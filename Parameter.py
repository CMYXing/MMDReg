"""
Auxiliary tool -- used for store the global params
"""

def _init():
    global _global_dict
    _global_dict = {}

def set_value(key, value):
    _global_dict[key] = value

def get_value(key):
    try:
        return _global_dict[key]
    except KeyError:
        print('no variable named ' + key + '.')