import requests

def elementFR(element):
    if element == 'water':
        return 'Eau'
    elif element == 'fire':
        return 'Feu'
    elif element == 'earth':
        return 'Terre'
    elif element == 'fire':
        return 'Feu'
    elif element == 'air':
        return 'Air'

def upgradesList(spell):
    res =''
    for i in spell['upgrades']:
        if(res):
            res = res + ' | ' + i['name']
        else:
            res = i['name']
    return res

def ingredient(data):
    res = ''
    if data['title'] is not None:
        res = res + data['title'] + ' : '
    res = res + data['text']
    return res


def ingredients(ingredients):
    return '\n\n' + ' | '.join(map(ingredient, ingredients))

def showCreature(name):
    r = requests.get('https://mmeg-db.com/fr/api/creatures/show?search=' + name)
    dictjson = r.json()['data'][0]
    

    res = dict()

    res['title'] = dictjson['name'] + ' ' + elementFR(dictjson['element'])
    res['image'] = dictjson['image']
    res['provider'] = dictjson['url']

    res['head'] = '**Nom** : ' + dictjson['name'] \
     + '\n**Element** : ''' + elementFR(dictjson['element']) \
     + '\n**Etoiles** : ''' + str(dictjson['stars'])   


    res['stats'] = '**HP** : ' + str(dictjson['hp']) \
    + '\n**Def** : ' + str(dictjson['defense']) \
    + '\n**Attaque** : ' + str(dictjson['attack']) \
    + '\n**CC :** ' + str(dictjson['criticalChance']) \
    + '\n**DCC** : ' + str(dictjson['criticalDamage']) \
    + '\n**Précision** : ' + str(dictjson['accuracy'] ) \
    + '\n**Vitesse** : ' + str(dictjson['speed']) \
    + '\n**Resistance** : ' + str(dictjson['resistance'])

    res['spells']= '\n**1. ' + dictjson['spells'][0]['title'] + '**\n' \
    + dictjson['spells'][0]['text'] \
    + ingredients(dictjson['spells'][0]['ingredients']) \
    + '\n\n*Upgrades* : ' + upgradesList(dictjson['spells'][0]) \
    + '\n\n**2. ' + dictjson['spells'][1]['title'] + '**\n' \
    + dictjson['spells'][1]['text'] \
    + ingredients(dictjson['spells'][1]['ingredients']) \
    + '\n\n*Upgrades* : ' + upgradesList(dictjson['spells'][1]) \
    + '\n\n**3. ' + dictjson['spells'][2]['title'] + '**\n' \
    + dictjson['spells'][2]['text'] \
    + ingredients(dictjson['spells'][2]['ingredients']) \
    + '\n\n*Upgrades* : ' + upgradesList(dictjson['spells'][2]) \

    return res

