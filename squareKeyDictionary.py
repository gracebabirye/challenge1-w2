
def squareKeys():
    try:
        dict = {}
        i = 1
        while(i <= 15):
            dict.update({i : i * i})
            i += 1
        return dict
    except ValueError:
        return("Invalid input")

print(squareKeys())    