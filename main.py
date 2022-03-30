from operator import itemgetter

from Iterators import itr, reverse_list
from itertools import islice

# l = [1, 2, 3, 4, 5]
#
# i = itr()
# print(list(islice(i, 0, 1)))
#
# print('Generator function')
# print('reverse_list')
# rev = reverse_list(l)
# print(list(islice(rev, 0, None)))
#
# print('##################')
#
# # Generator function
# print('Generator function')
# for item in reverse_list(l):
#     print(item)
#
# print('###############')
#
# # Generator expression(list comprehension)
# # l[::-1]
# print('Generator expression')
# [print(i) for i in l[::-1]]


print(sorted([(3, 2), (5, 1), (2, 7)], key=itemgetter(1), reverse=True))


xlist = []
def sort_without_z(s):
    for item in s:
        if item.startswith('z'):
            xlist.append(item)
            s.remove(item)
    print(sorted(xlist) + sorted(s))
    del xlist[:]


print(sort_without_z(['zxc', 'xzc', 'zcx', 'cxz', 'zxx', 'vbv']))

# print(sorted(['xzc', 'zxc', 'cxz', 'zxx', 'vbv'])
