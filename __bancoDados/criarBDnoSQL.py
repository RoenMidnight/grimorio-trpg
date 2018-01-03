import json
from pymongo import MongoClient

def lerArquivo(nomeArquivo, magias):
    f = open(nomeArquivo, 'r', encoding="utf-8")
    linhas = f.readlines()

    temp = ''
    for i in linhas:
        if(i == '\n'):
            magias.append(temp[:len(temp)-1])
            temp = ''
        else:
            temp += i

def parserJson(magica, collection):
    spell = magica
    data = {}
    data['Nome'] = spell[:spell.find('\n')]

    spell = spell[spell.find('\n') + 1:]
    cab = spell[:spell.find('\n') - 1]
    spell = spell[spell.find('\n') + 1:]
    cabecalho = cab.split('; ')

    for i in cabecalho:
        data[i[:i.find(':')]] = i[i.find(':') + 2:]

    fonte = spell[spell.rfind('\n') + 1:]
    spell = spell[:spell.rfind('\n')]

    data['Fonte'] = fonte[fonte.find(':') + 2:]
    data['Descrição'] = spell

    busca = collection.find_one({"Nome": data['Nome']})
    if(busca is None):
        magica_id = collection.insert_one(data)
    else:
        json_data = json.dumps(data)
        collection.update_one({"Nome":data['Nome']}, {"$set": data})
    return data

def popularBancoDados(collection):
    magias = []
    lerArquivo('magias.txt', magias)

    for i in magias:
        parserJson(i, collection)


cliente = MongoClient('localhost', 27017)
db = cliente.TormentaRPG
collection = db.magia

popularBancoDados(collection)

cliente.close()
