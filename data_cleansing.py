import json
import pandas as pd

# load data
with open('/Users/xueting/PycharmProjects/ingredientReplace/train 2.json', encoding="utf-8") as f:
    data = json.load(f)
#
MINIMALSUPPORT = 3
# find the distribution of the ingredients
ingredient_set =set()
recipe_list = []
invalid_id_list = []
for i in range(len(data)):
    recipe = data[i]
    if len(recipe['ingredients'])>=1:
        for ingre in recipe['ingredients']:
            recipe_list.append([recipe['id'], ingre])

    else:
        invalid_id_list.append(recipe['id'])

recipe_df = pd.DataFrame.from_records(recipe_list, columns=['id', 'ingredient'])
ingre_dist = recipe_df['ingredient'].value_counts()
rare_ingre = ingre_dist[ingre_dist.values<MINIMALSUPPORT]
rare_recipe = recipe_df[recipe_df['ingredient'].isin(rare_ingre.index)]
cleaned_recipe = recipe_df[~recipe_df.id.isin(rare_recipe.id.values)]
remain_id = set(cleaned_recipe.id)
rare_id = set(rare_recipe.id)
cleaned_recipe.to_csv('cleaned_recipe.csv', index=False)

