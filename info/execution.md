
### enviroment preparation
1. set up the conda enviroment 

```
conda create --name phylotree python=3.12
```
unfortunately biopython requires an older python version, so we have to build an enviroment with that

2. install packages 

```
conda install biopython
``` 
biopython --version == 1.78
3. download data from NCBI as fasta files
I will provide an excel file in which you will have each species and a link to the relative refernce mithocondrial genome. Currently looking for a way to automate this step.



### installing ete3 for building a cicurlar tree
```
conda install toytree
```
toytree --version = 3.0.10
I opted for this libray because it's mininmal and does not require old python versions for working, it's simple but not straightforward so have a look at the documentation. 
Alternatevly there's another tool called ete3, which might even be better but requires an even older python version (I think python 3.7). Therefore if you want to use that package you will need to rebuild the whole enviroment. 

https://eaton-lab.org/toytree/quick_guide/#styling-tree-drawings




NOTE: 
if you are working in VSCODE or in another IDE, you might have to change the python interpreter to the one in the phylotree enviroment
use : Ctrl+Shift+P in VSCODE, type Python: Select Interpreter and select the correct one. 
