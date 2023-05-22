# Main class of the task which is the Animal class
class Animal(object):
    '''Animal class docstring'''
    def __init__(self, numteeth, spots, weight):
        self.numteeth = numteeth
        self.spots = spots
        self.weight = weight

class Lion(Animal):
    '''This class inherits its constructor and the get_color method from Animal'''
    def __init__(self, numteeth, spots, weight):
        super().__init__(numteeth, spots, weight)

    # The distinct features of a Lion
    mane = "Mane"
    color = "Yellow"
    
    '''This method uses the weight of the Lion to define the lion type'''
    def lion_weight(self):
        if self.weight <= 80:
            self.lion_type = "Cub"
            return self.lion_type
        elif self.weight <= 120: 
            self.lion_type = "Adult Female"
            return self.lion_type
        elif self.weight > 120:
            self.lion_type ="Adult Male"
            return self.lion_type
         
class Cheetah(Animal):
    '''This class inherits its constructor and the get_color method from Animal'''
    def __init__(self, numteeth, spots, weight):
        super().__init__(numteeth, spots, weight)
    
    '''This is an array of the prey a cheetah catches'''
    cheetah_prey = ["SpringBok", "Rabbits", "Meerkat"]


#### Animal objects

# Output for Lion
lion = Lion(30, "No", 121)
print("Type of Lion: " + lion.lion_weight())

# Output for Cheetah
cheetah = Cheetah(20, "Yes", 80)
print(cheetah)

# References
# Working with classes, Inheritance retrieved 19/09/2021 from https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=7
# inheritance Capstone retrieved 19/09/2021 from C:\Users\user-pc\Dropbox\Naledi Motau-105175\Python for Data Science\Task 17\DS L1T17 - Capstone Project II.pdf