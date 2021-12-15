dict_old = {'dr':1, 'de':2}
dict_new = {}
for key_old in dict_old:
    key_new = key_old[1:].upper()
    dict_new[key_new] = dict_old[key_old]
print(dict_old, dict_new)

