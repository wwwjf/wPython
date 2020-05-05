class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name = name

    @property
    def getAge(self):
        return self.__age

    def setAge(self,age):
        self.__age = age


person = Person('zhangsan',18)
print('{0},{1}'.format(person.getName(),person.getAge))