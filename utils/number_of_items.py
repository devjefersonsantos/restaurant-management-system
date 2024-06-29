def number_of_items(items: list[int] | tuple[int]) -> dict:
    if type(items) is list: 
        items = items.copy()
    else:
        items = list(items)

    items.sort()
    result = dict()

    for item in items:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
