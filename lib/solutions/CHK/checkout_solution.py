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
    
    for item, details in items.items():
        if item == "A":
            batches_of_3 = details["count"] % 3
            remaining = details["count"]  // 3
            subtotal = batches_of_3 * 130 + remaining * details["price"]

        elif item == "B":
        else:
            subtotal = details["price"]*details["count"]

    raise NotImplementedError()




