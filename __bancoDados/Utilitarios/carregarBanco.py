import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import string
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')



def separarPorDescritor(magias):
    descritores = []

    for i in magias:
        nivel = i["Nível"]
        nivel = nivel[nivel.find("(")+1 : nivel.find(")")]

        if (" e " in nivel):
            nivel = nivel.replace(" e ", ", ")
        if (" ou " in nivel):
            nivel = nivel.replace(" ou ", ", ")

        spt = nivel.split(", ")
        for j in spt:
            if (j not in descritores):
                descritores.append(j)

    descritores.sort(key=locale.strxfrm)

    for i in descritores:
        print(i)

def mostrarMagiasPorDescritor(magias, spell):
    descritores = []
    flag = True
    print(type(spell))

    for i in magias:
        nivel = i["Nível"]
        nivel = nivel[nivel.find("(")+1 : nivel.find(")")]

        if (" e " in nivel):
            nivel = nivel.replace(" e ", ", ")
        if (" ou " in nivel):
            nivel = nivel.replace(" ou ", ", ")

        spt = nivel.split(", ")
        for j in spt:
            if(flag):
                print(type(j))
                flag = False
            if (j == spell):
                print("!!!!!!!!")
                print(i)
            # if (j not in descritores):
            #     descritores.append(j)

    # descritores.sort(key=locale.strxfrm)

    # for i in descritores:
    #     print(i)


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://tormentarpg-2018.firebaseio.com/'
})

ref = db.reference('Magias')
magias = ref.get()

# separarPorDescritor(magias)
# mostrarMagiasPorDescritor(magias, "muito caos")
mostrarMagiasPorDescritor(magias, "descritor igual à magia imitada")
