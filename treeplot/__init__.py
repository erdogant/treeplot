from treeplot.treeplot import (
    plot,
    randomforest,
	xgboost,
    import_example,
)

__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '0.1.2'

# module level doc-string
__doc__ = """
treeplot vizualizes a tree based on a randomforest or xgboost model.
=====================================================================

Description
-----------
treeplot vizualizes a tree based on a randomforest or xgboost model.

Example
-------
>>> import treeplot
>>> X,y = treeplot.import_example()
>>> model = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0).fit(X, y)
>>> model = XGBClassifier(n_estimators=100, max_depth=2, random_state=0).fit(X, y)
>>> fig = treeplot.plot(model)

References
----------
https://github.com/erdogant/treeplot
"""
