import enum
from collections import deque
import uuid

class Sizes(enum.Enum):
    Small = 0
    Medium = 1
    Large = 2
    __numVal = 0

    def __init__(self,nums:int):
        self.__numVal = nums

    def getNumVals(self):
        return self.__numVal


class Package:
    __packageSize: Sizes
    __packageId = ""

    def __init__(self,size : Sizes):
        self.__packageSize = size
        self.__packageId = uuid.uuid1()

    def __getSize(self):
        return self.__packageSize

    def __getPackageId(self):
        return self.__packageId


class Locker:
    __lockerSize: Sizes
    __lockerId = ""
    __packageInsideLocker: Package

    def __init__(self, size: Sizes):
        self.__lockerSize = size
        self.__lockerId = uuid.uuid1()

    def __getSize(self):
        return self.__lockerSize

    def __getLockerId(self):
        return self.__lockerId

    def emptyLocker(self)->Package:
        return self.__packageInsideLocker




class Objekt :
    __Size: Sizes
    __Id = ""

    def __init__(self, size: Sizes):
        self.__Size = size
        self.__Id = uuid.uuid1()

    def __getSize(self):
        return self.__Size

    def __getId(self):
        return self.__Id



class Locker1(Objekt):

    __packageInsideLocker: Package

    def __init__(self,obj):
        super().__init__(obj)

    def emptyLocker(self)->Package:
        current_package = self.__packageInsideLocker
        self.__packageInsideLocker = None

        return current_package

    def assignPackage(self,pack :Package):
        self.__packageInsideLocker = pack


class Package1(Objekt):
    def __init__(self, obj):
        super().__init__(obj)


class PickupLocation:

    availableLockers = dict(Sizes,deque(Locker1))
    packageLoc = dict(str, Locker1)

    def __init__(self,lockerSizes):
        for item in lockerSizes:
            pass






if __name__ == '__main__':

    size1 = Sizes(1)
    size2 = Sizes(2)

    firstPackage = Package1(size1)
    firstLocker  = Locker1(size2)
    firstLocker.assignPackage(firstPackage)
    x= 1



