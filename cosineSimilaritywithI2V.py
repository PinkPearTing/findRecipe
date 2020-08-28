import numpy as np

def getRecipeSimilaritywithI2V(recipeA, recipeB, ingredient2vec):
    """
    :param recipeA: a list of ingredients
    :param recipeB: a list of ingredients
    :return:
    """
    vectorListA, vectorListB = [],[]
    commonIngres = list(set(recipeA+recipeB))
    for ingre in commonIngres:
        if ingre in recipeA:
            vectorListA.append(1)
        else:
            vectorListA.append(max([ingredient2vec.similarity(ingre, ingre_i) for ingre_i in recipeA]))

        if ingre in recipeB:
            vectorListB.append(1)
        else:
            vectorListB.append(max([ingredient2vec.similarity(ingre, ingre_i) for ingre_i in recipeB]))

    # cosine similarity
    dot_product = np.dot(vectorListA, vectorListB)
    norm_l = np.linalg.norm(vectorListA)
    norm_coml = np.linalg.norm(vectorListB)
    # collect recipe's id and it's cosine similarity as a dictionay
    similarity = dot_product / (norm_l * norm_coml)

    return similarity

def top_k_similar_withI2V(imperfectRecipe, data, topK, ingredient2vec):
    cos = dict()
    k_cos = []
    for i in range(len(data)):
        com_recipe = data[i]
        com_ingredients = com_recipe['ingredients']

        cos[com_recipe['id']] = getRecipeSimilaritywithI2V(imperfectRecipe, com_ingredients, ingredient2vec)

        # collect recipe's id and it's cosine similarity as a dictionay

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

