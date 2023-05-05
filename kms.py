dict1 = {"bruh": [{'a':1,'b':2},{'a':3,'b':4}]}
print(dict1)
dict2 = {"bruh": [{'a':5,'b':6},{'a':7,'b':8}]}
print(dict2)
dict1['bruh'] = dict1['bruh']+dict2['bruh']
print(dict1)
#looks like this does indeed work! hmmmmmmmmmm