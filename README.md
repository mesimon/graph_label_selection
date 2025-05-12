This repository contains the code that was used for the experiments in the paper "Algorithms and Hardness for Active Learning on Graphs" accepted at ICML 2025.

Running "python simple_graphs.py" yields the experimental results for the table "Interpretable Example Graphs for k = 3"

Running "python experiments.py" generates the trade-off figures for the Davis southern woman graph and the synthetic graphs. 

Running "python table.py" yields the experimental results for the experiments with SNAP graphs. This experiment takes a lot of time and should be run in parallel. 

The algorithms are implemented in the following files: 

- cesa_bianchi_et_al.py: Implementation of the algorithm by Cesa-Bianchi et al.

- guillory_bilmes.py: Sequential and Paralell implementation of the algorithm by Guillory Bilmes.

- greedy_via_flow.py: Sequential and Paralell implementation of our algorithm. 

- helper_functions.py: Contains helper functions that are used by some of the algorithms. The function "cut_set()" is used to evaluate the performance of all algorithms. 
