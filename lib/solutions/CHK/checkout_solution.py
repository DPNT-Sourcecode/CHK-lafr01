# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items = { 
        "A": {"price": 50, "count": 0},
        "B": {"price": 30, "count": 0},
        "C": {"price": 20, "count": 0},
        "D": {"price": 15, "count": 0},
        "E": {"price": 40, "count": 0}
    }
    for item in skus:
        if item not in items: return -1
        items[item]["count"] += 1

    def get_price_for_b(n):
        batches_of_2 = n // 2
        remaining = n  % 2
        return batches_of_2 * 45 + remaining * items["B"]["price"]

    
    subtotal = 0
    for item, details in items.items():
        if item == "A":
            batches_of_5 = details["count"] // 5
            remaining = details["count"]  % 5

            batches_of_3 = remaining // 3
            remaining = remaining  % 3

            subtotal += batches_of_5*200 + batches_of_3 * 130 + remaining * details["price"]

        elif item == "B":
            batches_of_2 = details["count"] // 2
            remaining = details["count"]  % 2
            Bsubtotal = batches_of_2 * 45 + remaining * details["price"]
            subtotal += Bsubtotal

        else:
            subtotal += details["price"]*details["count"]

    freeBs = items["E"]["count"] // 2
    if items["B"]["count"]:
        discount = min(items["B"]["count"], freeBs)*items["B"]["price"]

    print(discount, freeBs, min(items["B"]["count"], freeBs))
    print(items)
    print(subtotal)

    return int(subtotal - discount)

checkout("EEEEBB")

