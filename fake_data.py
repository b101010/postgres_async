import random
import string


class fakeString():

    def __init__(self, length: int):
        self.length = length

    def genStr(self) -> str:
        characters = string.ascii_letters + string.digits
        myString = ''.join(random.choice(characters) for _ in range(self.length))

        return myString


class fakeList(fakeString):

    def __init__(self, length: int, count: int):
        super().__init__(length)
        self.count = count

    def genList(self) -> list:
        myList = []
        fs = fakeString(self.length)
        for _ in range(self.count):        
            myList.append(fs.genStr())

        return myList      


class fakeDicts(fakeList):
    def __init__(self, length: int, count: int, field: str):
        super().__init__(length, count)
        self.field = field

    def genDicts(self) -> list:
        myList = []
        fl = fakeList(self.length, self.count)
        tmpList = fl.genList()
        for item in tmpList:
            tmpDict = {}
            tmpDict[self.field] = item
            myList.append(tmpDict)

        return myList
