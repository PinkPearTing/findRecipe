from food2vec.semantic_nutrition import Estimator
import json
import pandas as pd
from cosineSimilarity import top_k_similar

import pandas as pd
sentences = []
with open("data/kaggle_and_nature_train.csv'") as fp:
    for line in fp:
        count += 1
        sentences = []
        print("Line{}: {}".format(count, line.strip()))

df = pd.read_csv('data/kaggle_and_nature.csv')
corpus_text = '\n'.join(df[:50000]['comment_text'])
sentences = corpus_text.split('\n')
sentences = [line.lower().split(' ') for line in sentences]

my_estimator = Estimator(food_data_filepath = 'data/kaggle_and_nature_train')

# load cleaned data
cleaned_recipe_df = pd.read_csv('cleaned_recipe.csv')
# for all the ingredients, compute the vector based on food2vec
estimator = Estimator()
ingredient_set = set()
embed_dict = {}
unknown_ingredient = set()
unique_ingre_set = set(cleaned_recipe_df['ingredient'].values)
for ingredient_i in unique_ingre_set:
    try:
        embed_dict[ingredient_i] = estimator.embed(ingredient_i)
    except:
        unknown_ingredient.update([ingredient_i])

# based on the vector similarity we clustering all the word into
# cluster  and using the most frequent word to replace all the other word in the cluster