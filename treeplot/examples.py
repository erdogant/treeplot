import treeplot


# %% Make example dataset
X,y = treeplot.import_example()

# %% RF EXAMPLE
from sklearn.ensemble import RandomForestClassifier
model_rf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0).fit(X, y)

ax = treeplot.randomforest(model_rf, export='png')
# pdf
ax = treeplot.randomforest(model_rf, export='pdf')


# %% EXAMPLE XGBOOST
from xgboost import XGBClassifier
model_xgb = XGBClassifier(n_estimators=100, max_depth=2, random_state=0).fit(X, y)

ax = treeplot.xgboost(model_xgb)
ax = treeplot.xgboost(model_xgb, plottype='vertical')


# %% Auto detect model
ax = treeplot.plot(model_xgb)
ax = treeplot.plot(model_rf)
