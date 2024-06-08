def number_of_items(item_list: list) -> dict:
    items = item_list.copy()
    items.sort()
    
    result = dict()

    for item in items:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
