#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for index, item in enumerate(weights):
        hash_table_insert(ht, item, index)
        print(hash_table_retrieve(ht, index))
        remainder_to_find = limit - item
        is_remainder = hash_table_retrieve(ht, remainder_to_find)
        # if the desired remaining value is in the weights array
        if is_remainder:
            # if index is 1, than the only other index would be zero, necessitating the tuple (1,0)
            if index == 1:
                print("index is 1")
                return (index, 0)
            # if is_remainder returns an index higher than the current index, than that would be the 0th spot in the returned tuple
            elif is_remainder > index:
                print("remainder > index")
                return (is_remainder, index)
            else:
                print("ELSE")
                return (index, is_remainder)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
