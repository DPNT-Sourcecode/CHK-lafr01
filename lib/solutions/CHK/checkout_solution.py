from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items = defaultdict(lambda: 0)
    for item in skus:
        items[item] += 1
    
    raise NotImplementedError()

