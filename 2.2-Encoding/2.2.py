import chardet

def ten_most_common(lst):
    set_l = set(lst)
    largest = sorted(set_l, key=lst.count, reverse=True)[:10]
    return largest

def top_ten(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        dec = data.decode(result['encoding'])
        lst = list(dec.split())
        lst = [item for item in lst if len(item) > 6]
        return ten_most_common(lst)

print('10 most common words:\n newsafr.txt:', top_ten('newsafr.txt'),'\n newscy.txt:', top_ten('newscy.txt'),  \
     '\n newsfr.txt:', top_ten('newsfr.txt'),'\n newsit.txt:', top_ten('newsit.txt'))
