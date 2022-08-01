# import treeplot as tree
# print(dir(tree))
# print(tree.__version__)


# %% Make example dataset
from sklearn.tree import DecisionTreeClassifier

from sklearn import datasets
data = datasets.load_iris()
data = datasets.load_breast_cancer()

# Import treeplot library
import treeplot as tree

# Learn model
model = DecisionTreeClassifier(max_depth=4, random_state=0).fit(data.data, data.target)

# Plot the tree
ax = tree.plot(model, featnames=data.feature_names)

# %% Make GradientBoostingClassifier example dataset
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import datasets
data = datasets.load_breast_cancer()
# data = datasets.load_iris()

# Import treeplot library
import treeplot as tree

# Learn model
model = GradientBoostingClassifier().fit(data.data, data.target)

# Plot the tree
ax = tree.plot(model, featnames=data.feature_names)

# %% Make LightBM example dataset
from lightgbm import LGBMClassifier
from sklearn import datasets
data = datasets.load_breast_cancer()
# data = datasets.load_iris()

# Import treeplot library
import treeplot as tree

# Learn model
model = LGBMClassifier().fit(data.data, data.target)

# Plot the tree
ax = tree.plot(model, featnames=data.feature_names)


# %% Make XGBOOST example dataset
# Library to for model
import xgboost as xgb
from sklearn import datasets
data = datasets.load_breast_cancer()
# data = datasets.load_iris()

# Import treeplot library
import treeplot as tree

# Learn model
model = xgb.XGBClassifier(use_label_encoder=False, n_estimators=10, max_depth=5, random_state=0, eval_metric='logloss').fit(data.data, data.target)

# Plot the tree
ax = tree.plot(model, featnames=data.feature_names, num_trees=5)


# %% EXAMPLE
X, y = tree.import_example()

# %% RandromForest EXAMPLE
from sklearn.ensemble import RandomForestClassifier
model_rf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0).fit(X, y)


ax = tree.randomforest(model_rf, export='png')
ax = tree.randomforest(model_rf, export='pdf')

# %% Gradientboosting example
from sklearn.ensemble import GradientBoostingClassifier
gb = GradientBoostingClassifier()
model_gradientboost = gb.fit(X, y)

ax = tree.plot(model_gradientboost)

# %% XGBOOST EXAMPLE
import xgboost as xgb
model_xgb = xgb.XGBClassifier(n_estimators=100, max_depth=2, random_state=0).fit(X, y)

ax = tree.plot(model_xgb)
ax = tree.xgboost(model_xgb, plottype='vertical')

# %% XGBOOST EXAMPLE
from xgboost import XGBClassifier
model_xgb = XGBClassifier(n_estimators=100, max_depth=2, random_state=0).fit(X, y)

ax = tree.xgboost(model_xgb)
ax = tree.xgboost(model_xgb, plottype='vertical')

# %% Auto detect model
ax = tree.plot(model_rf, verbose=4)
ax = tree.plot(model_gradientboost, verbose=4)
ax = tree.plot(model_dt, verbose=4)
ax = tree.plot(model_xgb, verbose=4)
