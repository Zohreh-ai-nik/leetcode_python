def swap_value(dict):
    return {value: key for key, value in dict.items()}

dict = {'a': 1, 'b': 2}
dict = swap_value(dict)
# print(dict)
# print(dict.items())

def swap_values(d):
    keys = list(d.keys())               # ['a', 'b']
    values = list(d.values())           # [1, 2]
    values.reverse()                    # [2, 1]
    return dict(zip(keys, values))      # {'a': 2, 'b': 1}
