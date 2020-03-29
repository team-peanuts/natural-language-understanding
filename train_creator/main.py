import json
import random

from duckling import DucklingWrapper, Language, Duckling
from padatious import IntentContainer
import pandas as pd

if __name__ == '__main__':

    df = pd.read_csv('product.csv', delimiter=';')

    train_data = dict()
    train_data['rasa_nlu_data'] = dict()
    train_data['rasa_nlu_data']["common_examples"] = []
    train_data['rasa_nlu_data']["regex_features"] = []
    train_data['rasa_nlu_data']["common_examples"] = []
    train_data['rasa_nlu_data']["entity_synonyms"] = []

    start = [
        'I would like to buy ',
        'I want '
    ]
    middle = [
        ', ',
        'and '
    ]
    end = [
        '.'
    ]

    for s in start:
        for i in range(100):
            sentence = dict()
            sentence['text'] = s
            sentence['intent'] = 'buy'
            sentence['entities'] = []

            txt = df.sample().iloc[0,0]
            ent = dict()
            ent['start'] = len(sentence['text'])
            ent['end'] = len(sentence['text'] + txt)
            ent['value'] = txt
            ent['entity'] = 'product'
            sentence['entities'].append(ent)
            sentence['text'] += txt + " "

            while random.random() > .5:
                m = random.choice(middle)
                sentence['text'] += m
                txt = df.sample().iloc[0, 0]
                ent = dict()
                ent['start'] = len(sentence['text'])
                ent['end'] = len(sentence['text'] + txt)
                ent['value'] = txt
                ent['entity'] = 'product'
                sentence['entities'].append(ent)
                sentence['text'] += txt+ " "

            sentence['text'] += random.choice(end)
            train_data['rasa_nlu_data']["common_examples"].append(sentence)

    with open('result.json', 'w+') as fp:
        json.dump(train_data, fp)










    container = IntentContainer('intent_cache')




    d = DucklingWrapper()
    d.parse('Bring me 250 ml sugar')
    d.parse_
    print(d.parse_time(u'Let\'s meet at 11:45am'))
    print(d.parse_number(u'Bring me one conserve of ravioli'))
    print(d.parse_quantity(u'Bring me 100 g of sugar'))