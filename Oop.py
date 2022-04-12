class AnyClass:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        attrs = ["%s = %s" % (key, value) for (key, value) in self.__dict__.items()]
        classname = self.__class__.__name__
        return "%s: %s" % (classname, " ".join(attrs))


a = AnyClass(first=1, second=2, thrid=3)
print(a)
