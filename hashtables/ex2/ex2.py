#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for t in tickets:
        hash_table_insert(hashtable, t.source, t.destination)

    current_dest = hash_table_retrieve(hashtable, "NONE")
    route[0] = current_dest

    for i in range(length):
        if i > 0:
            # using the destination of the first node as the key for finding the second node, and setting it to the next variable
            next = hash_table_retrieve(hashtable, current_dest)
            # adding the next value that is returned sequentially to the route array
            route[i] = next
            # sets current_dest to next, because the value of next will equal the key for the next node
            current_dest = next

    return route
