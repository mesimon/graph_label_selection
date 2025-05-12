import greedy_via_flow
import guillory_bilmes
import cesa_bianchi_et_al

import networkx as nx
import numpy as np


if __name__ == "__main__":
    #Star
    G = nx.star_graph(50)
    gb_ = []
    cb_ = []
    num_iters = 10
    for j in range(num_iters):
        gb_.append(guillory_bilmes.guillory_bilmes(G, 3)[0])
        cb_.append(cesa_bianchi_et_al.cesa_bianchi_et_al(G, 3)[0])
    ours = greedy_via_flow.gls(G, 3)[0]
    print("S(50):")
    print("GB: " + str(np.mean(gb_)) + " pm " + str(np.std(gb_)))
    print("CB: " + str(np.mean(cb_)) + " pm " + str(np.std(cb_)))
    print("Ours: " + str(np.mean(ours)))
    
    G = nx.empty_graph()
    #Three cliques
    # Create the three cliques with 10, 30, 10 vertices each
    clique1 = range(1, 11)  
    clique2 = range(11, 41)  
    clique3 = range(41, 50) 

    # Add edges to make the two cliques fully connected
    G.add_edges_from([(u, v) for u in clique1 for v in clique1 if u != v])
    G.add_edges_from([(u, v) for u in clique2 for v in clique2 if u != v]) 
    G.add_edges_from([(u, v) for u in clique3 for v in clique3 if u != v]) 

    G.add_edge(1,11)
    G.add_edge(41,11)
    gb_ = []
    cb_ = []
    num_iters = 10
    for j in range(num_iters):
        gb_.append(guillory_bilmes.guillory_bilmes(G, 3)[0])
        cb_.append(cesa_bianchi_et_al.cesa_bianchi_et_al(G, 3)[0])
    ours = greedy_via_flow.gls(G, 3)[0]
    print("3C(10,30,10):")
    print("GB: " + str(np.mean(gb_)) + " pm " + str(np.std(gb_)))
    print("CB: " + str(np.mean(cb_)) + " pm " + str(np.std(cb_)))
    print("Ours: " + str(np.mean(ours)))