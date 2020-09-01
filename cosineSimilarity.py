import numpy as np


def top_k_similar(imperfectRecipe, data, topK):
    cos = dict()
    k_cos = []
    for i in range(len(data)):
        com_recipe = data[i]
        com_ingredients = com_recipe['ingredients']
        com_l = []
        l = []
        factors = com_ingredients + imperfectRecipe
        setFactors = set(factors)
        listFactors = list(setFactors)

        # create ingredients vector of our recipe
        for j in range(len(listFactors)):
            if listFactors[j] in imperfectRecipe:
                l.append(1)
            else:
                l.append(0)

        # create ingredients vector of compared recipe
        for k in range(len(listFactors)):
            if listFactors[k] in com_ingredients:
                com_l.append(1)
            else:
                com_l.append(0)

        com_id = com_recipe['id']
        # cosine similarity
        dot_product = np.dot(l, com_l)
        norm_l = np.linalg.norm(l)
        norm_coml = np.linalg.norm(com_l)

        # collect recipe's id and it's cosine similarity as a dictionay
        cos[com_id] = dot_product / (norm_l * norm_coml)

    # sort the cos similarity list
    sort_cos = sorted(cos.items(), key=lambda x: x[1], reverse=True)
    #print(sort_cos)

    # select k top similar recipe
    k = topK
    k_recipe = []
    for n in range(k):
        k_cos.append(sort_cos[n])
        k_recipe.append(sort_cos[n][0])
    print(k_cos)

    return k_recipe
