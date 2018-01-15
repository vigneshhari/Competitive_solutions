from fractions import gcd


def is_power_of_two(x):
    return (x & (x - 1)) == 0 and x != 0

def has_exit(i, j):
    return is_power_of_two((i+j) / gcd(i,j))

class Guard:
    def __init__(self, bananas):
        self.bananas = bananas
        self.exit = []
        self.loop = []

def dn(list_nodes, node):
    for n in node.exit:
        n.exit.remove(node)
    for n in node.loop:
        n.loop.remove(node)
    list_nodes.remove(node)

def disconnect_pair(list_nodes, node1, node2):
    dn(list_nodes, node1)
    dn(list_nodes, node2)


def answer(banana_list):
    nb_guard = len(banana_list)
    g = [Guard(banana_list[i]) for i in xrange(nb_guard)]
    for i in xrange(0, nb_guard-1):
        for j in xrange(i+1, nb_guard):
            if has_exit(banana_list[i], banana_list[j]):
                g[i].exit.append(g[j])
                g[j].exit.append(g[i])
            else:
                g[i].loop.append(g[j])
                g[j].loop.append(g[i])

    counter = 0
    pairs = []

    """"
    if nb_guard % 2 == 1:
        singleton_guard = Guard(-1)
        for guard in g:
            singleton_guard.exit.append(guard)
            guard.exit.append(singleton_guard)
        g.append(singleton_guard)
        counter -= 1
    """

    while len(g) > 0:
        g.sort(key=lambda x: len(x.exit), reverse=True)

        current_guard = g[0]  #
        found_good = False
        for candidate_pair in g[1:]:
            if candidate_pair in current_guard.loop:
                pairs.append((current_guard, candidate_pair))
                disconnect_pair(g, current_guard, candidate_pair)
                found_good = True
                break
        if not found_good:
            counter += 2
            pairs.append((current_guard, g[1]))
            disconnect_pair(g, current_guard, g[1])

    return counter


if __name__ == "__main__":
    print answer([1, 1])
    print answer([1, 7, 3, 21, 13, 19])
    print answer([3, 3, 2, 6, 6])
    print answer([1, 7, 21])