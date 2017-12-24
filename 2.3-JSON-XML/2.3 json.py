import json
from collections import Counter

def ten_most_common(lst):
    cnt = Counter(lst).most_common(10)
    return cnt

def top_ten(filename, enc):
    with open(filename, encoding=enc) as f:
        js = json.load(f)
        js = js.get("rss")
        js = js.get("channel")
        js = js.get("items")
        lst = []

        for item in js:
            desc = item.get("description")
            title = item.get("title")
            lst.append(desc)
            lst.append(title)

        str1 = ' '.join(lst)
        str1 = str1.lower()
        lst = str1.split()
        lst = filter(str.isalnum, lst)
        lst = [item for item in lst if len(item) > 6]
        return ten_most_common(lst)


print('10 most common words:\n newsafr.json:', top_ten('newsafr.json', 'UTF-8'),'\n newscy.json:', top_ten('newscy.json', 'KOI8-R'),  \
     '\n newsfr.json:', top_ten('newsfr.json', 'ISO_8859-5'),'\n newsit.json:', top_ten('newsit.json', 'Windows_1251'))
