from operator import itemgetter

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

