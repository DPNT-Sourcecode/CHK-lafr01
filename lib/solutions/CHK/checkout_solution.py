from functools import partial
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    def n_items_for_p(n, p, n2, p2, item):
        batches_of_n = item["count"] // n
        remaining = item["count"] % n

        if n2 and p2:
            batches_of_n2 = remaining // n2
            remaining = remaining  % n2
            return batches_of_n * p + batches_of_n2*p2 + remaining*item["price"]

        return batches_of_n * p + remaining*item["price"]
    
    def free_X_for_nY(X, n, Y):
        freeXs = items[Y]["count"] // n
        items[X]["count"] = max(items[X]["count"]-freeXs, 0)
    
    def buy_n_get_1_free(n, X):
        if items[X]["count"] >= n+1:
            free = items[X]["count"] // n+1
            items[X]["count"] -= free


    items = { 
        "A": {"price": 50, "count": 0, "offer": n_items_for_p, "args":(5, 200, 3, 130)},
        "B": {"price": 30, "count": 0, "offer": n_items_for_p, "args":(2, 45, 0, 0)},
        "C": {"price": 20, "count": 0},
        "D": {"price": 15, "count": 0},
        "E": {"price": 40, "count": 0, "offer": free_X_for_nY, "args":("B", 2 , "E")},
        "F": {"price": 10, "count": 0, "offer": buy_n_get_1_free, "args": (2, "F")},
        "G": {"price": 20, "count": 0},
        "H": {"price": 10, "count": 0, "offer": n_items_for_p, "args":(10, 80, 5, 45)},
        "I": {"price": 35, "count": 0},
        "J": {"price": 60, "count": 0},
        "K": {"price": 80, "count": 0, "offer": n_items_for_p, "args":(2, 150, 0, 0)},






    }
    for item in skus:
        if item not in items: return -1
        items[item]["count"] += 1

    #CHK_R2

    def get_price_for_b(n):
        batches_of_2 = n // 2
        remaining = n  % 2
        return batches_of_2 * 45 + remaining * items["B"]["price"]


    freeBs = items["E"]["count"] // 2
    items["B"]["count"] =  max(items["B"]["count"] - freeBs, 0)

    #CHK_R3   

    if items["F"]["count"] >= 3:
        freeFs = items["F"]["count"]//3
        items["F"]["count"] -= freeFs


    subtotal = 0
    for item, details in items.items():
        if item == "A":
            batches_of_5 = details["count"] // 5
            remaining = details["count"]  % 5

            batches_of_3 = remaining // 3
            remaining = remaining  % 3

            subtotal += batches_of_5*200 + batches_of_3 * 130 + remaining * details["price"]

        elif item == "B":
            subtotal += get_price_for_b(details["count"])

        else:
            subtotal += details["price"]*details["count"]

    
    return int(subtotal)
