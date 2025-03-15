from Bio import AlignIO
from Bio import Phylo


with open('output_data/aligned_caninae.aln-clustalw','r') as aln:
    alignment = AlignIO.read(aln, 'clustal')

from Bio.Phylo.TreeConstruction import DistanceCalculator
calculator = DistanceCalculator('identity')

distance_matrix = calculator.get_distance(alignment)
#print(distance_matrix)


#tree building
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
constructor = DistanceTreeConstructor(calculator)

phylotree = constructor.build_tree(alignment)

#fig = Phylo.draw(phylotree)  



#adding styling
Phylo.write(phylotree, 'output_data/phylotree.nwk','newick')

import toytree
tree = toytree.tree('output_data/phylotree.nwk')

# Create cooler tree
canvas = tree.draw(
    width=800,
    height=800,
    edge_type='c',  
    node_sizes=16,
    node_colors='yellow',
    tip_labels=True,
    tip_labels_style={'font-size':'18px', 'fill':'white','font-family':'Helvetica'}
);

toytree.save(canvas[0], 'tree_plot.png')