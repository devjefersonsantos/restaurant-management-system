def find_tuple_by_name(list_of_tuples: list[tuple], tuple_name: str) -> tuple:
    """
    To use after database .fetchall()\n
    Find tuple by name.
    """
    for k, v in enumerate(list_of_tuples):
        if v[1] == tuple_name:
            return list_of_tuples[k]
