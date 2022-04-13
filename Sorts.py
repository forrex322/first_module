from operator import itemgetter

print(sorted([(3, 2, 3, 5), (2, 1), (5, 1, 5, 2, 5, 7, 8), (2, 7)], key=lambda x: x[-1], reverse=True))


def sort_without_z(s):
    xlist = list()
    for item in s:
        if item.startswith('z'):
            xlist.append(item)
            s.remove(item)
    print(sorted(xlist) + sorted(s))
    del xlist[:]


print(sort_without_z(['zxc', 'xzc', 'zcx', 'cxz', 'zxx', 'vbv']))

l = ['zxc', 'xzc', 'zcx', 'cxz', 'zxx', 'vbv']
print(sorted(l, key=lambda x: (not x.startswith('z'), x)))
