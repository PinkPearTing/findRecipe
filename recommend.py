# -*- coding: utf-8 -*-
import math
import re

import json


def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        json_array = json.loads(content)
    return json_array


def words_count(words):
    words_dict = {}
    for word in words:
        word = re.sub('[^a-zA-Z]', '', word)
        word = word.lower()
        if word != '' and word in words_dict:
            num = words_dict[word]
            words_dict[word] = num + 1
        elif word != '':
            words_dict[word] = 1
        else:
            continue
    return words_dict


def cosine_similarity(text_a, text_b):
    text_a = text_a.split(',')
    words1_dict = words_count(text_a)
    words2_dict = words_count(text_b)

    dic1 = sorted(words1_dict.items(), key=lambda asd: asd[1], reverse=True)
    dic2 = sorted(words2_dict.items(), key=lambda asd: asd[1], reverse=True)
    words_key = []
    for i in range(len(dic1)):
        words_key.append(dic1[i][0])
    for i in range(len(dic2)):
        if dic2[i][0] in words_key:
            pass
        else:
            words_key.append(dic2[i][0])
    vect1 = []
    vect2 = []
    for word in words_key:
        if word in words1_dict:
            vect1.append(words1_dict[word])
        else:
            vect1.append(0)
        if word in words2_dict:
            vect2.append(words2_dict[word])
        else:
            vect2.append(0)
    sum = 0
    sq1 = 0
    sq2 = 0
    for i in range(len(vect1)):
        sum += vect1[i] * vect2[i]
        sq1 += pow(vect1[i], 2)
        sq2 += pow(vect2[i], 2)
    try:
        result = round(float(sum) / (math.sqrt(sq1) * math.sqrt(sq2)), 2)
    except ZeroDivisionError:
        result = 0.0
    return result


def recommendation(user_input_str, user_input_file):
    json_array = load_file(user_input_file)
    key_value_result = {}
    key_value_ingredients = {}
    for json_item in json_array:
        json_str = json.dumps(json_item)
        json_object = json.loads(json_str)
        id = json_object['id']
        ingredients = json_object['ingredients']
        score = cosine_similarity(user_input_str, ingredients)
        key_value_result[id] = score
        key_value_ingredients[id] = ingredients
    result = sorted(key_value_result.items(), key=lambda kv: (kv[1], kv[0]))
    # print(result[len(result) - 1])
    # print(type(result[len(result) - 1]))
    number = result[len(result) - 1][0]
    # print(key_value_ingredients[number])
    recommendation_ingredients = key_value_ingredients[number]
    user_input_ingredients = user_input_str.split(',')
    recommendation_ingredients_result = []
    for one_recommendation in recommendation_ingredients:
        if one_recommendation not in user_input_ingredients:
            recommendation_ingredients_result.append(one_recommendation)
    return recommendation_ingredients_result


if __name__ == '__main__':
    recommendation_ingredients_result = recommendation('baking powder,eggs,all-purpose flour', 'test 2.json')
    print(recommendation_ingredients_result)
