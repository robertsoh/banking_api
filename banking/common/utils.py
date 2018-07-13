

def choices_to_dict(choices):
    data = {}
    for choice in choices:
        data[choice[0]] = choice[1]
    return data
