class Human:
    # This is a special function called a constructor. It is called when you create a new object of this class
    def __init__(self, age, gender, name, cnic, password):
        self.age = age # public attributes
        self.gender = gender
        self.name = name
        self.cnic = cnic
        self.__password = password # private attribute

    # getters and setters

    def getPassword(self):
        return self.__password

    def setPassword(self, new_password):
        self.__password = new_password 

    def printInfo(self):
        print(f"Name: {self.name} | Age: {self.age} | CNIC: {self.cnic} | Password: {self.getPassword()} ")       

alyanObject = Human(19, "Male", "Alyan", "12345", "kldsflkdsfjs")
ayaanObject = Human(18, "Male", "Ayaan", "1232", "k243324sflkdsfjs")

alyanObject.setPassword("DSJHFDKJHFK")
print(alyanObject.getPassword())
alyanObject.printInfo()
ayaanObject.printInfo()
# object.publicatrr is fine
# object.__privateattr is not fine, it will not work

myage = alyanObject.age

print("Alyan's age is", myage)



