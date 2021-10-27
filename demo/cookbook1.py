from collections import defaultdict
from operator import itemgetter
from itertools import groupby

# d = defaultdict(list)
# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(4)
# print(d)
#
# rows = [
#     {'address': '5412 N CLARK', 'date': '07/01/2012'},
#     {'address': '5148 N CLARK', 'date': '07/04/2012'},
#     {'address': '5800 E 58TH', 'date': '07/02/2012'},
#     {'address': '2122 N CLARK', 'date': '07/03/2012'},
#     {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
#     {'address': '1060 W ADDISON', 'date': '07/02/2012'},
#     {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
#     {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
# ]
# # 排序
# rows.sort(key=itemgetter("date"))
# for date, items in groupby(rows, key=itemgetter('date')):
#     print(date)
#     for i in items:
#         print(' ', i)
# # 不进行排序 直接使用字段
# rows_by_date = defaultdict(list)
# for row in rows:
#     rows_by_date[row['date']].append(row)
# print(rows_by_date)
import hashlib


def c_md5(file):
    with open(file, "rb") as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        _hash = md5obj.hexdigest()
    return str(_hash)

if __name__ == '__main__':
    # print(c_md5("f:/download/SecureLink-2.8.0-519-1437-win-x64.exe"))
    print(c_md5("f:/download/SecureLink-2.8.0-522-1440-win-x64.exe"))
    print(c_md5("f:/download/SecureLink-2.8.0-522-1440-win-ia32.exe"))