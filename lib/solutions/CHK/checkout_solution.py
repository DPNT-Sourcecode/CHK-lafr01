from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items = { 
        "A": {"price": 50, "count": 0},
        "B": {"price": 30, "count": 0},
        "C": {"price": 20, "count": 0},
        "D": {"price": 15, "count": 0}
    }
    
    for item in skus:
        items[item]["count"] += 1
    
    raise NotImplementedError()



