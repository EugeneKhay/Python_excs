# exc 7
def ubbi_dubbi(word):
    res = []
    out = list(word)
    for i in out:
        if i in 'aeiuo':
            res.append('ub' + i)
        else:
            res.append(i)
    return "".join(res)


# exc 8
def strsort(s):
    return "".join(sorted(s, reverse=True))


# print(strsort('cba'))
# print(ubbi_dubbi("Elephant"))


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return repr((self.name, self.age))

# print(Student("John", 33))
