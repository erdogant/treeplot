import treeplot
print(dir(treeplot))
print(treeplot.__version__)


# %% Make example dataset
from sklearn import tree
X,y = treeplot.import_example('iris')


# %% RandromForest EXAMPLE
from sklearn.tree import DecisionTreeClassifier
model_dt = DecisionTreeClassifier(max_depth=2, random_state=0).fit(X, y)

ax = treeplot.randomforest(model_dt)
tree.plot_tree(model_dt) 


# %% RandromForest EXAMPLE
from sklearn.ensemble import RandomForestClassifier
model_rf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0).fit(X, y)

ax = treeplot.randomforest(model_rf, export='png')
ax = treeplot.randomforest(model_rf, export='pdf')

# %% Gradientboosting example
from sklearn.ensemble.gradient_boosting import GradientBoostingClassifier
gb = GradientBoostingClassifier()
model_gradientboost = gb.fit(X, y)

ax = treeplot.plot(model_gradientboost)

# %% XGBOOST EXAMPLE
import xgboost as xgb
model_xgb = xgb.XGBClassifier(n_estimators=100, max_depth=2, random_state=0).fit(X, y)

ax = treeplot.plot(model_xgb)
ax = treeplot.xgboost(model_xgb, plottype='vertical')

# %% XGBOOST EXAMPLE
from xgboost import XGBClassifier
model_xgb = XGBClassifier(n_estimators=100, max_depth=2, random_state=0).fit(X, y)

ax = treeplot.xgboost(model_xgb)
ax = treeplot.xgboost(model_xgb, plottype='vertical')

# %% Auto detect model
ax = treeplot.plot(model_rf, verbose=4)
ax = treeplot.plot(model_gradientboost, verbose=4)
ax = treeplot.plot(model_dt, verbose=4)
ax = treeplot.plot(model_xgb, verbose=4)
