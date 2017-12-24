import xml.etree.ElementTree as ET
from collections import Counter

def ten_most_common(lst):
    cnt = Counter(lst).most_common(10)
    return cnt

def top_ten(filename):

    tree = ET.parse(filename)
    root = tree.getroot()
    lst = []
    root = root[0]

    for kek in root:
        for lel in kek:
            if lel.tag == 'description':
                lst.append(lel.text)
            elif lel.tag == 'title':
                lst.append(lel.text)

    str1 = ' '.join(lst)
    lst = str1.split()
    lst = filter(str.isalnum, lst)
    lst = [item for item in lst if len(item) > 6]
    return ten_most_common(lst)

print('10 most common words:\n newsafr.xml:', top_ten('newsafr.xml'),'\n newscy.xml:', top_ten('newscy.xml'),  \
     '\n newsfr.xml:', top_ten('newsfr.xml'),'\n  newsit.xml:', top_ten('newsit.xml'))

# Во всех файлах, кроме newsit, я получаю ошибку not well-formed (invalid token). Понимаю, что проблема в том,
# что парсер не определяет кодировку, но как её указать, ума не приложу. ET.parse не принимает аргумент encoding.
#
# Что я делаю не так?
