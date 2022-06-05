import networkx as nx
import matplotlib.pyplot as plt
import random

def get_rand_graph(edge_count = 10,
                   min_e_weight = 1,
                   max_e_weight = 100,
                   random_seed = 123,
                   display = False):
    random.seed(random_seed)

    inc_random_seed = random_seed
    while True:
        g = nx.gnp_random_graph(edge_count, 0.3, inc_random_seed)
        if not nx.is_connected(g):
            # try again
            inc_random_seed += 1
        else:
            break
    nx.set_edge_attributes(g, {e: {'weight': random.randint(min_e_weight, max_e_weight+1)} for e in g.edges})

    if display:
        pos = nx.spring_layout(g, seed=random_seed)
        nx.draw(g, pos)
        labels=nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
        plt.show()

    return g
