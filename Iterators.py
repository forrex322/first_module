from itertools import islice


class itr:

    def __init__(self, l):
        self.l = l
        self.index = len(self.l)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.l[self.index]


def reverse_list(l):
    for index in reversed(range(len(l))):
        yield l[index]


l = [1, 2, 3, 4, 5]

print('Iterator class')
i = itr(l)
print(list(islice(i, 0, 5)))

print('##################')

print('Generator function')
print('reverse_list')
rev = reverse_list(l)
print(list(islice(rev, 0, None)))

print('##################')

# Generator function
print('Generator function')
for item in reverse_list(l):
    print(item)

print('##################')

# Generator expression(list comprehension)
# l[::-1]
print('Generator expression')
[print(i) for i in l[::-1]]
