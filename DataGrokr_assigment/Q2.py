#Abstract class
from abc import ABC,abstractmethod
class Something(ABC):
    @abstractmethod
    def get_gender(self):
        pass
    
class Male(Something):
    def get_gender(self):
        return "male"
class Female(Something):
    def get_gender(self):
        return "female"
class Notprefered(Something):
    def get_gender(self):
        return "NOt prefereed"    
male=Male().get_gender()
print(male)
female=Female().get_gender()
print(female)
notpr=Notprefered().get_gender()
print(notpr)
