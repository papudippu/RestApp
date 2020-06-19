
class Person:
    def __init__(self, name, mother, father):
        self.name = name
        self.mother =mother
        self.father =father

    def getNamesOfAllAncestors(self, resultArray=None):

        if resultArray is None:
            resultArray = []

        resultArray.append(self.name)
        if self.mother != None:

            self.mother.getNamesOfAllAncestors (resultArray)
        else:

            pass

        if self.father != None:
            self.father.getNamesOfAllAncestors (resultArray)
        else:
            pass

        return resultArray

john = Person( "John",
               Person( "Jane",
                       Person("Jill", None, None),
                       Person("Jack", None, None)),
               Person( "Jim",
                       Person("Josephine", None, None),
                       Person("Joe", None, None) ) )


ancestors = john.getNamesOfAllAncestors()
print(', '.join(ancestors))
# will print “John, Jane, Jill, Jack, Jim, Josephine, Joe”