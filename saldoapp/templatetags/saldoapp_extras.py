from django import template

register = template.Library()

def times(number):
    return range(number)

def get_value_from_list(l, index):
    return l[index]

def get_value_from_dict(dict_data, key):
    """
    usage example {{ your_dict|get_value_from_dict:your_key }}
    """
    if key:
        return dict_data.get(key)

def subtract(a, b):
    return a-b

register.filter('get_value_from_dict', get_value_from_dict)
register.filter('subtract', subtract)
register.filter('times', times)
register.filter('get_value_from_list', get_value_from_list)
