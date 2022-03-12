Input
###########################

The input for ``treeplot`` is a **model** that is learned with: 

	* DecisionTreeClassifier
	* GradientBoostingClassifier
	* XGBClassifier

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




.. raw:: html

	<hr>
	<center>
		<script async type="text/javascript" src="//cdn.carbonads.com/carbon.js?serve=CEADP27U&placement=erdogantgithubio" id="_carbonads_js"></script>
	</center>
	<hr>
