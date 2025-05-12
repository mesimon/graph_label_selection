import greedy_via_flow
import guillory_bilmes
import cesa_bianchi_et_al

import networkx as nx
import numpy as np

if __name__ == "__main__":
    num_itr = 5

    f = open("../results/results.txt", "a")
    f.write("GrQs:\n")
    GrQc = nx.read_edgelist('../data/CA-GrQc.txt', nodetype=int)
    size = 0
    largest_comp = set()
    for comp in nx.connected_components(GrQc):
        if len(comp) > size:
            size = len(comp)
            largest_comp = comp
    GrQc = GrQc.subgraph(largest_comp)
    tau = None
    for i in [10, 50, 100]:
        f.write(str(i) + ":\n")
        tau = greedy_via_flow.gls(GrQc, i, tau_lower=tau)[0]
        f.write("Ours: " + str(tau) + "\n") 
        gb = []
        cb = []
        for _ in range(num_itr):
            cb.append(cesa_bianchi_et_al.cesa_bianchi_et_al(GrQc, i)[0])
            gb.append(guillory_bilmes.guillory_bilmes(GrQc, i)[0])
        f.write("guillory_bilmes: " + str(np.mean(gb)) + " pm " + str(np.std(gb)) + "\n")
        f.write("cesa_bianchi_et_al: " + str(np.mean(cb)) + " pm " + str(np.std(cb)) + "\n") 


