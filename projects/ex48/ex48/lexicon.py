_DIRECTIONS = ['north', 'east', 'south', 'west']
_VERBS = ['go', 'kill', 'eat']
_STOPS = ['the', 'in', 'of']
_NOUNS = ['bear', 'princess']


def _convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def _get_tuple(word):
    if word in _DIRECTIONS:
        return 'direction', word
    elif word in _VERBS:
        return 'verb', word
    elif word in _STOPS:
        return 'stop', word
    elif word in _NOUNS:
        return 'noun', word
    else:
        number = _convert_number(word)
        if number is not None:
            return 'number', number
        else:
            return 'error', word

def scan(sentence):
    ret_val = []
    for word in sentence.split():
        ret_val.append(_get_tuple(word))
    return ret_val
