# treeplot

[![Python](https://img.shields.io/pypi/pyversions/treeplot)](https://img.shields.io/pypi/pyversions/treeplot)
[![PyPI Version](https://img.shields.io/pypi/v/treeplot)](https://pypi.org/project/treeplot/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/treeplot/blob/master/LICENSE)
[![Downloads](https://pepy.tech/badge/treeplot)](https://pepy.tech/project/treeplot)
[![Downloads](https://pepy.tech/badge/treeplot/month)](https://pepy.tech/project/treeplot/month)
[![BuyMeCoffee](https://img.shields.io/badge/buymea-coffee-yellow.svg)](https://www.buymeacoffee.com/erdogant)
[![Sphinx](https://img.shields.io/badge/Sphinx-Docs-Green)](https://erdogant.github.io/treeplot/)
<!---[![Coffee](https://img.shields.io/badge/coffee-black-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)-->

* ``treeplot`` is Python package to easily plot the tree derived from models such as decisiontrees, randomforest and xgboost.
Developing explainable machine learning models is becoming more important in many domains. The most popular and classical explainable models are still tree based. Think of decision trees or random forest. The tree that is learned can be visualized and then explained. However, it can be a challange to simply plot the tree. Think of configuration issues with dot files, path locations to graphviz, differences across operating systems, differences across editors such as jupyter notebook, colab, spyder etc. This frustration led to this library, an easy way to plot the decision trees 🌲. It works for Random-forest, decission trees, xgboost and gradient boosting models. Under the hood it makes many checks, downloads graphviz, sets the path and then plots the tree.

### Functions in treeplot

Treeplot can plot the tree for Random-forest, decission trees, xgboost and gradient boosting models:
  * .plot         : Generic function to plot the tree of any of the four models with default settings
  * .randomforest : Plot the randomforest model. Parameters can be specified.
  * .xgboost      : Plot the xgboost model. Parameters can be specified.
  * .import_example('iris') : Import example dataset

# 
**⭐️ Star this repo if you like it ⭐️**
#

#### Install treeplot from PyPI

```bash
pip install treeplot
```

#### Import treeplot package

```python
import treeplot as tree
```
# 


### [Documentation pages](https://erdogant.github.io/treeplot/)

On the [documentation pages](https://erdogant.github.io/treeplot/) you can find detailed information about the working of the ``treeplot`` with examples. 

<hr> 

### Examples

# 

* [Example: RandomForest](https://erdogant.github.io/treeplot/pages/html/Examples.html#)

<p align="left">
  <a href="https://erdogant.github.io/treeplot/pages/html/Examples.html#">
  <img src="https://github.com/erdogant/treeplot/blob/master/docs/figs/fig_breast_randomforest.png" width="600" />
  </a>
</p>


# 

* [Example: XGboot](https://erdogant.github.io/treeplot/pages/html/Examples.html#xgboost)

<p align="left">
  <a href="https://erdogant.github.io/treeplot/pages/html/Examples.html#xgboost">
  <img src="https://github.com/erdogant/treeplot/blob/master/docs/figs/fig_breast_xgboot_tree.png" width="600" />
   <br>
  <img src="https://github.com/erdogant/treeplot/blob/master/docs/figs/fig_breast_xgboot_weights.png" width="600" />
  </a>
</p>


# 
* [Example: gradientboostingclassifier](https://erdogant.github.io/treeplot/pages/html/Examples.html#gradientboostingclassifier)
# 
* [Example: lightbm](https://erdogant.github.io/treeplot/pages/html/Examples.html#lightbm)
# 
* [Example: Explore other trees such as second best tree etc](https://erdogant.github.io/treeplot/pages/html/Examples.html#plot-second-best-tree-and-other-trees)

<hr>

#### Maintainers
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)

#### Contribute
* Contributions are welcome.
* If you wish to buy me a <a href="https://www.buymeacoffee.com/erdogant">Coffee</a> for this work, it is very appreciated :)

