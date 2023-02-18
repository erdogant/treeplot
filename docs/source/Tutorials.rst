.. include:: add_top.add

Input
###########################

The input for ``treeplot`` is a **model** that is learned with: 

	* Decision Tree Classifier
	* Gradient Boosting Classifier
	* XGBoost Classifier
	* LightBM Classifier

In the first run, *graphviz* will be downloaded and added to path locations. A demonstration is shown below.

.. code:: python
	
	# Import treeplot library
	import treeplot as tree
	
	# Plot the tree on the learned model
	ax = tree.plot(model)

	# [treeplot] >Downloading graphviz..
	# [treeplot] >Extracting graphviz files..
	# [treeplot] >Set path in environment.


Output
###########################

The output of ``treeplot`` :func:`treeplot.treeplot` is a ``ax``.



.. include:: add_bottom.add