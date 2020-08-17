from treeplot.treeplot import (
    plot,
    randomforest,
	xgboost,
    import_example,
)

__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '0.1.10'

# module level doc-string
__doc__ = """
treeplot
==========================================

Description
-----------
treeplot is Python package to easily plot the tree derived from models such as
decisiontrees, randomforest, xgboost and gradient boosting models. Under the hood it makes many checks,
downloads graphviz, sets the path and then plots the tree.

Example
-------
>>> import treeplot
>>> X,y = treeplot.import_example()
>>>
>>> # randomforest model
>>> model = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0).fit(X, y)
>>> fig = treeplot.plot(model)
>>>
>>> # xgboost model
>>> model = XGBClassifier(n_estimators=100, max_depth=2, random_state=0).fit(X, y)
>>> fig = treeplot.plot(model)

References
----------
* https://github.com/erdogant/treeplot
* https://arogozhnikov.github.io/2016/06/24/gradient_boosting_explained.html
* https://scikit-learn.org/stable/modules/tree.html

"""
