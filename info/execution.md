
### enviroment preparation
1. set up the conda enviroment 

```
conda create --name phylotree python=3.12
```

2. install packages 

```
conda install biopython
``` 
3. download data from NCBI as fasta files







### installing ete3 for building a cicurlar tree
```
conda install toytree
```
I opted for this libray because it's mininmal and does not require old python versions for working, it's simple but not straightforward so have a look at the documentation. 

https://eaton-lab.org/toytree/quick_guide/#styling-tree-drawings




NOTE: 
if you are working in VSCODE or in another IDE, you might have to change the python interpreter to the one in the phylotree enviroment
use : Ctrl+Shift+P in VSCODE, type Python: Select Interpreter and select the correct one. 
