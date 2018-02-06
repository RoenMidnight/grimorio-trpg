import json

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

def parserJson(magica):
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

    return data

def criarMarkdown():
    magias = []
    lerArquivo('magias.txt', magias)

    for i in magias:
        spell = parserJson(i)
        nomeArquivo = spell['Nome'].replace('/', '-')
        nomeArquivo = "../_posts/2018-01-01-" + nomeArquivo.replace(' ', '-') + ".markdown"
        w = open(nomeArquivo, 'w', encoding="utf-8")

        w.write("---\nlayout: post\ntitle:  \"" + spell['Nome'] + "\"\n")
        w.write("date:   2018-01-01\n")
        w.write("source: " + spell['Fonte'] + "\n")
        w.write("tags: [nenhum, bardo]\n---\n\n")

        w.write("**" + spell['Nível'] + "**\n\n")

        for key, value in spell.items():
            if(key != 'Nome' and key != 'Fonte' and key != 'Descrição' and key != 'Nível'):
                w.write("**" + key + "**: " + value + "\n\n")

        w.write(spell['Descrição']+ "\n")

        w.close()




criarMarkdown()
