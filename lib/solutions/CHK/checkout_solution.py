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
        if item not in items: return -1
        items[item]["count"] += 1
    
    subtotal = 0
    for item, details in items.items():
        if item == "A":
            batches_of_3 = details["count"] // 3
            remaining = details["count"]  % 3
            subtotal += batches_of_3 * 130 + remaining * details["price"]

        elif item == "B":
            batches_of_2 = details["count"] // 2
            remaining = details["count"]  % 2
            subtotal += batches_of_2 * 45 + remaining * details["price"]

        else:
            subtotal += details["price"]*details["count"]

    return int(subtotal)

