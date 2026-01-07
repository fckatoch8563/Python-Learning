from abc import ABC, abstractmethod


class BaseA(ABC):
    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError


class SubA(BaseA):
    @property
    def name(self):
        return "Alice"


class SubB(BaseA):
    @property
    def name(self):
        return "Bob"


# usage
try:
    BaseA()  # raises TypeError because name is abstract
except TypeError as e:
    print("BaseA failed to instantiate:", e)

s1 = SubA()
print(s1.name)  # Alice

s2 = SubB()
print(s2.name)  # Bob

#####################################################################################
from abc import ABC, abstractmethod


class MyBase(ABC):
    @property
    @abstractmethod
    def name(self):
        """Abstract property that must be implemented by subclasses"""
        raise NotImplementedError


# attempting to instantiate the abstract base fails
try:
    MyBase()
except TypeError as e:
    print("Instantiation failed:", e)


# concrete subclass implements the abstract property
class Concrete(MyBase):
    @property
    def name(self):
        return "ConcreteName"


c = Concrete()
print("Concrete instance name:", c.name)
