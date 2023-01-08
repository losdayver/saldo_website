from django import template

register = template.Library()

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
