#Александр Шанчук ТА-20V
#Задача ( №7.2) / Вариант ( №17 ) / Страница ( №115 )
#Одесса  2011
#В  заданной  строке  заменить  каждый  символ  «No»  строкой  «номер  по порядку».
#перед тем чтобы запустить надо скачать файл text.txt

filename = "text.txt"#название файла text.txt 
with open(filename, encoding="utf8") as file: #открывает фаил по названию в формате utf-8
    txt = file.read()#читает файл 
    x = txt.replace("№", "номер  по порядку ")#меняем слово № на номер  по порядку

print("ИСХОДНЫЙ ВАРИАНТ \n")
print(txt) #выписывает исходный вариант
print("")#отделяет исходный вариант от готового
print("ГОТОВЫЙ ВАРИАНТ \n")
print(x)#выписывает готовый вариант