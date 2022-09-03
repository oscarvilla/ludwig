# %%
from ludwig.visualize import compare_performance
from ludwig.api import LudwigModel
import pandas as pd

df = pd.read_csv('rotten_tomatoes.csv')
model = LudwigModel(config='rotten_tomatoes.yaml')
results = model.train(dataset=df)

# %%
predictions, _ = model.predict(dataset='rotten_tomatoes_test.csv')
predictions.head()
# %%
eval_stats, _, _ = model.evaluate(dataset='rotten_tomatoes_test.csv')

# %%
# For just one model stats:
compare_performance([eval_stats])
# For comparison of two models stats
compare_performance([eval_stats_model_1, eval_stats_model_2])

# %%
