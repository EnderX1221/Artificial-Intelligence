class Dog:
    def __init__(self, name, age):
        self.name = name #attribute
        self.age = age #attribute
        
    def bark(self): #method
        return f"{self.name} barks!"