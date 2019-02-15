
def squareKeys():
    dict = {}
    i = 1
    while(i <= 5):
        dict.update({i : i * i})
        i += 1
    return dict

print(squareKeys())    