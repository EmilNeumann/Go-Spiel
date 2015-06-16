'''
Created on 15.06.2015

@author: Emil
'''
class pet():
    number_of_legs = 0
    def sleep(self):
        print "zzz"
    def count_legs(self):
        print "I have %s legs." % self.number_of_legs
        
class dog(pet):
    number_of_legs = 4
    def bark(self):
        print "Woof"
        
class dalmatiner(dog):
    number_of_legs = 4
    
doug = dog()
doug.sleep()
doug.bark()
doug.count_legs()

nemo = pet()
nemo.sleep()
nemo.count_legs()