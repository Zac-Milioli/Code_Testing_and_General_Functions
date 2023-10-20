
def separate(separ = '\n'*5):
    print(separ)

json = {
    "item_1": {
        "1": [1,2],
        "2": [3,4],
        "3": [5,6]
    },
    "item_2": {
        "1": [1,2],
        "2": [3,4],
        "3": [5,6]
    }
}

separate()
print(json)
separate()
for i in json:
    print(i)
    separate()

print(json['item_1'])
print(json['item_1']['1'])
print(json['item_1']['2'])
print(json['item_2'])
print(json['item_2']['1'])
print(json['item_2']['2'])
separate()

print(len(json))
print(len(json['item_1']))
print(len(json['item_2']))
print(len(json['item_1']['1']))
print(len(json['item_1']['2']))
print(len(json['item_2']['1']))
print(len(json['item_2']['2']))
separate()
