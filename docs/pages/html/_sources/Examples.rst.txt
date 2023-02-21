RandomForest
################################################

In the following example we learn a simple **RandomForest** model and plot the tree.

.. code:: python
	
	# Library to for model
	from sklearn.tree import DecisionTreeClassifier
	from sklearn import datasets

	# Load example data
	data = datasets.load_breast_cancer()

	# Learn model
	model = DecisionTreeClassifier(max_depth=4, random_state=0).fit(data.data, data.target)

	# Import treeplot library
	import treeplot as tree

	# Plot the tree
	ax = tree.plot(model, featnames=data.feature_names)


.. |fig1| image:: ../figs/fig_breast_randomforest.png

.. table:: Decision tree for breastcancerusing RandomForest.
   :align: center

   +----------+
   | |fig1|   |
   +----------+


GradientBoostingClassifier
################################################

In the following example we learn a simple **GradientBoostingClassifier** model and plot the tree.

.. code:: python
	
	# Library to for model
	from sklearn.ensemble import GradientBoostingClassifier
	from sklearn import datasets

	# Load example data
	data = datasets.load_breast_cancer()

	# Learn model
	model = GradientBoostingClassifier().fit(data.data, data.target)

	# Import treeplot library
	import treeplot as tree

	# Plot the tree
	ax = tree.plot(model, featnames=data.feature_names)


.. |fig2| image:: ../figs/fig_breast_GradientBoostingClassifier.png

.. table:: Decision tree for breastcancer using GradientBoosting.
   :align: center

   +----------+
   | |fig2|   |
   +----------+


XGboost
################################################

In the following example we learn a simple **XGboost** model and plot the tree.

.. code:: python
	
	# Library to for model
	import xgboost as xgb
	from sklearn import datasets

	# Load example data
	data = datasets.load_breast_cancer()

	# Learn model
	model = xgb.XGBClassifier(use_label_encoder=False, n_estimators=10, max_depth=5, random_state=0, eval_metric='logloss').fit(data.data, data.target)

	# Import treeplot library
	import treeplot as tree

	# Plot the tree
	ax = tree.plot(model, featnames=data.feature_names)


.. |fig3| image:: ../figs/fig_breast_xgboot_tree.png
.. |fig4| image:: ../figs/fig_breast_xgboot_weights.png

.. table:: Decision tree for breastcancer using XGboost.
   :align: center

   +----------+
   | |fig3|   |
   +----------+
   | |fig4|   |
   +----------+



LightBM
################################################

In the following example we learn a simple **LightBM** model and plot the tree.

.. code:: python
	
	# Library to for model
	from lightgbm import LGBMClassifier
	from sklearn import datasets

	# Load example data
	data = datasets.load_breast_cancer()

	# Learn model
	model = LGBMClassifier().fit(data.data, data.target)

	# Import treeplot library
	import treeplot as tree

	# Plot the tree
	ax = tree.plot(model, featnames=data.feature_names)


.. |fig5| image:: ../figs/fig_breast_LightBM_tree.png
.. |fig6| image:: ../figs/fig_breast_LightBM_weights.png

.. table:: Decision tree for breastcancer using LightBM.
   :align: center

   +----------+
   | |fig5|   |
   +----------+
   | |fig6|   |
   +----------+



Plot second best Tree and other Trees
################################################

The opimization proces in the tee models will return the best performing models. However, other learned trees are also available and can be easily plotted.
Let's vizualize the second and third best tree.

.. code:: python
	
	# Library to for model
	import xgboost as xgb
	from sklearn import datasets

	# Load example data
	data = datasets.load_breast_cancer()

	# Learn model
	model = xgb.XGBClassifier(use_label_encoder=False, n_estimators=10, max_depth=5, random_state=0, eval_metric='logloss').fit(data.data, data.target)

	# Import treeplot library
	import treeplot as tree

	# Plot the tree
	ax = tree.plot(model, featnames=data.feature_names, num_trees=2)
	ax = tree.plot(model, featnames=data.feature_names, num_trees=5)


.. |fig7| image:: ../figs/fig_breast_xgboot_tree2.png
.. |fig8| image:: ../figs/fig_breast_xgboot_tree5.png

.. table:: Tree #2 and #5 for breastcancer using XGboost.
   :align: center

   +----------+
   | |fig7|   |
   +----------+
   | |fig8|   |
   +----------+


XGBoost Horizontal vs. Vertical
################################################

Changing the horizontal or vertical plotting can only be for XGboost.

.. code:: python
	
	# Library to for model
	import xgboost as xgb
	from sklearn import datasets

	# Load example data
	data = datasets.load_breast_cancer()

	# Learn model
	model = xgb.XGBClassifier(use_label_encoder=False, n_estimators=10, max_depth=5, random_state=0, eval_metric='logloss').fit(data.data, data.target)

	# Import treeplot library
	import treeplot as tree

	# Plot the tree
	ax = tree.plot(model, featnames=data.feature_names, plottype='vertical')
	ax = tree.plot(model, featnames=data.feature_names, plottype='horizontal')


.. |fig9| image:: ../figs/horizontal_plot.png
.. |fig10| image:: ../figs/vertical_plot.png

.. table:: Decision tree for breastcancer using LightBM.
   :align: center

   +----------+
   | |fig9|   |
   +----------+
   | |fig10|  |
   +----------+



.. include:: add_bottom.add