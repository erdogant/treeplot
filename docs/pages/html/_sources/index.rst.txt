treeplot's documentation!
==============================

``treeplot`` is Python package to easily plot the tree derived from models such as decisiontrees, randomforest and xgboost. Developing explainable machine learning models is becoming more important in many domains. The most popular and classical explainable models are still tree based. Think of decision trees or random forest. The tree that is learned can be visualized and then explained. However, it can be a challange to simply plot the tree. Think of configuration issues with dot files, path locations to graphviz, differences across operating systems, differences across editors such as jupyter notebook, colab, spyder etc. This frustration led to this library, an easy way to plot the decision trees 🌲. It works for Random-forest, decission trees, xgboost and gradient boosting models. Under the hood it makes many checks, downloads graphviz, sets the path and then plots the tree.


Treeplot can plot the tree for Random-forest, decission trees, xgboost and gradient boosting models:

	* .plot		: Generic function to plot the tree of any of the four models with default settings
	* .randomforest : Plot the randomforest model.
	* .xgboost	: Plot the xgboost model.
	* .LightBM	: Plot the LightBM model.


Content
=======

.. toctree::
   :maxdepth: 1
   :caption: Installation
   
   Installation


.. toctree::
  :maxdepth: 1
  :caption: Tutorials

  Tutorials


.. toctree::
  :maxdepth: 1
  :caption: Plot

  Examples

.. toctree::
  :maxdepth: 1
  :caption: Documentation
  
  Documentation
  Coding quality
  treeplot.treeplot

* :ref:`genindex`


Quick install
-------------

.. code-block:: console

   pip install treeplot




Github
------------------------------

Please report bugs, issues and feature extensions there.
Github, `erdogant/treeplot <https://github.com/erdogant/treeplot/>`_.


Citing *treeplot*
-----------------------

The bibtex can be found in the right side menu at the `github page <https://github.com/erdogant/treeplot/>`_.


Sponsor this project
------------------------------

If you like this project, **Star** this repo at the github page and become a **sponsor**!
Read more why this is important on my sponsor page. The **sponsor button** will direct you to the sponsor github page.

.. raw:: html

	<iframe src="https://github.com/sponsors/erdogant/button" title="Sponsor erdogant" height="35" width="116" style="border: 0;"></iframe>



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. raw:: html

	<hr>
	<center>
		<script async type="text/javascript" src="//cdn.carbonads.com/carbon.js?serve=CEADP27U&placement=erdogantgithubio" id="_carbonads_js"></script>
	</center>
	<hr>

