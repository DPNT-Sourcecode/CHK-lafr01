from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items = { 
        "A": {"price": 50, "count": 0},
        "B": {"price": 50, "count": 0},
        "C": {"price": 50, "count": 0},
        "D": {"price": 50, "count": 0} }
    for item in skus:
        items[item] += 1
    
    raise NotImplementedError()


