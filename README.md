# treeplot

[![Python](https://img.shields.io/pypi/pyversions/treeplot)](https://img.shields.io/pypi/pyversions/treeplot)
[![PyPI Version](https://img.shields.io/pypi/v/treeplot)](https://pypi.org/project/treeplot/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/treeplot/blob/master/LICENSE)
[![Downloads](https://pepy.tech/badge/treeplot/month)](https://pepy.tech/project/treeplot/month)

* treeplot is Python package to easily plot the tree derived from models such as decisiontrees, randomforest and xgboost.
Developing explainable machine learning models is becoming more important in many domains. The most popular and classical explainable models are still tree based. Think of decision trees or random forest. The tree that is learned can be visualized and then explained. However, it can be a challange to simply plot the tree. Think of configuration issues with dot files, path locations to graphviz, differences across operating systems, differences across editors such as jupyter notebook, colab, spyder etc. This frustration led to this library, an easy way to plot the decision trees 🌲. It works for Random-forest, decission trees, xgboost and gradient boosting models. Under the hood it makes many checks, downloads graphviz, sets the path and then plots the tree.

Have fun!

### Functions in treeplot

Treeplot can plot the tree for Random-forest, decission trees, xgboost and gradient boosting models:
  * treeplot.plot()         : Generic function to plot the tree of any of the four models with default settings
  * treeplot.plot_tree()    : Plot the decission tree model. Parameters can be specified.
  * treeplot.randomforest() : Plot the randomforest model. Parameters can be specified.
  * treeplot.xgboost()      : Plot the xgboost model. Parameters can be specified.
  * treeplot.import_example('iris') : Import example dataset

### Contents
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Contribute](#-contribute)
- [Maintainers](#-maintainers)
- [License](#-copyright)

### Installation
* Install treeplot from PyPI (recommended). treeplot is compatible with Python 3.6+ and runs on Linux, MacOS X and Windows. 
* It is distributed under the MIT license.

#### Quick Start
```
pip install treeplot
```

* Alternatively, install treeplot from the GitHub source:
```bash
git clone https://github.com/erdogant/treeplot.git
cd treeplot
python setup.py install
```  
 
#### Import treeplot package
```python
import treeplot
```

### Example RandomForest:
```python
# Load example dataset
X,y = treeplot.import_example()
# Learn model
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0).fit(X, y)
```

```python
# Make plot
ax = treeplot.plot(model)
# or directly
ax = treeplot.randomforest(model)
```
<p align="center">
  <img src="https://github.com/erdogant/treeplot/blob/master/docs/figs/Figure_1.png" width="550" />
</p>

```python
# If more parameters needs to be specified, use the exact function:
ax = treeplot.randomforest(model, export='pdf')
```

#### Example XGboost:
```python
# Load example dataset
X,y = treeplot.import_example()
# Learn model
from xgboost import XGBClassifier
model = XGBClassifier(n_estimators=100, max_depth=2, random_state=0).fit(X, y)
```

```python
# Make plot
ax = treeplot.plot(model)
# or directly
ax = treeplot.xgboost(model)
```
<p align="center">
  <img src="https://github.com/erdogant/treeplot/blob/master/docs/figs/Figure2_xgboost_hor.png" width="550" />
  <img src="https://github.com/erdogant/treeplot/blob/master/docs/figs/Figure2_featimportance.png" width="350" />
</p>

```python
# If more parameters needs to be specified, use the exact function:
ax = treeplot.xgboost(model, plottype='vertical')
```
<p align="center">
  <img src="https://github.com/erdogant/treeplot/blob/master/docs/figs/Figure2_xgboost_ver.png" width="550" />
</p>


#### Maintainers
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)

#### Contribute
* Contributions are welcome.

#### Licence
See [LICENSE](LICENSE) for details.
