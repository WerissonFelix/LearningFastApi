'''  
    We can declare a class as the type of a variable
'''

class Person:
    def __init__(self, name: str):
        self.name = name
        
def get_person_name(one_person: Person):
    return one_person.name

''' 
That means  the variable one_person is an instance of the class Person, and
it doesn't mean one_person is the class called Person.

'''