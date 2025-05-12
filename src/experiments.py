import greedy_via_flow
import guillory_bilmes
import cesa_bianchi_et_al

import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

def line_plot(G, ks, title, num_iters = 5):
    gb = []
    gb_std = []
    ours = []
    cb = []
    cb_std = []
    tl = None
    for i in ks:
        gb_ = []
        cb_ = []
        for j in range(num_iters):
            gb_.append(guillory_bilmes.guillory_bilmes(G, i)[0])
            cb_.append(cesa_bianchi_et_al.cesa_bianchi_et_al(G, i)[0])
        gb.append(np.mean(gb_))
        cb.append(np.mean(cb_))
        gb_std.append(np.std(gb_))
        cb_std.append(np.std(cb_))
        tl = greedy_via_flow.gls(G, i, tau_lower=tl)[0]
        ours.append(tl)
    x = ks
    # Set Seaborn style
    sns.set_theme(style="whitegrid", font_scale = 1.8)

    f = plt.figure(figsize=(10, 6))  # Set the figure size

    # Plot the lines
    plt.plot(x, gb, label='Guillory Bilmes', color='blue', marker='o', linestyle='-', linewidth=2)
    plt.plot(x, cb, label='Cesa-Bianchi et al.', color='orange', marker='o', linestyle='-', linewidth=2)
    plt.plot(x, ours, label='Ours', color='red', marker='o', linestyle='-', linewidth=2)

    # Add standard deviations
    plt.fill_between(x, [gb[i] - gb_std[i] for i in range(len(gb))], [gb[i] + gb_std[i] for i in range(len(gb))],
                    color='blue', alpha=0.2)
    plt.fill_between(x, [cb[i] - cb_std[i] for i in range(len(cb))], [cb[i] + cb_std[i] for i in range(len(cb))],
                    color='orange', alpha=0.2)

    # Title and labels
    plt.title(title)
    plt.xlabel('k')
    plt.ylabel('Ψ(L)')

    # Legend
    plt.legend()

    # Add a grid
    plt.grid(True, linestyle='--', alpha=0.7)
    return f

if __name__ == "__main__":
    G = nx.davis_southern_women_graph()
    # create figure for davis southern woman graph
    southern_woman = line_plot(G, range(1, G.number_of_nodes()), "Davis Southern Woman", 10)
    southern_woman.savefig("../figures/davis_southern_woman_new.pdf", format="pdf", bbox_inches="tight")

    # create figures for synthetic graphs
    G = nx.watts_strogatz_graph(50, 4, 0.2, seed = 42)
    watts = line_plot(G, range(1, G.number_of_nodes()), "Watts Strogatz(50, 4, 0.2)", 10)
    watts.savefig("../figures/watts_strogatz_50_4_2_new.pdf", format="pdf", bbox_inches="tight")

    G = nx.watts_strogatz_graph(50, 4, 0.1, seed = 42)
    watts = line_plot(G, range(1, G.number_of_nodes()), "Watts Strogatz(50, 4, 0.1)", 10)
    watts.savefig("../figures/watts_strogatz_50_4_1_new.pdf", format="pdf", bbox_inches="tight")

    G = nx.watts_strogatz_graph(50, 8, 0.2, seed = 42)
    watts = line_plot(G, range(1, G.number_of_nodes()), "Watts Strogatz(50, 8, 0.2)", 10)
    watts.savefig("../figures/watts_strogatz_50_8_2_new.pdf", format="pdf", bbox_inches="tight")

    G = nx.watts_strogatz_graph(50, 8, 0.1, seed = 42)
    watts = line_plot(G, range(1, G.number_of_nodes()), "Watts Strogatz(50, 8, 0.1)", 10)
    watts.savefig("../figures/watts_strogatz_50_8_1_new.pdf", format="pdf", bbox_inches="tight")
