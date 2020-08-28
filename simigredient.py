from food2vec.semantic_nutrition import Estimator
import json
import pandas as pd
from cosineSimilarity import top_k_similar
# load data
with open('/Users/xueting/PycharmProjects/ingredientReplace/test 2.json', encoding="utf-8") as f:
    data = json.load(f)

# all_ingredients = recipe['ingredients']
## build the emding table:
estimator = Estimator()
ingredient_set = set()
for i in range(len(data)):
    recipe = data[i]
    ingredient_set.update(recipe['ingredients'])
embed_dict = {}
unknown_ingredient = set()
for ingredient_i in ingredient_set:
    try:
        embed_dict[ingredient_i] = estimator.embed(ingredient_i)
    except:
        unknown_ingredient.update([ingredient_i])
### start inference
imperfectRecipe = ['egg yolks', 'corn starch', 'cream of tartar',
                   'vanilla wafers', 'milk', 'vanilla extract', 'toasted pecans', 'egg whites', 'light rum', 'bananas']
missing_ingredient = 'sugar'
num_recomand = 3
k=100
select_top_k = True
trainData = []
candidate_set = set()
k_recipe = top_k_similar(imperfectRecipe, data, k)
for i in range(len(data)):
    recipe = data[i]
    if recipe['id'] in k_recipe:
        candidate_set.update(recipe['ingredients'])

for i in candidate_set:
    if i not in embed_dict:
        try:
            embed_dict[i] = estimator.embed(i)
        except:
            unknown_ingredient.update([i])
for i in unknown_ingredient:
    if i in candidate_set:
        candidate_set.remove(i)

replace_list = [[i,  estimator.cosine(embed_dict[missing_ingredient], embed_dict[i])]
                for i in candidate_set]
replace_df = pd.DataFrame.from_records(replace_list, columns=['ingredient','similarity'])

replace_df.nlargest(5, columns=['similarity'])
