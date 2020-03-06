import treeplot
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier


# %% Make example dataset
X,y = treeplot.import_example()


# %% EXAMPLE 1
model_rf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0).fit(X, y)
model_xgb = XGBClassifier(n_estimators=100, max_depth=2, random_state=0).fit(X, y)

# %% Make the plot
ax = treeplot.randomforest(model_rf, export='png')
# pdf
ax = treeplot.randomforest(model_rf, export='pdf')


# %% EXAMPLE 2
ax = treeplot.xgboost(model_xgb)
ax = treeplot.xgboost(model_xgb, plottype='vertical')


# %% Auto detect model
ax = treeplot.plot(model_xgb)
ax = treeplot.plot(model_rf)
