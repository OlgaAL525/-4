def divide(first, second):
    if second == 0:
        from math import inf
        return inf
    else:
        return round((first/second),3)
