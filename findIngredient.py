import json
import time
from cosineSimilaritywithI2V import top_k_similar_withI2V
from gensim.models import Word2Vec
import pandas as pd
# load data
df = pd.read_csv('cleaned_recipe.csv')
data = []
for id_value in set(df['id'].values):
    data.append({
        'id':id_value,
        'ingredients':list(df[df['id']==id_value]['ingredient'].values)})
# all_ingredients = recipe['ingredients']
'''


imperfectRecipe = ['seasoned bread crumbs',
                    'dried basil',
                    'linguine',
                    'dried parsley',
                    'sugar',
                    'water',
                    'grated parmesan cheese',
                    'garlic cloves',
                    'vegetable oil cooking spray',
                    'pepper',
                    'large eggs',
                    'salt',
                    'dried oregano',
                    'crushed tomatoes',
                    'red wine',
                    'onions']

missing_value = ['extra lean ground beef']


imperfectRecipe = [
                    'red chili peppers',
                    'star anise',
                    'beansprouts',
                    'fish sauce',
                    'rice noodles',
                    'salt',
                    'coriander',
                    'spring onions',
                    'garlic',
                    'onions',
                    'sugar',
                    'ginger',
                    'cinnamon sticks'
                    ]
missing_value = ['beef steak']


imperfectRecipe = ['black beans',
                   'chili powder',
                   'purple onion',
                   'fresh cilantro',
                   'tilapia fillets',
                   'red pepper flakes',
                   'cumin',
                   'cooked rice',
                   'corn',
                   'garlic']
missing_value = ['red pepper']

imperfectRecipe = [
                    'sugar',
                    'whipping cream',
                    'toasted almonds',
                    'powdered sugar',
                    'amaretto',
                    'cake flour',
                    'eggs',
                    'baking powder',
                    'vanilla extract',
                    'slivered almonds',
                    'salt']
missing_value = ['red currant jelly']


imperfectRecipe = [
                    'ground cinnamon',
                    'golden raisins',
                    'red bell pepper',
                    'kosher salt',
                    'yellow onion',
                    'ground cumin',
                    'black pepper',
                    'lemon',
                    'tomatoes',
                    'olive oil',
                    'shrimp']
missing_value = ['couscous']


imperfectRecipe = [
                    'soy sauce',
                    'vegetable oil',
                    'oyster sauce',
                    'Shaoxing wine',
                    'tapioca starch',
                    'beef sirloin',
                    'chicken stock',
                    'ground black pepper',
                    'large garlic cloves',
                    'noodles',
                    'sugar',
                    'dark sesame oil']
missing_value = ['gai lan']

imperfectRecipe = [

                    'agave nectar',
                    'scallions',
                    'fresh mint',
                    'lime juice',
                    'carrots',
                    'gluten-free tamari',
                    'water',
                    'rice noodles',
                    'unsalted peanut butter',
                    'toasted sesame oil',
                    'fresh cilantro',
                    'garlic',
                    'red bell pepper']

missing_value = ['extra firm tofu']

imperfectRecipe = [

                    'sugar',
                    'vegetable oil',
                    'salt',
                    'potato starch',
                    'sesame seeds',
                    'ginger',
                    'toasted sesame oil',
                    'chicken wings',
                    'gochugaru',
                    'garlic',
                    'soy sauce',
                    'liquor']

missing_value = ['Gochujang base']
#######  sesame oil,scallions   

imperfectRecipe = [

                    'pepper',
                    'hash brown',
                    'green pepper',
                    'milk',
                    'salt',
                    'eggs',
                    'fully cooked ham',
                    'sharp cheddar cheese']
missing_value = ['butter']
##   shredded cheddar cheese,flour

imperfectRecipe = [

                    'water',
                    'lean ground beef',
                    'lasagna noodles',
                    'shredded mozzarella cheese',
                    'eggs',
                    'ground black pepper',
                    'salt',
                    'cottage cheese',
                    'grated parmesan cheese',
                    'dried parsley']

missing_value = ['pasta sauce']
#####tomato paste,ground beef , parmesan cheese  

imperfectRecipe = [
                  'light soy sauce',
                  'scallions',
                  'canola oil',
                  'cremini mushrooms',
                  'rice wine',
                  'carrots',
                  'eggs',
                  'shiitake',
                  'oyster sauce',
                  'gari',
                  'frozen peas']

missing_value = ['white rice']  
##sesame oil ,soy sauce ,corn starch,chicken stock

imperfectRecipe = [
                    'lean ground pork',
                    'salt',
                    'green beans',
                    'low sodium soy sauce',
                    'garlic',
                    'corn starch',
                    'hoisin sauce',
                    'peanut oil',
                    'sugar',
                    'crushed red pepper',
                    'ground white pepper']
missing_value = ['cooked white rice']
#  scallions  ,soy sauce   
'''
imperfectRecipe = [
                    'whole wheat hamburger buns',
                    'baby spinach',
                    'canola oil',
                    'grated parmesan cheese',
                    'chili sauce',
                    'part-skim mozzarella cheese',
                    'green pepper',
                    'italian seasoning',
                    'parsley flakes',
                    'ricotta cheese']

missing_value = ['ground beef']



num_recomand = 5
k = 100
time_start1 = time.time()
ingredient2vec = Word2Vec.load('ingredient2vecV2.model')
k_recipe = top_k_similar_withI2V(imperfectRecipe, data, k, ingredient2vec)
print(k_recipe)
print('---------------------------------------------------------------------------------------')
trainData = []
for i in range(len(data)):
    recipe = data[i]
    if recipe['id'] in k_recipe:
        print(recipe['ingredients'])

        trainData.append(recipe['ingredients'])

print('---------------------------------------------------------------------------------------')

# call associate rule mining and print frequent itemsets and it's posibility
"""
from associateRule import FPgrowth
clf1 = FPgrowth()
pred1 = clf1.train(trainData)
arm_res = pred1[1]
"""

################--------------
from fpgrowth import Fp_growth
import pyfpgrowth
#data_set = load_data(path)
#fp = Fp_growth()

#arm_res = fp.generate_R(trainData, min_support=3, min_conf=0.3)
patterns = pyfpgrowth.find_frequent_patterns(trainData, 3)

arm_res = pyfpgrowth.generate_association_rules(patterns, 0.3)
# sellect proper result and print it
time_end1 = time.time()
incpltset = set(imperfectRecipe)
missingset = set(missing_value)

candidate_list = []
candidate_ingredients = list(set([ingres[0] for ingres in patterns.keys() if len(ingres)==1]))
for candi in candidate_ingredients:
    if candi not in missingset | incpltset:
        candidate_list.append([candi, patterns[(candi,)]])

candidate_df = pd.DataFrame.from_records(candidate_list,
                                         columns=['candidate', 'support'])

# print proper result
print("Runtime of FP-growth:", time_end1-time_start1)
print('---------------------------------------------------------------------------------------')
print('we have following ingredients : ', imperfectRecipe)
print('our missing ingredient: ', missing_value)
print('\n')
print(patterns)
print('---------------------------------------------------------------------------------------')
print(candidate_df)
print('---------------------------------------------------------------------------------------')
print(candidate_df.nlargest(num_recomand, columns=['support']))